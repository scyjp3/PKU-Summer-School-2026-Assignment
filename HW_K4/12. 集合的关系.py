A = {'a', 'b'}
B = {'a', 'b', 'c', 'd'}
print(f"A = {A}")
print(f"B = {B}")

subset = A.issubset(B)
print(f"A 是否是 B 的子集: {subset}")

subset_2 = A in B
print(f"A in B = {subset_2}")

if subset_2 == True:
    print("A 是 B 的一个【子集】")
else:
    print("'A in B' 不能表示 A 是否是 B 的【子集】")
    A_2 = 'a'
    print(f"A_2 = {A_2}")
    print(f"A_2 in B = {A_2 in B}")
    print("'A in B' 可以表示 A 是否是 B 的一个【元素】")