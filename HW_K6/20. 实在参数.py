def checkin(name, room):
    """登记入住信息"""
    print("  {} 入住 {} 房间".format(name, room))

print("1. 字面值作为实参")
checkin("张三", 101)
checkin("李四", 202)

print("\n2. 表达式作为实参")
checkin("王" + "五", 100 + 3)
checkin("赵六" * 1, 300 // 2)
checkin("钱" + "七七", 4 * 50 + 1)

print("\n3. 变量作为实参")
guest = "孙八"
room_no = 405
checkin(guest, room_no)

print("\n4. 混合使用各种实参")
prefix = "客人"
num = 5
checkin(prefix + "周九", num * 100 + 6) 
checkin("吴十", room_no + 1)