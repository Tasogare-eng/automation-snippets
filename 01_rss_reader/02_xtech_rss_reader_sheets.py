import os
import json
import requests
import feedparser
import gspread
from google.oauth2.service_account import Credentials

# ── 設定 ───────────────────────────────────────────────────────────────
RSS_URL              = "https://xtech.nikkei.com/rss/xtech-it.rdf"
PROCESSED_FILE       = "processed_ids.json"           # 処理済 ID を保存する JSON
SERVICE_ACCOUNT_FILE = "./service-account.json"
SPREADSHEET_ID       = "spread sheet id"  # スプレッドシートの ID
# ────────────────────────────────────────────────────────────────────────

# 1) 処理済 ID のロード
if os.path.exists(PROCESSED_FILE):
    with open(PROCESSED_FILE, "r", encoding="utf-8") as f:
        processed_ids = set(json.load(f))
else:
    processed_ids = set()

# 2) RSS フィード取得＆パース
resp = requests.get(RSS_URL)
resp.encoding = "utf-8"
feed = feedparser.parse(resp.content)

# 3) Google Sheets 認証
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
gc = gspread.authorize(creds)
sh = gc.open_by_key(SPREADSHEET_ID)
ws = sh.sheet1   # 先頭シートを使う場合

new_ids = []

# 4) 各エントリをループし、未処理のみを書き込み
for entry in feed.entries:
    # 一意なキーとして、まず entry.id、その次に entry.link を使う
    eid = entry.get("id") or entry.get("link")
    if eid in processed_ids:
        continue

    title     = entry.get("title", "")
    link      = entry.get("link", "")
    published = entry.get("published", "")

    # Google Sheets に 1 行追加
    ws.append_row([title, link, published], value_input_option="RAW")

    new_ids.append(eid)

# 5) 処理済 ID を更新して保存
if new_ids:
    processed_ids |= set(new_ids)
    with open(PROCESSED_FILE, "w", encoding="utf-8") as f:
        json.dump(list(processed_ids), f, ensure_ascii=False, indent=2)

print(f"{len(new_ids)} 件の新規エントリを追加しました。")