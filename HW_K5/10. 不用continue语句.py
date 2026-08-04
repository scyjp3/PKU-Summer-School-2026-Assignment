tips = []
for i in range(1, 100):
    if ("7" not in str(i)) and (i % 7 != 0):
        tips.append(i)
    else:
        tips.append("过!")

print(tips)