n = int(input("请输入一个正整数n："))
total = 0
tips = []
for i in range(1, n + 1):
    if i % 7 != 0 and '7' not in str(i):
        total += i
    else:
        tips.append(i)

# 把游戏小抄写入数据文件 skip7tips.dat
with open('skip7tips.dat', 'w', encoding='utf-8') as f:
    for num in tips:
        f.write(str(num) + '\n')

print("1~{}中未被跳过数字的累加和为：{}".format(n, total))
print("已将 {} 个需要跳过的数字写入 skip7tips.dat".format(len(tips)))


# 读取并打印小抄内容
with open('skip7tips.dat', 'r', encoding='utf-8') as f:
    tip_list = f.read().split()
print(" ".join(tip_list))