n = int(input())
total = 0
for i in range(1, n + 1):
    if i % 7 != 0 and '7' not in str(i):
        total += i
print(total)