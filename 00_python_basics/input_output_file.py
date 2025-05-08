# 書き込み
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("こんにちは\nさようなら")

# 読み込み
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
