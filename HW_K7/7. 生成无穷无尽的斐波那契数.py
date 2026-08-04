def fibonacci():
    """无穷斐波那契数列生成器"""
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()

print("前15项斐波那契数：")
for _ in range(15):
    print(next(fib_gen), end=" ")