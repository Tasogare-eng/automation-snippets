import schedule, threading, time

def job():
    print("タスク実行!")

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(schedule.idle_seconds() or 1)

schedule.every(1).minutes.do(job)

thread = threading.Thread(target=run_scheduler, daemon=True)
thread.start()

print("スケジューラーを起動しました。Ctrl+Cで終了できます。")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("終了します。")