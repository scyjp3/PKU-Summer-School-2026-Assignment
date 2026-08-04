x = float(input("进价："))
price = x * 1.2
if price > 3.5:
    price = 3.5
print(f"售价：{round(price, 1)}元")
