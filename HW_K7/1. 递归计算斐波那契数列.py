import time

def fib(n):

    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

for n in range(37, 41):
    start = time.perf_counter()
    result = fib(n)
    end = time.perf_counter()
    print(f"第{n}项结果：{result}，耗时：{end - start:.4f} 秒")