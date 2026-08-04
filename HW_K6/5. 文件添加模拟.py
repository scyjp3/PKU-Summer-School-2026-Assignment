with open('lyric2.txt', 'w', encoding='utf-8') as f:
    f.write('昔人已乘黄鹤去，此地空余黄鹤楼。\n')
    f.write('黄鹤一去不复返，白云千载空悠悠。\n')

lines = [
    '晴川历历汉阳树，\n',
    '芳草萋萋鹦鹉洲。\n',
    '日暮乡关何处是？\n',
    '烟波江上使人愁。\n',
]
with open('lyric2.txt', 'at', encoding='utf-8') as f:
    f.writelines(lines)

with open('lyric2.txt', 'r', encoding='utf-8') as f:
    print(f.read())