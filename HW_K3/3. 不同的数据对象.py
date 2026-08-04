x = 3.5
y = float('3.5')
print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")
print(f"x == y: {x == y}")
print(f"x is y: {x is y}")
print()
print("结论：即便是值相等的数据（3.5 == 3.5），也可能是不同的对象（id不同）")
