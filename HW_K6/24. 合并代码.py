import random

menu = {
    "主食": {"小面": 12, "担担面": 15, "牛肉粉": 18, "米饭": 2},
    "热菜": {
        "毛血旺": 38, "酸菜鱼": 45, "口水鸡": 32, "烤鱼": 58,
        "小龙虾": 68, "水煮牛肉": 48, "泡椒牛蛙": 52, "辣子鸡": 42
    },
    "饮料": {"气泡水": 8, "椰奶": 10, "听可乐": 5, "扎啤": 15}
}

price_all = {}
for category in menu.values():
    price_all.update(category)


def whatever(count=1):
    """随便套餐函数：随机生成订单，返回菜品列表"""

    hot_dishes = random.sample(list(menu["热菜"].keys()), count)
    staple = random.choice(list(menu["主食"].keys()))
    drink = random.choice(list(menu["饮料"].keys()))

    order = hot_dishes.copy()
    order.append(staple)
    order.append(drink)
    return order


def checkout(order):
    """结账函数：接收订单列表，打印明细并返回总金额"""
    total = 0
    print("===== 消费明细 =====")
    for dish in order:
        price = price_all[dish]
        print(f"{dish}\t{price} 元")
        total += price
    print("====================")
    print(f"应付总计：{total} 元\n")
    return total

print("随便套餐！")

# 小王点单（默认1道热菜）+ 结账
order_wang = whatever()
print("小王点了", order_wang)
checkout(order_wang)

# 小佩点单（2道热菜）+ 结账
order_pei = whatever(2)
print("小佩点了", order_pei)
checkout(order_pei)

# 小明点单（2道热菜）+ 结账
order_ming = whatever(2)
print("小明点了", order_ming)
checkout(order_ming)