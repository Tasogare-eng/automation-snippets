# ai_codegen.py
from openai import OpenAI
# from dotenv import load_dotenv
import textwrap, os, pathlib, subprocess, sys

# load_dotenv()                         # .env から API キー読込み
client = OpenAI()                     # ← 環境変数 OPENAI_API_KEY を自動使用

PROMPT = """
あなたは熟練の Python エンジニアです。
次の要件に合うスクリプトをコメント付きで出力してください。
完成コードのみ ```python ...``` で囲んでください。

要件:
{task}
"""

def generate(task: str, fname="generated.py"):
    res = client.chat.completions.create(
        model="gpt-4o-mini",          # gpt‑3.5‑turbo でも可
        messages=[{"role": "user", "content": PROMPT.format(task=task.strip())}],
        temperature=0.2               # 再現重視で低温
    )
    code = res.choices[0].message.content
    with open(fname, "w") as f:
        f.write(textwrap.dedent(code.split("```python")[1].split("```")[0]))
    print(f"✅ {fname} saved")

if __name__ == "__main__":
    generate(sys.argv[1] if len(sys.argv) > 1 else "CSV を Excel に変換")
