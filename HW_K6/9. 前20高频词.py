import re
import jieba
from collections import Counter

# 1. 读取并按作者分组解析全唐诗
authors = {}
current_author = ""

with open('全唐诗.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()

        m = re.match(r'卷\d+_\d+\s*【.*?】(\S+)', line)
        if m:
            current_author = m.group(1)
            authors.setdefault(current_author, "")
        elif line and current_author:
            authors[current_author] += line

print("全唐诗共收录 {} 位诗人的作品\n".format(len(authors)))

# 2. 选择4位著名诗人对比
poets = ["李白", "杜甫", "白居易", "王维"]

# 停用词：文言虚词及无意义高频单字
stopwords = set("之乎者也矣焉哉兮尔其于此乃则以而为若何所不无一有人"
                "山水风云月日花草春秋冬夏上下中前后外来去归知情见"
                "不得是已还亦皆即只因如欲能行坐立看闻道言心身名客游"
                "青白红尘明暗远高长短新旧死生老少轻重")
# 标点符号
puncts = set("，。、；：？！""''（）·…—《》【】\n\r\t ")

def top20(text):
    """对文本分词，返回前20高频词（过滤单字、标点、停用词）"""
    words = jieba.lcut(text)
    valid = [w for w in words
             if len(w) >= 2
             and re.search(r'[\u4e00-\u9fff]', w)
             and not all(c in stopwords for c in w)] 
    return Counter(valid).most_common(20)

# 3. 输出每位诗人的前20高频词
for poet in poets:
    if poet in authors:
        print("=" * 45)
        print("{} 的高频词（诗作 {} 字）".format(poet, len(authors[poet])))
        print("=" * 45)
        for i, (word, cnt) in enumerate(top20(authors[poet]), 1):
            print("  {:2d}. {:<6s}  {}次".format(i, word, cnt))
        print()
    else:
        print("未找到诗人 {} 的作品\n".format(poet))
