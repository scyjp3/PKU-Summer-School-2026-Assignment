# 随机酒吧模拟程序
# 随机选择饮料并计算消费金额和捐赠金额

# 导入随机模块
import random

# 初始化随机数生成器
random.seed()

# 定义饮料菜单列表
menu = ['cola','milk', 'tea', 'coffee','water','juice']

# 打印欢迎界面
print("~=" * 12)
print("Welcome to Random Bar!")
print("~=" * 12)

# 获取顾客姓名
guest = input("Please input your name: ")

# 随机选择一杯饮料
drink = random.choice(menu)

# 打印点单结果
print("-*-" * 10)
print(f"Hello, {guest}! Enjoy your {drink}.")

# 随机生成消费金额（0~5美元）
cost = random.randrange(6)

# 计算捐赠金额：消费金额的3% + 0.01美元
donation = cost * 0.03 + 0.01

# 根据消费金额输出不同提示
if cost == 0:
    print("It's free!")
else:
    print(f"${cost} please.")

# 输出捐赠金额（保留两位小数）
print(f"We'll donate ${donation:.2f} to the charity.")
