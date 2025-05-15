import pyautogui, schedule, time, datetime as dt
def cap(): pyautogui.screenshot().save(f"{dt.datetime.now():%Y%m%d_%H%M%S}.png")
schedule.every(1).minutes.do(cap)
while True:
    schedule.run_pending() or time.sleep(1)
