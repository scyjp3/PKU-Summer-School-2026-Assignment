# 1. 创建方式相似
print("1. 创建方式相似:")
s = {1, 2, 3}           # 集合字面量
d = {'a': 1, 'b': 2}    # 字典字面量
print(f"  集合 s = {s}")
print(f"  字典 d = {d}")

# 2. 都支持 in 运算符（判断元素/键是否存在）
print("\n2. 都支持 in 运算符:")
print(f"  2 in s = {2 in s}")          # 集合：判断元素
print(f"  'a' in d = {'a' in d}")     # 字典：判断键

# 3. 都支持 len()
print("\n3. 都支持 len():")
print(f"  len(s) = {len(s)}")
print(f"  len(d) = {len(d)}")

# 4. 都是无序的
print("\n4. 都是无序的:")
s2 = {3, 1, 2}
d2 = {'b': 2, 'a': 1}
print(f"  {{3,1,2}} 创建后可能打印为: {s2}")
print(f"  {{'b':2,'a':1}} 创建后可能打印为: {d2}")

# 5. 都支持遍历
print("\n5. 都支持遍历:")
print("  遍历集合: ", end="")
for item in s:
    print(item, end=" ")
print()
print("  遍历字典: ", end="")
for key in d:
    print(key, end=" ")
print()

# 6. 都支持推导式
print("\n6. 都支持推导式:")
s_comp = {x*2 for x in range(5)}
d_comp = {x: x**2 for x in range(5)}
print(f"  集合推导式: {s_comp}")
print(f"  字典推导式: {d_comp}")