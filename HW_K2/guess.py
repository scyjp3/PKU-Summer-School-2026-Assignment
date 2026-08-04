# 猜数字游戏
# 程序随机生成一个1~100之间的数字，玩家有6次机会猜测

# 导入随机模块
import random

# 生成1~100之间的随机整数作为秘密数字
secret = random.randint(1, 100)

# 打印游戏规则说明
print(
    """Guess the number! 
    I think of a number between 1 and 100. You have 6 chances to guess it right.
    """
)

# 初始化猜测次数
tries = 1

# 循环进行最多6次猜测
while tries <= 6:
    # 获取用户输入的猜测值
    guess = int(input("Please input your guess: "))
    
    # 判断猜测结果
    if guess == secret:
        # 猜对了，输出成功信息并退出循环
        print("You guessed it right!")
        break
    elif guess < secret:
        # 猜小了，提示用户
        print("Your guess is too low.")
    else:
        # 猜大了，提示用户
        print("Your guess is too high.")
    
    # 猜测次数加1
    tries += 1
else:
    # 6次机会用完仍未猜对，输出失败信息
    print("Sorry, you didn't guess it right.")
