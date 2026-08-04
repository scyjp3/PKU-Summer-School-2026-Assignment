n = int(input())
fact = 1
if 1<=n<=20:
    for i in range(1,n+1):
        fact *= i
    print(fact)
else:
    print("输入有误：n必须在1到20之间")