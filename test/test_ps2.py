from machine import Pin, UART
import time

# 定义 PWM 通道对应的 GPIO 引脚（根据你的接线修改）
pwm_pins = [25, 26, 27, 14, 18, 5, 17, 16]  # 假设 CH1~CH6 分别接 GPIO25~GPIO13
uart = UART(1, baudrate=115200, tx=4, rx=5)  # ESP32 UART1 (GPIO4=TX, GPIO5=RX)

def measure_pwm(pin, timeout=1000000):  # 1秒超时
    start_time = time.ticks_us()
    pulse_start = 0
    pulse_end = 0
    high_time = 0

    while time.ticks_diff(time.ticks_us(), start_time) < timeout:
        if pin.value() == 1 and pulse_start == 0:  # 上升沿
            pulse_start = time.ticks_us()
        elif pin.value() == 0 and pulse_start != 0:  # 下降沿
            pulse_end = time.ticks_us()
            high_time = time.ticks_diff(pulse_end, pulse_start)
            return high_time
    return 0  # 超时返回 0

while True:
    pwm_data = []
    for pin_num in pwm_pins:
        pin = Pin(pin_num, Pin.IN)
        pwm_data.append(str(measure_pwm(pin)))  # 读取每个通道的 PWM 高电平时间（μs）
    
    # 发送数据格式：CH1,CH2,CH3,CH4,CH5,CH6\n（例如 "1000,1500,2000,1200,1800,1600\n"）
    data_str = ",".join(pwm_data) + "\n"
    uart.write(data_str)
    print(",".join(pwm_data))



'''from machine import Pin
import time

# 定义 PWM 通道对应的 GPIO 引脚（根据你的接线修改）
pwm_pins = [25, 26, 27, 14]  # 假设 CH1~CH6 分别接 GPIO25~GPIO13

# 存储每个通道的高电平时间（μs）
pwm_values = [0] * len(pwm_pins)

def measure_pwm(pin, timeout=1000000):  # 1秒超时
    start_time = time.ticks_us()
    pulse_start = 0
    pulse_end = 0
    high_time = 0

    while time.ticks_diff(time.ticks_us(), start_time) < timeout:
        if pin.value() == 1 and pulse_start == 0:  # 上升沿
            pulse_start = time.ticks_us()
        elif pin.value() == 0 and pulse_start != 0:  # 下降沿
            pulse_end = time.ticks_us()
            high_time = time.ticks_diff(pulse_end, pulse_start)
            return high_time
    return 0  # 超时返回 0

while True:
    for i, pin_num in enumerate(pwm_pins):
        pin = Pin(pin_num, Pin.IN)
        pwm_values[i] = measure_pwm(pin)
        print(f"ch{i+1}:{pwm_values[i]}")
    time.sleep(0.08)  # 每 100ms 读取一次
'''


'''
from machine import Pin
import time

pwm_pin = Pin(33, Pin.IN)  # 假设 CH1 接在 GPIO25

def measure_pwm(pin, timeout=1000000):  # 1秒超时
    start_time = time.ticks_us()
    pulse_start = 0
    pulse_end = 0
    high_time = 0

    while time.ticks_diff(time.ticks_us(), start_time) < timeout:
        if pin.value() == 1 and pulse_start == 0:  # 上升沿（PWM 开始）
            pulse_start = time.ticks_us()
        elif pin.value() == 0 and pulse_start != 0:  # 下降沿（PWM 结束）
            pulse_end = time.ticks_us()
            high_time = time.ticks_diff(pulse_end, pulse_start)  # 高电平时间（μs）
            print(f"PWM High Time: {high_time} μs")
            pulse_start = 0

while True:
    measure_pwm(pwm_pin)
'''



'''from machine import Pin,ADC
from time import sleep_ms

x=ADC(Pin(33),atten=ADC.ATTN_11DB)
y=ADC(Pin(35),atten=ADC.ATTN_11DB)
button=Pin(0,Pin.IN)

while True:
    print('x:%d y:%d button:%d'%(x.read(),y.read(),(0 if button.value() else 4095)))
    sleep_ms(25)'''