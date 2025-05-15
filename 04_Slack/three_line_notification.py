import schedule, subprocess, time, os

schedule.every().day.at("11:15").do(
  lambda: subprocess.run(["curl","-X", "POST","-d", '{"text": "がんばれ！ ☀"}', os.environ["SLACK_URL"]]))  
while True: schedule.run_pending(); time.sleep(1)  

# schedule.every().day.at("19:43").do(
#   lambda: subprocess.run([
#     "curl",
#     "-X", "POST",
#     "-H", "Content-Type: application/json",
#     "-d", '{"text": "こんにちは ☀"}', 
#     os.environ["SLACK_URL"]
#     ]))  
# while True: 
#   schedule.run_pending(); 
#   time.sleep(1)  

# SLACK webhook　Test
# import requests, json
# requests.post(os.environ["SLACK_URL"],
#               data=json.dumps({"text": "おはようございます ☀️"}))
