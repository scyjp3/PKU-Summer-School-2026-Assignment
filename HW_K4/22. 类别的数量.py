from collections import Counter

cities = ['北京', '上海', '北京', '广州', '上海', '北京', '深圳', '广州', '杭州']

city_counter = Counter(cities)
print(f"生源城市统计: {city_counter}")

city_count = len(city_counter)
print(f"\n用 len() 得到类别数量: {city_count}")

print(f"\n结论: 用 len() 函数即可得到类别数量")