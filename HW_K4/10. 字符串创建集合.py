str = "Hello World"
print("原字符串:", str)
char_set = set(str)
print(f"set(str) = {char_set}")
for i in char_set:
    num = str.count(i)
    print(f"{i} 在字符串中出现了 {num} 次")

print(f"结论：set()函数可以将字符串中出现的字符转换为集合并去重。")