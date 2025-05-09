# API設定
# MAC
# export OPENAI_API_KEY="YOUR_API_KEY"
# echo $OPENAI_API_KEY

# Windows
# setx OPENAI_API_KEY "sk-XXXXXXXXXXXXXXXXXXXXXXXX"
# 確認方法：echo %OPENAI_API_KEY%

# 確認: openai 1.75.0
import base64
from openai import OpenAI

client = OpenAI()

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Path to your image
image_path = "local_image.png"

# Getting the Base64 string
base64_image = encode_image(image_path)

completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "user",
            "content": [
                { "type": "text", "text": "このイメージはなんですか?" },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
)

print(completion.choices[0].message.content)