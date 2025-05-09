# API設定
# MAC
# export OPENAI_API_KEY="YOUR_API_KEY"
# echo $OPENAI_API_KEY

# Windows
# setx OPENAI_API_KEY "sk-XXXXXXXXXXXXXXXXXXXXXXXX"
# 確認方法：echo %OPENAI_API_KEY%

# 確認: openai 1.75.0
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4.1",
  messages=[
    {"role": "developer", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message.content)
