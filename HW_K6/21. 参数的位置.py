def checkin(hotel, leader):
    print(f"在地图搜索{hotel}")
    print(f"打车前往{hotel}")
    print(f"由{leader}到前台办理入住手续")
    print("-" * 30)

# 正确示例：位置+关键字混合调用
print("【正确示例】")
checkin("星城酒店", leader="小王")

# 错误1：语法错误，关键字在前、位置在后
# checkin(hotel="星城酒店", "小王")

# 错误2：参数重复赋值
# checkin("星城酒店", hotel="蓉城酒店")

# 错误3：关键字参数名不存在
checkin("星城酒店", name="小王")