def bill(items, discount=1.0):
    """
    结算账单函数
    参数:
        items: 点餐列表（字符串列表）
        discount: 折扣（1.0 为无折扣，0.85 为八五折），默认 1.0
    返回:
        折扣后的总金额
    """
    menu = {
        "小面": 10, "担担面": 12, "牛肉粉": 16, "米饭": 2,
        "毛血旺": 48, "酸菜鱼": 32, "口水鸡": 26, "烤鱼": 68,
        "小龙虾": 38, "水煮牛肉": 32, "泡椒牛蛙": 39, "辣子鸡": 32,
        "气泡水": 8, "椰奶": 6, "听可乐": 5, "扎啤": 20,
    }
    total = 0
    for item in items:
        if item in menu:
            total += menu[item]

    return total * discount

order = ["小面", "口水鸡", "烤鱼", "气泡水"]
original_total = bill(order)
discounted_total = bill(order, discount=0.85)

print("点餐:", order)
print("原价金额：{:.2f} 元".format(original_total))
print("折扣金额：{:.2f} 元".format(discounted_total))

print("\n=== 不同折扣对比 ===")
for d in [1.0, 0.95, 0.9, 0.85, 0.8]:
    print("  折扣 = {:.0%} → {:.2f} 元".format(d, bill(order, d)))