import math
import turtle


def q1():
    count = 80
    price = 0.8
    print(f"串点数量: {count}, 类型: {type(count)}")
    print(f"进货价格: {price}, 类型: {type(price)}")


def q2():
    print("便利店商品数据分析：")
    print("| 序号 | 数据项 | 类型 | 数据值 |")
    print("| --- | --- | --- | --- |")
    print("| 1 | 商品名称 | str | 浓香原味奶茶 |")
    print("| 2 | 产地 | str | 中国 |")
    print("| 3 | 单位 | str | 瓶 |")
    print("| 4 | 原价 | float | 10.50 |")
    print("| 5 | 促销价 | float | 5.25 |")
    print("| 6 | 库存数量 | int | 50 |")
    print("| 7 | 是否促销 | bool | True |")


def q3():
    a = 3.5
    b = 3.5
    print(f"a = {a}, id(a) = {id(a)}")
    print(f"b = {b}, id(b) = {id(b)}")
    print(f"a == b: {a == b}")
    print(f"a is b: {a is b}")


def q4_swap():
    x = 10
    y = 20
    print(f"交换前: x = {x}, y = {y}")
    temp = x
    x = y
    y = temp
    print(f"交换后: x = {x}, y = {y}")


def q4_welcome(name="李清照"):
    surname = name[0]
    print(f"请输入您的姓名：{name}")
    print(f"小{surname}你好！欢迎来到便利店！")


def q5_chord():
    chord = "C" * 6 + "G" + "C" + "G" + "C"
    print(f"两只老虎和弦: {chord}")


def q6_milk_tea():
    label = "品名：浓香原味奶茶；产地：中国；单位：瓶；原价：10.50元；促销价：5.25元"
    name_start = label.find("品名：") + 3
    name_end = label.find("；", name_start)
    name = label[name_start:name_end]
    price_start = label.find("促销价：") + 4
    price_end = label.find("元", price_start)
    price = label[price_start:price_end]
    print(f"品名：{name}")
    print(f"促销价：{price}元")


def q7_poetry():
    poem = "鸟宿池边树，僧推月下门"
    new_poem = poem.replace("推", "敲")
    print(f"原句：{poem}")
    print(f"修改后：{new_poem}")


def q8_vip():
    beef_price = 5.0
    water_price = 2.0
    total = beef_price + water_price
    discount = 0.9
    balance = 5.3
    final_payment = max(total * discount - balance, 0)
    print(f"牛肉串价格: {beef_price}元")
    print(f"矿泉水价格: {water_price}元")
    print(f"原价总计: {total}元")
    print(f"VIP九折后: {total * discount}元")
    print(f"会员卡余额: {balance}元")
    print(f"最终支付: {final_payment}元")


def q9_digits():
    def get_digits(n):
        return math.floor(math.log10(n)) + 1
    print(f"2035 的位数: {get_digits(2035)}")
    print(f"32768 的位数: {get_digits(32768)}")


def q10_price():
    def calculate_price(cost):
        price = cost * 1.2
        price_rounded = round(price * 10) / 10
        final_price = min(price_rounded, 3.5)
        return final_price
    print(f"牛肉串进价3.0元，售价: {calculate_price(3.0)}元")
    print(f"进价2.8元，售价: {calculate_price(2.8)}元")


def q11_discount(amount=23.7):
    print(f"请输入打折前的金额：{amount}")
    discounted = round(amount * 0.9 * 10) / 10
    print(f"VIP九折后（四舍五入到角）: {discounted}")


def q12_float_format():
    num = 3.14159
    print(f"原始值: {num}")
    print(f"保留1位小数: {num:.1f}")
    print(f"保留2位小数: {num:.2f}")
    print(f"保留3位小数: {num:.3f}")
    print("结论：格式化字符串中浮点数指定的小数位数不足时，会进行四舍五入")


def q13_1_triangle():
    t = turtle.Turtle()
    t.color("blue")
    for _ in range(3):
        t.forward(100)
        t.left(120)
    turtle.done()


def q13_2_heart():
    t = turtle.Turtle()
    t.color("red")
    t.begin_fill()
    t.left(50)
    t.forward(133)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(133)
    t.end_fill()
    turtle.done()


def q13_3_crystal():
    t = turtle.Turtle()
    t.color("green")
    for _ in range(6):
        t.forward(80)
        t.backward(80)
        t.right(60)
    turtle.done()


def q13_4_inkstone():
    t = turtle.Turtle()
    t.color("black")
    t.begin_fill()
    t.forward(100)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(80)
    t.end_fill()
    t.penup()
    t.goto(20, -20)
    t.pendown()
    t.color("gray")
    t.begin_fill()
    t.forward(60)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(40)
    t.end_fill()
    turtle.done()


def q13_5_taiji():
    t = turtle.Turtle()
    t.speed(2)
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.begin_fill()
    t.circle(100, 180)
    t.end_fill()
    t.begin_fill()
    t.circle(50, 180)
    t.end_fill()
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.begin_fill()
    t.circle(50, 180)
    t.end_fill()
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.begin_fill()
    t.circle(-25, 180)
    t.end_fill()
    t.penup()
    t.goto(0, -25)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.penup()
    t.goto(0, 75)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    turtle.done()


