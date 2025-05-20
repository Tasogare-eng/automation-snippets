import os
from PIL import Image

file_path = "./a.png"
file_size = os.path.getsize(file_path)
file_name = os.path.splitext(os.path.basename(file_path))[0]

print("file_size:", file_size)

# 入力画像の読み込み
img = Image.open(file_path)

width, height = img.size

# 画像の幅を表示
print('width:', width)
# 画像の高さを表示
print('height:',height)

img_resize = img.resize((256, 256))
print(f'{width}x{height}へリサイズしました。')
img_resize.save(f'reSIZE_{file_name}.png')
