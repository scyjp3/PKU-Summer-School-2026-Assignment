# 情景：2个班级，每个班级3个学生，每个学生3门课的成绩
scores = [
    [   # 第1个班级
        [85, 90, 78],   # 学生1的3门课成绩
        [76, 88, 95],   # 学生2的3门课成绩
        [90, 85, 82],   # 学生3的3门课成绩
    ],
    [   # 第2个班级
        [70, 75, 80],   # 学生1的3门课成绩
        [92, 88, 76],   # 学生2的3门课成绩
        [85, 90, 95],   # 学生3的3门课成绩
    ],
]

print(f"scores = {scores}")

# 维度信息
print(f"\n维度信息:")
print(f"  层数（班级数）: {len(scores)}")
print(f"  行数（每班学生数）: {len(scores[0])}")
print(f"  列数（每生课程数）: {len(scores[0][0])}")

# 访问元素：scores[层][行][列]
print(f"\n访问元素 scores[层][行][列]:")
print(f"  scores[0][0][0] = {scores[0][0][0]}  (第1班/学生1/第1门课)")
print(f"  scores[0][1][2] = {scores[0][1][2]}  (第1班/学生2/第3门课)")

# 遍历三维数组
print("\n遍历三维数组:")
for i, classroom in enumerate(scores):
    print(f"  第{i+1}个班级:")
    for j, student in enumerate(classroom):
        print(f"    学生{j+1}的成绩: {student}")
