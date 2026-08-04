a = int(input())
b = int(input())
prime_count = 0
for i in range(a, b+1):
    if i <= 1:
        continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        prime_count += 1
print(prime_count)