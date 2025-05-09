# ⚠️注意
# "gpt-image-1"を使用するには下記のリンクでVerify Organizationをクリックしてから免許などでの本人確認が必要となります
# https://platform.openai.com/settings/organization/general

import base64
from openai import OpenAI
client = OpenAI()

prompt= """
少年がopenAIのAPIを使ってアプリを開発しているイラスト
"""

img = client.images.generate(
    model="gpt-image-1",
    prompt=prompt,
    n=1,
    size="1024x1024"
)

image_bytes = base64.b64decode(img.data[0].b64_json)
with open("output.png", "wb") as f:
    f.write(image_bytes)
