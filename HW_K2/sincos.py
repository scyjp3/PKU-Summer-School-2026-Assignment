# 正弦和余弦波形绘制程序
# 使用matplotlib库绘制sin(x)和0.6*cos(x)的波形图

# 导入matplotlib绘图库和numpy数值计算库
import matplotlib.pyplot as plt
import numpy as np

# 生成x轴数据：从-2π到2π，共100个点
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)

# 绘制sin(x)曲线，红色实线带圆圈标记，图例为"sin(x)"
plt.plot(x, np.sin(x), 'r-o', label="sin(x)")

# 绘制0.6*cos(x)曲线，蓝色虚线，图例为"0.6 * cos(x)"
plt.plot(x, 0.6 * np.cos(x), 'b--', label="0.6 * cos(x)")

# 显示图例
plt.legend()

# 设置x轴标签
plt.xlabel("Rads")

# 设置y轴标签
plt.ylabel("Amplitude")

# 设置图表标题
plt.title("Sin and Cos Waves")

# 显示图形
plt.show()
