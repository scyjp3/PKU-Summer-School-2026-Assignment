try:
    a = float(input("请输入第一个数："))
    b = float(input("请输入第二个数："))
    print(a / b)
except ZeroDivisionError:
    print("除数不能为0")
except ValueError:
    print("请输入数字")