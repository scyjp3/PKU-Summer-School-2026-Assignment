def bill_skewer(count, discount):
    total = 10 * count * discount
    return total

def bill_drink(count):
    total = 6.5 * count
    return total

discount = 0.85
skewer, drink = 6, 2

total = bill_skewer(skewer, discount) + bill_drink(drink)

print(f"您点了{skewer}串麻辣烫，{drink}瓶饮料。")
print(f"优惠后金额为{total:.2f}元。")