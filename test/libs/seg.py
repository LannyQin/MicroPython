from machine import Pin


# 创建共阴型数码管对象
class Seg:
    # 要求用户在调用的时候，填写所有段选管
    def __init__(self, a, b, c, d, e, f, g, dp):
        # 定义不同引脚对应不同的 Pin 对象
        self.a = Pin(a, Pin.OUT)
        self.b = Pin(b, Pin.OUT)
        self.c = Pin(c, Pin.OUT)
        self.d = Pin(d, Pin.OUT)
        self.e = Pin(e, Pin.OUT)
        self.f = Pin(f, Pin.OUT)
        self.g = Pin(g, Pin.OUT)
        self.dp = Pin(dp, Pin.OUT)

        # 将所有引脚对象存放在 led_list 中
        self.led_list = [self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.dp]

        # 把所有数字对应的逻辑电平存入字典中，逻辑值依次为 abcdefgh
        self.number_dict = {
            0: [0, 0, 0, 0, 0, 0, 1, 1],
            1: [1, 0, 0, 1, 1, 1, 1, 1],
            2: [0, 0, 1, 0, 0, 1, 0, 1],
            3: [0, 0, 0, 0, 1, 1, 0, 1],
            4: [1, 0, 0, 1, 1, 0, 0, 1],
            5: [0, 1, 0, 0, 1, 0, 0, 1],
            6: [0, 1, 0, 0, 0, 0, 0, 1],
            7: [0, 0, 0, 1, 1, 1, 1, 1],
            8: [0, 0, 0, 0, 0, 0, 0, 1],
            9: [0, 0, 0, 0, 1, 0, 0, 1],
        }

        # 初始化所有引脚
        self.clean()

    def clean(self):
        # 初始化状态
        for i in self.led_list:
            i.value(0)

    def display_number(self, number):
        # 显示数字
        logic_list = self.number_dict.get(number)
#         print(logic_list)
        if logic_list:
            for i in range(len(logic_list)):
                if logic_list[i] == 0:
                    self.led_list[i].value(1)
                else:
                    self.led_list[i].value(0)

