ages = [24, 30, 35, 40]
b = ages

# 操作1: 添加元素
ages.append(45)
print("添加元素后:")
print("  ages:", ages)
print("  b:   ", b)

# 操作2: 更新元素（通过索引赋值）
ages[0] = 25  # 把第一个元素24更新为25
print("\n更新元素后:")
print("  ages:", ages)
print("  b:   ", b)

# 操作3: 删除元素
ages.remove(40)
print("\n删除元素后:")
print("  ages:", ages)
print("  b:   ", b)

print("\n结论：b和ages指向同一个列表对象，")
print("对ages进行任何操作（添加/更新/删除/清空），b都会同步变化。")