def q14_warning_sign(n=100):
    t = turtle.Turtle()
    t.color("red")
    t.begin_fill()
    for _ in range(3):
        t.forward(n)
        t.left(120)
    t.end_fill()
    t.penup()
    t.goto(n/2, n/3)
    t.pendown()
    t.color("white")
    t.dot(n/4)
    turtle.done()


def q15_binary_examples():
    print("两种状态的事情举例：")
    print("1. 便利店门：开/关")
    print("2. 商品库存：有货/缺货")
    print("3. 灯：亮/灭")
    print("4. 会员状态：VIP/普通")
    print("5. 天气：晴天/阴天")
    print("6. 电源：接通/断开")


def q16_discount_check(member_id="VIP123", product="牛肉串"):
    print(f"请输入会员号：{member_id}")
    print(f"请输入商品名称：{product}")
    is_vip = member_id.startswith("VIP")
    is_chuan = "串" in product
    discount = is_vip or is_chuan
    print(f"享受九折优惠: {discount}")


def q17_weekend_discount(member_id="VIP123", product="奶茶"):
    print(f"请输入会员号：{member_id}")
    print(f"请输入商品名称：{product}")
    is_vip = member_id.startswith("VIP")
    is_milk_or_chuan = any(item in product for item in ["奶茶", "串"])
    discount = 0.8 if is_vip or is_milk_or_chuan else 0.9
    print(f"折扣: {discount}")


def q18_1_a_plus_b():
    a, b = map(int, input().split())
    print(a + b)


def q18_2_reverse_3digit():
    n = input().strip()
    print(n[::-1])


def q18_3_circle():
    r = float(input())
    pi = 3.14159
    circumference = 2 * pi * r
    area = pi * r * r
    print(f"{circumference:.2f} {area:.2f}")


def q18_4_sphere_volume():
    r = float(input())
    volume = (4 / 3) * 3.14159 * r ** 3
    print(f"{volume:.2f}")


def q18_5_resistance():
    r1, r2 = map(float, input().split())
    r = r1 * r2 / (r1 + r2)
    print(f"{r:.2f}")


def q18_6_arithmetic_sequence():
    a1, d, n = map(int, input().split())
    an = a1 + (n - 1) * d
    print(an)


def q18_7_fraction_float():
    a, b = map(int, input().split())
    print(a / b)


def q18_8_average():
    nums = list(map(int, input().split()))
    avg = sum(nums) / len(nums)
    print(f"{avg:.2f}")


def q18_9_quotient_remainder():
    a, b = map(int, input().split())
    print(a // b, a % b)


def q18_10_apples_worms():
    x, y, z = map(int, input().split())
    hours = z // y
    remaining = max(x - hours, 0)
    print(remaining)


def q18_11_height_on_hypotenuse():
    a, b = map(float, input().split())
    c = math.sqrt(a ** 2 + b ** 2)
    h = (a * b) / c
    print(f"{h:.2f}")


if __name__ == "__main__":
    print("=" * 50)
    print("题目1：商品信息的数据分析")
    print("=" * 50)
    q1()

    print("\n" + "=" * 50)
    print("题目2：便利店里的数据分析")
    print("=" * 50)
    q2()

    print("\n" + "=" * 50)
    print("题目3：不同的数据对象")
    print("=" * 50)
    q3()

    print("\n" + "=" * 50)
    print("题目4-1：变量值交换")
    print("=" * 50)
    q4_swap()

    print("\n" + "=" * 50)
    print("题目4-2：便利店欢迎程序")
    print("=" * 50)
    q4_welcome()

    print("\n" + "=" * 50)
    print("题目5：拼接和弦")
    print("=" * 50)
    q5_chord()

    print("\n" + "=" * 50)
    print("题目6：奶茶标签")
    print("=" * 50)
    q6_milk_tea()

    print("\n" + "=" * 50)
    print("题目7：推敲")
    print("=" * 50)
    q7_poetry()

    print("\n" + "=" * 50)
    print("题目8：VIP会员")
    print("=" * 50)
    q8_vip()

    print("\n" + "=" * 50)
    print("题目9：正整数的位数")
    print("=" * 50)
    q9_digits()

    print("\n" + "=" * 50)
    print("题目10：串点售价")
    print("=" * 50)
    q10_price()

    print("\n" + "=" * 50)
    print("题目11：自动计算折扣")
    print("=" * 50)
    q11_discount()

    print("\n" + "=" * 50)
    print("题目12：浮点数位数")
    print("=" * 50)
    q12_float_format()

    print("\n" + "=" * 50)
    print("题目15：两种状态的事情")
    print("=" * 50)
    q15_binary_examples()

    print("\n" + "=" * 50)
    print("题目16：优惠活动")
    print("=" * 50)
    q16_discount_check()

    print("\n" + "=" * 50)
    print("题目17：周末折扣")
    print("=" * 50)
    q17_weekend_discount()
