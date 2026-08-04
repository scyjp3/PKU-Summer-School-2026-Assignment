n = int(input())
if 1<=n<=40:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end="")
        print()
else:
    print("输入有误：n必须在1到40之间")