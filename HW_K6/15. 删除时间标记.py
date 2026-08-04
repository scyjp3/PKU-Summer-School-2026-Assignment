import urllib.request
import json
import re

# 歌词抓取API链接
lyric_url = "http://music.163.com/api/song/media"

song = input("请输入歌曲链接或ID: ")
# 从歌曲链接分离id字符串
id = song.split("=")[-1]

# 从网站请求歌词
f = urllib.request.urlopen(f"{lyric_url}?id={id}")
lyric_bytes = f.read()
f.close()

# 解析歌词
lyric_json = lyric_bytes.decode()
lyric = json.loads(lyric_json)

print(f"返回数据的关键字: {lyric.keys()}")


raw_lyric = lyric["lyric"]

clean_lyric = re.sub(r'\[\d{2}:\d{2}\.\d{2,3}\]', '', raw_lyric)

clean_lyric = '\n'.join([line.strip() for line in clean_lyric.splitlines() if line.strip()])

print("\n纯净歌词：")
print(clean_lyric)