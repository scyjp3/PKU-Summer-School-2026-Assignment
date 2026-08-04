import re
import jieba
from collections import Counter

STOPWORDS = set("之乎者也矣焉哉兮尔其于此乃则以而为若何所不无一有人"
                "山水风云月日花草春秋冬夏上下中前后外来去归知情见"
                "不得是已还亦皆即只因如欲能行坐立看闻道言心身名客游"
                "青白红尘明暗远高长短新旧死生老少轻重")


#函数1：按作者解析全唐诗文件
def parse_poems_by_author(filename):
    """读取全唐诗文件，返回 {作者: 该作者全部诗作拼接文本}"""
    authors = {}
    current_author = ""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            m = re.match(r'卷\d+_\d+\s*【.*?】(\S+)', line)
            if m:
                current_author = m.group(1)
                authors.setdefault(current_author, "")
            elif line and current_author:
                authors[current_author] += line
    return authors


#函数2：统计某文本的前N高频词
def top_n_words(text, n=20):
    """对文本分词，返回前N高频词（过滤单字、标点、停用词）"""
    words = jieba.lcut(text)
    valid = [w for w in words
             if len(w) >= 2
             and re.search(r'[\u4e00-\u9fff]', w)
             and not all(c in STOPWORDS for c in w)]
    return Counter(valid).most_common(n)


#函数3：打印某诗人的高频词报告
def print_report(poet, text, n=20):
    """打印某位诗人的前N高频词报告"""
    print("=" * 45)
    print("{} 的高频词（诗作 {} 字）".format(poet, len(text)))
    print("=" * 45)
    for i, (word, cnt) in enumerate(top_n_words(text, n), 1):
        print("  {:2d}. {:<6s}  {}次".format(i, word, cnt))
    print()


#函数4：对比多位诗人的高频词
def compare_poets(authors, poets, n=20):
    """对比多位诗人的高频词"""
    for poet in poets:
        if poet in authors:
            print_report(poet, authors[poet], n)
        else:
            print("未找到诗人 {} 的作品\n".format(poet))


#函数5：找出某诗人独有的特色词
def unique_words(authors, poet, n=10):
    """找出某诗人高频词中、其他指定对比诗人都没用的特色词"""
    poets_to_compare = ["李白", "杜甫", "白居易", "王维"]
    poets_to_compare = [p for p in poets_to_compare if p != poet and p in authors]

    my_words = {w for w, _ in top_n_words(authors[poet], 30)}
    others_words = set()
    for p in poets_to_compare:
        others_words |= {w for w, _ in top_n_words(authors[p], 30)}

    unique = my_words - others_words
    print("{} 的特色词（其他对比诗人没用）：{}".format(poet, "、".join(sorted(unique)) or "无"))
    print()


#主程序：调用各函数完成分析
def main():
    # 1. 解析全唐诗
    authors = parse_poems_by_author('全唐诗.txt')
    print("全唐诗共收录 {} 位诗人的作品\n".format(len(authors)))

    # 2. 对比四位诗人
    poets = ["李白", "杜甫", "白居易", "王维"]
    compare_poets(authors, poets, n=20)

    # 3. 找出每位诗人的特色词
    print("=" * 45)
    print("各诗人特色词对比")
    print("=" * 45)
    for poet in poets:
        unique_words(authors, poet)


if __name__ == "__main__":
    main()
