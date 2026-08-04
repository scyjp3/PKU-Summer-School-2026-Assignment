# 五角星绘制程序
# 使用turtle库绘制一个红色的五角星

# 导入turtle绘图库
import turtle

# 获取用户输入的五角星大小（20~200）
size = int(input("Please input size(20~200):"))

# 创建一个turtle对象
t = turtle.Turtle()

# 设置画笔颜色为红色
t.color("red")

# 设置画笔粗细为5
t.pensize(5)

# 循环5次绘制五角星的5条边
for i in range(5):
    # 向前移动size距离
    t.forward(size)
    # 向右旋转144度（五角星的内角角度）
    t.right(144)

# 隐藏turtle光标
t.hideturtle()

# 保持图形窗口显示，等待用户关闭
turtle.done()
