import json

song_info = {
    "标题": "春芽",
    "演唱者": "Wang",
    "作者": {"作词": "Pei", "作曲": "Pei", "编曲": "Pei"},
    "专辑": {"名称": "四季", "歌曲数量": 4, "歌曲列表": ["春芽", "热夏", "秋酿", "知寒"]},
    "歌词": "春风吹绿枝桠，新芽慢慢长大，走过四季变化，歌声伴着年华"
}

print(f"歌曲信息对象的类型: {type(song_info)}")

song_json = json.dumps(song_info, ensure_ascii=False)
print(song_json)