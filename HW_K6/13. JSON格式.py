import json

song = {
    "标题": "春芽",
    "演唱者": "Wang",
    "作者": {
        "作词": "Pei",
        "作曲": "Pei",
        "编曲": "Pei"
    },
    "专辑": {
        "名称": "四季",
        "歌曲数量": 4,
        "歌曲列表": ["春芽", "热夏", "秋酿", "知寒"]
    },

    "歌词": [
        "春日里的嫩芽，悄悄破土而出",
        "带着希望与梦想，沐浴着阳光",
        "微风轻拂，万物苏醒",
        "这是新的开始，春的礼物"
    ]
}

print("=== JSON 格式（带缩进）===")
json_str = json.dumps(song, ensure_ascii=False, indent=2)
print(json_str)


with open('13. JSON格式.json', 'w', encoding='utf-8') as f:
    json.dump(song, f, ensure_ascii=False, indent=2)
print("\n已写入 13. JSON格式.json")


with open('13. JSON格式.json', 'r', encoding='utf-8') as f:
    loaded = json.load(f)
print("\n=== 从文件读回验证 ===")
print("标题:", loaded['标题'])
print("歌词共", len(loaded['歌词']), "行：")
for i, line in enumerate(loaded['歌词'], 1):
    print(f"  {i}. {line}")
