import serial
import pynput
import time
import threading

# 1. 设置串口（修改为你的 COM 端口，如 'COM3'）
ser = serial.Serial('COM5', 115200, timeout=0.1)  # Windows: 'COM3', Linux/Mac: '/dev/ttyUSB0'
lock=threading.Lock()
key_data=[[0,'q','e',1550,1450],[1,'w','s',1550,1450],[2,pynput.keyboard.Key.ctrl_l,pynput.keyboard.Key.shift_l,1600,1400],[3,'a','d',1550,1450]]
time.sleep(3)

controller=pynput.keyboard.Controller()

def press_and_release():
    lock.acquire()
    line=line_out
    lock.release()
    print('\r' + line, flush=False, end='')
    if line:
        try:
            values = list(map(int, line.split(',')))  # 解析为 [CH1, CH2, CH3, CH4]
            press_list = []
            release_list = []
            for index, key_1, key_2,min,max in key_data:
                data = values[index]
                if data >= min:
                    press_list.append(key_2)
                    release_list.append([key_2, (data - 1500) / 50000 if (data - 1500) / 50000 <= 0.05 else 0.05])
                elif data < max:
                    press_list.append(key_1)
                    release_list.append([key_1, (1500 - data) / 50000 if (1500 - data) / 50000 <= 0.05 else 0.05])
                else:
                    controller.release(key_2)
                    controller.release(key_1)
            t0 = time.time()
            for key in press_list:
                controller.press(key)
            while len(release_list) > 0:
                tnow = time.time()
                for key, sec in release_list:
                    if tnow - t0 >= sec:
                        controller.release(key)
                        release_list.remove([key, sec])
                        break
            while time.time()-t0<=0.05:
                pass
        except ValueError:
            print(f"无法解析数据: {line}")

def super_visor():
    time.sleep(3)
    while True:
        press_and_release()

threading.Thread(target=super_visor).start()

# 3. 实时读取串口数据
try:
    while True:
        if ser.in_waiting:
            try:
                lock.acquire()
                line_out = ser.readline().decode('utf-8').strip()  # 读取一行数据（如 "1520,1509,1081,1510"）
                lock.release()
            except:
                continue
        # time.sleep(0.02)  # 避免 CPU 占用过高
except KeyboardInterrupt:
    print("程序终止")
finally:
    ser.close()  # 关闭串口



"""import serial
import time
import matplotlib.pyplot as plt
from collections import deque

# 串口配置（根据你的 ESP32 UART 设置）
ser = serial.Serial('COM5', 115200, timeout=0.1)  # Windows: 'COM3', Linux/Mac: '/dev/ttyUSB0'

# 存储最近 100 个数据点（用于绘图）
data_history = [deque(maxlen=10) for _ in range(6)]  # 假设 6 个通道

plt.ion()  # 开启交互模式
fig, axs = plt.subplots(6, 1, figsize=(8, 12))
lines = [ax.plot([], [])[0] for ax in axs]

while True:
    if ser.in_waiting:
        line = ser.readline().decode('utf-8').strip()  # 读取一行数据（如 "1000,1500,2000,1200,1800,1600\n"）
        print(line)
        try:
            if line:
                values = list(map(int, line.split(',')))  # 解析为 [CH1, CH2, CH3, CH4, CH5, CH6]
                for i, val in enumerate(values):
                    data_history[i].append(val)
                    lines[i].set_data(range(len(data_history[i])), data_history[i])
                    axs[i].relim()
                    axs[i].autoscale_view()
                    axs[i].set_title(f'CH{i+1} (PWM: {val} μs)')
                plt.pause(0.01)  # 刷新图表
        except:
            pass"""