import jieba

sentence = "销售部长会开到了半夜"

print("1. 默认分词结果")
words = jieba.lcut(sentence)
print("  ".join(words))
print("  （不符合期望：'会开'黏在一起，'销售部长'被拆散）")

jieba.add_word("销售部长")
jieba.add_word("开到了")

print("\n2. 调整为方式一：销售部长 / 会 / 开到了 / 半夜")
words1 = jieba.lcut(sentence)
print("  ".join(words1))

jieba.del_word("销售部长")
jieba.add_word("部长会")

print("\n3. 调整为方式二：销售 / 部长会 / 开到了 / 半夜")
words2 = jieba.lcut(sentence)
print("  ".join(words2))
