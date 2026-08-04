n = int(input())
count = 0
for i in range(1, n + 1):
    count += str(i).count("1")
print(count)