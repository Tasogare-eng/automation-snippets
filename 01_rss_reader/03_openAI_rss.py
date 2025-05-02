import os
import json
import requests
import feedparser
import gspread
from google.oauth2.service_account import Credentials

# ── 設定 ───────────────────────────────────────────────────────────────
RSS_URL              = "https://openai.com/blog/rss.xml"
PROCESSED_FILE       = "processed_openai_ids.json"     # OpenAI 用の処理済 ID
SERVICE_ACCOUNT_FILE = "./service-account.json"
SPREADSHEET_ID       = "spread sheet id"  # スプレッドシートの ID
# ────────────────────────────────────────────────────────────────────────

# 1) 前回までに処理した ID をロード
if os.path.exists(PROCESSED_FILE):
    with open(PROCESSED_FILE, "r", encoding="utf-8") as f:
        processed_ids = set(json.load(f))
else:
    processed_ids = set()

# 2) requests で RSS を取得（SSL エラー回避）
resp = requests.get(RSS_URL)
resp.encoding = "utf-8"
feed = feedparser.parse(resp.content)

# 3) Google Sheets 認証＆シート取得
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
gc = gspread.authorize(creds)
sh = gc.open_by_key(SPREADSHEET_ID)
ws = sh.sheet1

new_ids = []

# 4) 未処理のエントリだけをシートに追加
for entry in feed.entries:
    # 一意キー：entry.id（なければリンク URL）
    eid = entry.get("id") or entry.get("link")
    if eid in processed_ids:
        continue

    title     = entry.get("title", "")
    link      = entry.get("link", "")
    published = entry.get("published", "")

    # シートに追記
    ws.append_row([title, link, published], value_input_option="RAW")

    new_ids.append(eid)

# 5) 新たに処理した ID を保存
if new_ids:
    processed_ids |= set(new_ids)
    with open(PROCESSED_FILE, "w", encoding="utf-8") as f:
        json.dump(list(processed_ids), f, ensure_ascii=False, indent=2)

print(f"{len(new_ids)} 件の新規エントリを追加しました。")
