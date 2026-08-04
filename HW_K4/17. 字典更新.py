original = {'Tom': 18, 'Jack': 20}
print(f"更新前字典: {original}")
print(f"更新前长度: {len(original)}")

new_data = {'Jack': 21, 'Lucy': 19, 'Lily': 22}
print(f"\n要更新的数据: {new_data}")
print(f"要更新的条目数: {len(new_data)}")

before_len = len(original)
original.update(new_data)
after_len = len(original)

added = after_len - before_len
updated = len(new_data) - added

print(f"\n更新后字典: {original}")
print(f"更新后长度: {after_len}")
print(f"\n新增条目数: {added}")
print(f"更新已有条目数: {updated}")