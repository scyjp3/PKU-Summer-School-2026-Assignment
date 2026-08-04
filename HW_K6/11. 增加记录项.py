import csv

colnames = ["品名", "数量", "价格"]
item = {}

# 打开文件，建议指定utf-8防止中文乱码
f = open("盘货记录_带价格.csv", "w", encoding="utf-8")
writer = csv.DictWriter(f, fieldnames=colnames)
writer.writeheader()

skewer = input("请输入品名：（直接回车退出程序）")
while skewer != "":
    count = input("请输入数量：")
    price = input("请输入单价：")

    item = {"品名": skewer, "数量": count, "价格": price}
    writer.writerow(item)
    print(f"----成功写入{item}")
    skewer = input("请输入品名：（直接回车退出程序）")

print("再见！")
f.close()