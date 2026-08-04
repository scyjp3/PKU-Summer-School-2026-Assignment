pythagorean = [(i, j, k)
              for i in range(1, 101)
              for j in range(i + 1, 101)
              for k in range(j + 1, 101)
              if i * i + j * j == k * k]

print("100以内所有勾股数共 %d 组：" % len(pythagorean))
for triple in pythagorean:
    i, j, k = triple
    print("(%d, %d, %d)  验证: %d² + %d² = %d² + %d² = %d" % (i, j, k, i, j, i*i, j*j, k*k))