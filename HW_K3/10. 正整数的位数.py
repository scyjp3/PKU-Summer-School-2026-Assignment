x = int(input("请输入一个正整数："))
import math
print(f"{x}的位数为：{math.floor(math.log10(x)) + 1}")