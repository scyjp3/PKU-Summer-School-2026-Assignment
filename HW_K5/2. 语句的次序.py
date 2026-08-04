lst2 = [23, 45, 12, 35, 76, 10, 66, 75, 2]  # 必须最先
n2 = len(lst2)             # 可与 sort 互换（只依赖 lst2）
lst2.sort()                # 必须在取最值 / 中位数之前
lmed2 = lst2[n2 // 2]      # 三者顺序可任意调换
lmin2 = lst2[0]
lmax2 = lst2[-1]
print(f"median = {lmed2}")  # 三个 print 顺序可任意调换
print(f"min = {lmin2}")
print(f"max = {lmax2}")
print(lst2)

print("""总结：
    【不可调】lst 创建 → sort →（lmax / lmin / lmed）→ 对应的 print，其中 n = len(lst) 必须在 lmed 之前（lmed 用到 n）

    【可调】  n 与 sort 之间、lmax / lmin / lmed 三者之间、三个 print 之间、print(lst) 的位置 —— 均互不依赖，可自由""")