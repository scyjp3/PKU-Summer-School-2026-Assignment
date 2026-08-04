with open("盘货记录.csv", "w", encoding="utf-8") as f:

    f.write("商品编号,商品名称,库存数量,单价(元)\n")

    f.write("SP001,笔记本,128,5.5\n")
    f.write("SP002,中性笔,350,2.0\n")
    f.write("SP003,文件夹,76,8.8\n")
    f.write("SP004,订书机,22,15.0\n")

print("盘货记录.csv 文件已创建并写入完成")