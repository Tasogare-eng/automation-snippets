try:
    x = int(input("数字を入力: "))
    print(10 / x)
except ValueError:
    print("数値を入力してください。")
except ZeroDivisionError:
    print("0では割れません。")
finally:
    print("処理終了。")
