vip_input = input("请输入会员号（VIP会员请输入VIP，普通会员请输入普通）：")
product = input("请输入商品名称：")
is_vip = vip_input == "VIP"
discount = 0.8 if is_vip or any(item in product for item in ["奶茶", "串点"]) else 0.9
print(f"折扣为：{discount}")