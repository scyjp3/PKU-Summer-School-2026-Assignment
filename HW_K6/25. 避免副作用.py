def my_order2(order):
    """有副作用的函数：直接在传入的列表上操作"""
    order.append("加蛋")
    order[0] = "辣子鸡"
    return sum({"小面": 10, "辣子鸡": 32, "加蛋": 2}.get(i, 0) for i in order)


print("=== 1. 有副作用：直接传 order ===")
order = ["小面", "口水鸡"]
print("调用前 order:", order)
total = my_order2(order)
print("调用后 order:", order) 
print("账单金额:", total)

print("\n=== 2. 无副作用：传 order[:] 切片拷贝 ===")
order = ["小面", "口水鸡"]
print("调用前 order:", order)
total = my_order2(order[:])
print("调用后 order:", order)
print("账单金额:", total)

print("\n=== 3. 原理：order 与 order[:] 是两个不同的列表对象 ===")
order = ["小面", "口水鸡"]
copy = order[:]
print("order:", id(order), order)
print("copy : ", id(copy), copy)
print("order is copy ?", order is copy)