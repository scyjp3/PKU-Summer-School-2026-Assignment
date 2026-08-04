# -*- coding: utf-8 -*-
"""
第2题：艺术分形树
使用 turtle 递归绘制一棵带有随机变化、颜色渐变、粗细变化的艺术分形树。

功能说明：
1. 树枝粗细随递归深度变细（pensize 与 depth 成正比）。
2. 树枝颜色随长度变化：主干棕色 -> 中段橄榄绿 -> 树梢嫩绿 -> 末端花/果。
3. 倾斜角度在 15~45 度范围内随机变化，左右可不同。
4. 树枝长度在一定范围内随机变化（0.65~0.85 倍），使整棵树更逼真。
"""

import turtle
import random


def draw_tree(t, branch_len, depth):
    """
    递归绘制分形树
    :param t: turtle 画笔对象
    :param branch_len: 当前树枝长度
    :param depth: 递归深度（用于控制粗细、颜色和终止条件）
    """
    # 终止条件：树枝过短或深度耗尽，则在末端绘制"花/果"
    if branch_len < 10 or depth <= 0:
        choice = random.random()
        if choice < 0.5:
            t.pencolor("#FF69B4")  # 粉色花
            t.pensize(3)
        elif choice < 0.8:
            t.pencolor("#FF3333")  # 红色果
            t.pensize(4)
        else:
            t.pencolor("#FFD700")  # 金黄花朵
            t.pensize(3)
        t.forward(branch_len)
        t.backward(branch_len)
        return

    # 1) 粗细变化：树枝越深越细
    t.pensize(max(1, depth * 1.5))

    # 2) 颜色变化：根据长度过渡 棕褐 -> 橄榄绿 -> 嫩绿
    if branch_len > 60:
        t.pencolor("#8B4513")   # 树干：棕褐色
    elif branch_len > 30:
        t.pencolor("#6B8E23")   # 树枝：橄榄绿
    else:
        t.pencolor("#32CD32")   # 树梢：嫩绿色

    # 3) 长度随机变化：子枝为当前长度的 0.65~0.85 倍
    len_factor = random.uniform(0.65, 0.85)

    # 绘制当前树枝
    t.forward(branch_len)

    # 4) 角度随机变化：左右倾斜角度在 15~45 度间随机
    left_angle = random.randint(15, 45)
    right_angle = random.randint(15, 45)

    # 左侧树枝
    t.left(left_angle)
    draw_tree(t, branch_len * len_factor, depth - 1)

    # 右侧树枝：先回到原方向，再向右转
    t.right(left_angle)
    t.right(right_angle)
    draw_tree(t, branch_len * len_factor, depth - 1)

    # 复位到原方向（朝上）
    t.left(right_angle)

    # 有时加第三个中间小分支，使树更茂密（30% 概率）
    if random.random() < 0.3:
        mid_angle = random.randint(-15, 15)
        t.left(mid_angle)
        draw_tree(t, branch_len * len_factor * 0.7, depth - 1)
        t.right(mid_angle)

    # 回到当前树枝起点
    t.backward(branch_len)


def main():
    # 初始化画布
    screen = turtle.Screen()
    screen.setup(width=900, height=700)
    screen.bgcolor("#E0F7FA")   # 浅蓝色天空背景
    screen.title("艺术分形树")
    screen.colormode(255)

    # 初始化画笔
    t = turtle.Turtle()
    t.speed(0)            # 最快速度
    t.hideturtle()        # 隐藏画笔箭头
    t.penup()
    t.goto(0, -250)       # 从画布底部开始绘制
    t.setheading(90)      # 朝向上方
    t.pendown()

    # 设置随机种子（注释掉后每次运行效果不同）
    random.seed(42)

    # 开始递归绘制：初始长度 120，递归深度 9 层
    draw_tree(t, 120, 9)

    print("分形树绘制完成！点击画布关闭窗口。")
    screen.exitonclick()


if __name__ == "__main__":
    main()
