lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]

lst_add_1 = lst_1 + lst_2
lst_add_2 = lst_2 + lst_1
print("列表加法运算:")
print(f"  lst_1 + lst_2 = {lst_add_1}")
print(f"  lst_2 + lst_1 = {lst_add_2}")
if lst_add_1 == lst_add_2:
    print("列表加法运算的交换律成立")
else:
    print("列表加法运算的交换律不成立")

print()

n = 3
lst_mul_1 = lst_1 * n
lst_mul_2 = n * lst_1
print("列表乘法运算:")
print(f"  lst_1 * {n} = {lst_mul_1}")
print(f"  {n} * lst_1 = {lst_mul_2}")
if lst_mul_1 == lst_mul_2:
    print("列表乘法运算的交换律成立")
else:
    print("列表乘法运算的交换律不成立")