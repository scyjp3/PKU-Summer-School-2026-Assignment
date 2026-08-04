fname = input("请输入歌词文件名: ")
try:
    f = open(fname, "xt", encoding='utf-8')
except FileExistsError:
    f = open(fname, "rt", encoding='utf-8')
    lyric = f.read()
    print(lyric)
    f.close()
    print("歌词文件已经存在，可继续添加歌词！")
    f = open(fname, "at", encoding='utf-8')

# 输入歌词，以空行结束
print("下面请继续输入歌词，每行回车，直接回车结束输入")
line = input("歌词: ")
while line != "":
    f.write(line + "\n")
    line = input("歌词: ")
f.close()
print("歌词已经记录到文件中，再见！")

#新新增功能：查看、删除、更新一行歌词
print("\n歌词管理新功能")
print("当前歌词内容：")
with open(fname, 'rt', encoding='utf-8') as f:
    lines = f.readlines()  # 读成列表，每行带换行符
for i, l in enumerate(lines, 1):
    print("  [{}] {}".format(i, l.rstrip('\n')))

# 提供操作菜单
while True:
    print("\n请选择操作：")
    print("  1. 查看歌词")
    print("  2. 删除一行")
    print("  3. 更新一行")
    print("  4. 退出")
    choice = input("请输入选项 (1/2/3/4): ").strip()
    if choice:                      # 输入非空时，只取第一个字符来匹配
        choice = choice[0]          # 这样输入 "4"、"4."、"4. 退出" 都能识别为 "4"

    if choice == '1':
        print("\n当前歌词：")
        for i, l in enumerate(lines, 1):
            print("  [{}] {}".format(i, l.rstrip('\n')))

    elif choice == '2':
        try:
            idx = int(input("请输入要删除的行号: "))
            if 1 <= idx <= len(lines):
                removed = lines.pop(idx - 1)
                print("已删除第{}行：{}".format(idx, removed.rstrip('\n')))
                # 同步写回文件
                with open(fname, 'wt', encoding='utf-8') as f:
                    f.writelines(lines)
            else:
                print("行号超出范围！")
        except ValueError:
            print("请输入有效数字！")

    elif choice == '3':
        try:
            idx = int(input("请输入要更新的行号: "))
            if 1 <= idx <= len(lines):
                new_line = input("请输入新的歌词内容: ")
                lines[idx - 1] = new_line + '\n'
                print("已更新第{}行".format(idx))
                with open(fname, 'wt', encoding='utf-8') as f:
                    f.writelines(lines)
            else:
                print("行号超出范围！")
        except ValueError:
            print("请输入有效数字！")

    elif choice == '4':
        print("退出管理，再见！")
        break
    else:
        print("无效选项，请重试。")
