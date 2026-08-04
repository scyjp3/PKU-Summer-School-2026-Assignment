lst = ['apple', 'banana', 'orange', 'grape']
targets = input("请输入要查找的元素（空格分隔）：").split()
for i in targets:
    if i in lst:
        idx = lst.index(i)
        print(f"  '{i}' 在列表中，索引为 {idx}")
    else:
        print(f"  '{i}' 不在列表中")