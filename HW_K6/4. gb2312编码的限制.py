char = '仌'
print("生僻字：{}（读音和本义同'冰'）".format(char))

# 尝试用 gb2312 编码
try:
    encoded = char.encode('gb2312')
    print("gb2312 编码成功：", encoded)
except UnicodeEncodeError as e:
    print("gb2312 编码失败：", e)