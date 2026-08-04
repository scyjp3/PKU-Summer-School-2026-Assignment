vip_input = input("请输入会员号（VIP会员请输入VIP，普通会员请输入普通）：")
is_vip = vip_input == "VIP"
normal_member = vip_input == "普通"
product = input("请输入商品名称：")
if is_vip:
    print(True)
elif normal_member and product == "串点":
    print(True)
else:
    print(False)