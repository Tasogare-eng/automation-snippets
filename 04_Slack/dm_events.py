import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import openai

# 環境変数からトークンを読み込み
SLACK_BOT_TOKEN      = os.environ["SLACK_BOT_TOKEN"]
SLACK_APP_TOKEN      = os.environ["SLACK_APP_TOKEN"]
OPENAI_API_KEY       = os.environ["OPENAI_API_KEY"]

# 初期化
app = App(token=SLACK_BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

# DM（im チャネル）を受信したら反応
@app.event("message")
def handle_dm_events(body, say, logger):
    event = body.get("event", {})
    channel_type = event.get("channel_type")
    user        = event.get("user")
    text        = event.get("text")
    channel     = event.get("channel")

    # Bot 自身の発言は無視
    if event.get("bot_id"):
        return

    # チャンネルタイプが DM (im) の場合のみ処理
    if channel_type == "im" and user and text:
        try:
            # ① OpenAI ChatCompletion 呼び出し
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "あなたは親切なアシスタントです。"},
                    {"role": "user",   "content": text}
                ],
                temperature=0.7,
                max_tokens=500,
            )
            answer = response.choices[0].message.content.strip()

            # ② Slack に返信
            say(text=answer, channel=channel)

        except Exception as e:
            logger.error(f"Error calling OpenAI or replying: {e}")
            say(text="申し訳ありません。内部エラーが発生しました。", channel=channel)

# アプリ起動 (Socket Mode 使用例)
if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
