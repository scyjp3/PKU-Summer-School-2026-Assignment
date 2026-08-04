x = float(input("请输入价："))
vip_input = input("是否为VIP会员（是/否）：")
is_vip = vip_input == "是"
if is_vip:
    pay = x * 0.9
else:
    pay = x
print(f"折扣后的价：{round(pay, 1)}元")