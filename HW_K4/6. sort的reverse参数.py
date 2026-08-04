lst_1 = [2, 1, 3, 9, 5, 7, 6, 4, 8]
lst_2 = [2, 1, 3, 9, 5, 7, 6, 4, 8]

print("原列表:", lst_1)

lst_1.sort(reverse=True)
print(f'用sort(reverse=True)生成的列表：{lst_1}')

lst_2.reverse()
print(f'用reverse()生成的列表：{lst_2}')
print()
print(f'结论：sort(reverse=True)方法会先对列表进行排序，再将列表反转；而reverse()方法不会对列表进行排序，直接将列表反转。')