student = {}

def add_or_update(dictionary, key, value):
    # 添加前判断key是否存在
    if key in dictionary:
        print(f"更新已有条目：{key} -> {value}")
    else:
        print(f"新建条目：{key} -> {value}")
    
    # 添加或更新
    dictionary[key] = value


# 第一次添加
add_or_update(student, "Tom", 18)

# 第二次添加相同键
add_or_update(student, "Tom", 20)

# 添加新的键
add_or_update(student, "Jack", 22)


print("\n最终字典内容：")
print(student)

print(f'结论：Python 字典在使用赋值语句添加条目时，根据键是否已经存在，会分别执行新增条目或更新条目的操作。不存在则新增，存在则更新。')