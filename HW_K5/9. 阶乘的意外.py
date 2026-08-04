n = 1
fact = 1

while fact <= 100000000:
    n += 1
    fact *= n

print(f"{n} 的阶乘 {n}! = {fact}，刚好超过1亿")
