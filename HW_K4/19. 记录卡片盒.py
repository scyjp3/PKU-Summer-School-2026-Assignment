students_dict = [
    {'name': 'Tom', 'age': 18, 'city': '北京'},
    {'name': 'Jack', 'age': 20, 'city': '上海'},
    {'name': 'Lucy', 'age': 19, 'city': '广州'},
]

students_list = [
    ['Tom',  18, '北京'],   # 第1张卡片
    ['Jack', 20, '上海'],   # 第2张卡片
    ['Lucy', 19, '广州'],   # 第3张卡片
]

print("字典列表")
print(students_dict)

print("\n嵌套列表")
print(students_list)

print("\n按索引抽取整张卡片:")
print(f"第2张卡片（dict）: {students_dict[1]}")
print(f"第2张卡片（list）: {students_list[1]}")

print("\n访问卡片中的数据项:")
print(f"第2张卡片的姓名（dict）: {students_dict[1]['name']}")
print(f"第2张卡片的姓名（list）: {students_list[1][0]}")

# 3. 遍历所有卡片
print("\n遍历所有卡片:")
print("dict:")
for card in students_dict:
    print(f"姓名:{card['name']}, 年龄:{card['age']}, 城市:{card['city']}")

print("list:")
for card in students_list:
    print(f"姓名:{card[0]}, 年龄:{card[1]}, 城市:{card[2]}")