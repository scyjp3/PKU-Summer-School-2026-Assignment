left, middle, right = "N", "G", "R"

# 左转规则（原题原有）
if (left == "G") or (left == "N" and middle == "G"):
    left_state = "左转通行"
else:
    left_state = "左转停止"

# 直行规则
if (middle == "G") or (middle == "N" and (left == "G" or right == "G")):
    mid_state = "直行通行"
else:
    mid_state = "直行停止"

# 右转规则
if right == "G" or right == "N":
    right_state = "右转通行"
else:
    right_state = "右转停止"

# 输出结果
print(left_state)
print(mid_state)
print(right_state)