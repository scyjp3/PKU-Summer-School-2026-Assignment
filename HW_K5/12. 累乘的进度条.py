import time
from tqdm import tqdm

n = 20              # 累乘到 20
product = 1         # 累乘结果，初始为 1

# 用 tqdm 包装可迭代对象，即可在循环时显示进度条
for i in tqdm(range(1, n + 1), desc="累乘进度"):
    product *= i
    time.sleep(0.2)   # 模拟耗时，方便观察进度条变化

print(f"\n{n}! = {product}")