student_dict_int = {
    12: {"姓名": "刘桂花", "年龄": 18, "城市": "北京"},
    13: {"姓名": "孙柳", "年龄": 19, "城市": "重庆"},
    14: {"姓名": "康平", "年龄": 20, "城市": "广州"},
}

print("整数类型学号")
print(student_dict_int)
print(f"查询学号 13: {13 in student_dict_int}")

student_dict_str = {
    '12': {"姓名": "刘桂花", "年龄": 18, "城市": "北京"},
    '13': {"姓名": "孙柳", "年龄": 19, "城市": "重庆"},
    '14': {"姓名": "康平", "年龄": 20, "城市": "广州"},
}

print("\n字符串类型学号")
print(student_dict_str)
print(f"查询学号 '13': {'13' in student_dict_str}")

print("\n3: 访问学生信息")
print(f"整数版 student_dict_int[13] = {student_dict_int[13]['姓名']}")
print(f"字符串版 student_dict_str['13'] = {student_dict_str['13']['姓名']}")