total = sum(1 / i for i in range(1, 101))
print(f"1~100的倒数之和：{total:.4f}")

str_list = ["abc", "hello", "world", "python", "hi", "programming"]

longest_str = max((len(s), s) for s in str_list)[1]
print(f"最长的字符串：{longest_str}，长度：{len(longest_str)}")