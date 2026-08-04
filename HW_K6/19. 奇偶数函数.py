def parity(n, style="中文"):
    """
    判断整数 n 的奇偶性并打印结果
    选项参数 style：控制输出形式
        "中文" -> 打印"奇数"或"偶数"（默认）
        "英文" -> 打印"odd"或"even"
        "数学" -> 打印 n ≡ 1 (mod 2) 或 n ≡ 0 (mod 2)
    """
    if n % 2 == 0:
        if style == "中文":
            print("偶数")
        elif style == "英文":
            print("even")
        elif style == "数学":
            print("{} ≡ 0 (mod 2)".format(n))
    else:
        if style == "中文":
            print("奇数")
        elif style == "英文":
            print("odd")
        elif style == "数学":
            print("{} ≡ 1 (mod 2)".format(n))

print("=== 默认选项（中文）===")
parity(7)
parity(10)

print("\n=== 英文选项 ===")
parity(7, style="英文")
parity(10, style="英文")

print("\n=== 数学选项 ===")
parity(7, style="数学")
parity(10, style="数学")

print("\n=== 交互测试 ===")
num = int(input("请输入一个整数: "))
parity(num)
