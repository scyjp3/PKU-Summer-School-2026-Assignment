age = int(input("请输入年龄："))
while age < 0:
    print("年龄不能为负数，请重新输入！")
    age = int(input("请输入年龄："))

if age <= 6:
    print("童年")
elif age <= 17:
    print("少年")
elif age <= 40:
    print("青年")
elif age <= 65:
    print("中年")
else:
    print("老年")