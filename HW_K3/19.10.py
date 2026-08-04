import math
n = int(input())
x = int(input())
y = int(input())
if y > n*x:
    print(0)
else:
    remaining = int(n - math.ceil(y/x))
    print(remaining)