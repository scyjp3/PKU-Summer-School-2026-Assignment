beef_price = 5.0
water_price = 2.0
total = beef_price + water_price
is_vip = True
balance = 5.3

if is_vip:
    pay = total * 0.9
else:
    pay = total

final_pay = pay - balance
print(f"牛肉串：{beef_price}元")
print(f"矿泉水：{water_price}元")
print(f"原价合计：{total}元")
print(f"VIP九折后：{pay}元")
print(f"扣除会员卡余额{balance}元")
print(f"最终支付：{final_pay}元")
