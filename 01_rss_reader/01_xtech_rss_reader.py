import requests
import feedparser

def fetch_and_display_rss(url: str):
    # ① レスポンスのエンコーディングを UTF-8 に設定
    resp = requests.get(url) 
    resp.encoding = 'utf-8'
    
    # ② 取得したバイト列を feedparser でパース
    feed = feedparser.parse(resp.content)

    # エラー状態の確認
    if feed.bozo:
        print("Warning: パース中に問題発生")
        print("Exception:", feed.bozo_exception)

    # フィードタイトル
    title = feed.feed.get('title', 'N/A')
    print(f"Feed Title: {title}\n")

    # エントリを表示
    for entry in feed.entries:
        print("─" * 60)
        print(f"Title    : {entry.get('title', 'N/A')}")
        print(f"Link     : {entry.get('link', 'N/A')}")
        print(f"Published: {entry.get('published', 'N/A')}")
        summary = entry.get('summary', '').strip()
        if summary:
            print(f"Summary  : {summary[:200]}{'…' if len(summary) > 200 else ''}")
    print("─" * 60)

if __name__ == "__main__":
    RSS_URL = "https://xtech.nikkei.com/rss/xtech-it.rdf"
    fetch_and_display_rss(RSS_URL)
