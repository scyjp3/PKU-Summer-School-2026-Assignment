# 三角形图案绘制程序（改进版）
# 添加了输入验证，确保用户输入的数值在3~20范围内
# 获取用户输入的三角形大小
n = int(input("Please input size(3~20):"))
# 输入验证循环：当输入值不在3~20范围内时，提示用户重新输入
while n < 3 or n > 20:
    print(f"{n} is not in range! Please input a number between 3 and 20.")
    n = int(input("Please input size(3~20):"))
# 外层循环控制三角形的行数，共n行
for i in range(n):
# 每行由两部分组成：前导空格 + @符号
# 空格数量：n - i - 1（逐行递减）
# @符号数量：i * 2 + 1（逐行递增，保证等腰）
    line = " " * (n - i - 1) + "@" * (i * 2 + 1)
# 打印当前行
    print(line)