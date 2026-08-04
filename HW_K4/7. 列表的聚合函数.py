empty_list = []
print("len(empty_list):", len(empty_list))
print("sum(empty_list):", sum(empty_list))
try:
    print("min(empty_list):", min(empty_list))
except:
    print("min(empty_list): ValueError")
try:
    print("max(empty_list):", max(empty_list))
except:
    print("max(empty_list): ValueError")