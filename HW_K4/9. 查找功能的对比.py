text = "Hello World"
print("字符串查找:")
print(f"text.find('W')   = {text.find('W')}")
print(f"text.find('World') = {text.find('World')}")  
# find()找不到时返回-1
result = text.find('Python')
if result == -1:
    print(f"’Python’不在字符串中。")
else:
    print(f"text.find('Python') = {result}")