# 二次函数计算器
# 计算二次函数 y = ax² + bx + c 的值，其中a=2, b=-45, c=13

# 获取用户输入的x值
x = float(input("Please input a number: "))

# 定义二次函数的系数
a = 2      # x²项的系数
b = -45    # x项的系数
c = 13     # 常数项

# 计算二次函数的值
y = a * x**2 + b * x + c

# 输出结果
print("x = ", x)
print("y = ", y)