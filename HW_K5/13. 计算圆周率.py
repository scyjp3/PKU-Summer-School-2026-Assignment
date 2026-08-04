from random import random
from tqdm import tqdm

N = 10_000_000  # 1000万个随机点，下划线是数字分隔符，不影响数值
c = 0

pbar = tqdm(range(1, N + 1))
for i in pbar:
    x, y = random(), random()
    # 直接比较平方，省去开根号，等价于距离<1
    if x * x + y * y < 1:
        c += 1
    
    # 每1000个点计算一次pi并更新描述
    if i % 1000 == 0:
        pi = (c / i) * 4.0
        pbar.set_description(f"pi: {pi:.8f}")

# 输出最终结果
final_pi = c / N * 4.0
print(f"最终计算的圆周率 pi = {final_pi:.8f}")