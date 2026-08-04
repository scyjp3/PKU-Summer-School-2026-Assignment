def get_valid_age():
    while True:
        try:
            age_str = input("请输入您的年龄：")
            
            # 处理空输入
            if age_str.strip() == "":
                print("输入不能为空，请重新输入！")
                continue
            
            # 尝试转换为整数
            age = int(age_str)
            
            # 检查年龄范围是否合理（0~150岁）
            if age < 0:
                print("年龄不能为负数，请重新输入！")
            elif age > 150:
                print(f"年龄 {age} 岁不太合理，请重新输入！")
            else:
                return age
                
        except ValueError:
            print("输入格式错误，请输入一个整数！")

def judge_age_stage(age):
    """根据年龄判断所处的年龄段"""
    if age <= 6:
        return "童年"
    elif age <= 17:
        return "少年"
    elif age <= 40:
        return "青年"
    elif age <= 65:
        return "中年"
    else:
        return "老年"

age = get_valid_age()

stage = judge_age_stage(age)

print(f"\n您输入的年龄是：{age} 岁")
print(f"对应的年龄段为：{stage}")