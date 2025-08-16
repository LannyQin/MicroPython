import serial
import time
import pyvjoy
import threading

# === 配置项 ===
SERIAL_PORT = 'COM5'      # 根据实际情况修改，比如 COM3, COM4（Windows）
BAUD_RATE = 115200

VJOY_DEVICE_ID = 1        # 通常为 1，表示第一个虚拟手柄

# PyVJoy 轴编号（常用映射，可根据需求调整）
AXIS_ROLL     = pyvjoy.HID_USAGE_RX  # 滚转 Roll → 通常用 Rx 轴
AXIS_PITCH    = pyvjoy.HID_USAGE_X   # 俯仰 Pitch → 通常用 X 轴
AXIS_THROTTLE = pyvjoy.HID_USAGE_Z   # 油门 Throttle → 通常用 Z 轴
AXIS_YAW      = pyvjoy.HID_USAGE_Y   # 偏航 Yaw → 通常用 Y 轴

# PyVJoy 轴范围设定
AXIS_CENTER = 0x4000         # 中立点 (16384)
AXIS_RANGE  = 0x4000         # 每侧范围 (±16384)

# 初始化 PyVJoy 虚拟手柄设备（设备号通常为 1）
j = pyvjoy.VJoyDevice(VJOY_DEVICE_ID)

def map_value(value, in_min, in_max, out_min, out_max):
    """将输入值从 [in_min, in_max] 线性映射到 [out_min, out_max]"""
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def update_vjoy_axes(roll, pitch, throttle, yaw,A,B,C,D):
    # try:
        # 映射 1000~2000 -> 0x0000 ~ 0x8000（围绕 0x4000）
        roll_axis    = AXIS_CENTER + map_value(roll,    1000, 2000, -AXIS_RANGE, +AXIS_RANGE)
        pitch_axis   = AXIS_CENTER + map_value(pitch,   1000, 2000, -AXIS_RANGE, +AXIS_RANGE)
        throttle_axis= AXIS_CENTER + map_value(throttle,1000, 2000, -AXIS_RANGE, +AXIS_RANGE)
        yaw_axis     = AXIS_CENTER + map_value(yaw,     1000, 2000, -AXIS_RANGE, +AXIS_RANGE)

        # 限制到合法范围 [0x0000, 0xFFFF]
        roll_axis    = max(0x0000, min(0xFFFF, roll_axis))
        pitch_axis   = max(0x0000, min(0xFFFF, pitch_axis))
        throttle_axis= max(0x0000, min(0xFFFF, throttle_axis))
        yaw_axis     = max(0x0000, min(0xFFFF, yaw_axis))

        a=False if A<1500 else True
        b=False if B<1500 else True
        c=False if C<1500 else True
        d=False if D<1500 else True

        # 设置到虚拟手柄
        j.set_axis(AXIS_ROLL,    roll_axis)
        j.set_axis(AXIS_PITCH,   pitch_axis)
        j.set_axis(AXIS_THROTTLE, throttle_axis)
        j.set_axis(AXIS_YAW,     yaw_axis)

        j.set_button(1, a)
        j.set_button(2, b)
        j.set_button(3, c)
        j.set_button(4, d)

        # 打印调试用（可选）
        print(f"\r[VJoy] Roll={roll:4d} → {roll_axis:5d}, "
              f"Pitch={pitch:4d} → {pitch_axis:5d}, "
              f"Throttle={throttle:4d} → {throttle_axis:5d}, "
              f"Yaw={yaw:4d} → {yaw_axis:5d}, "
              f"A={a}, B={b}, C={c}, D={d}",flush=True,end='')

    # except Exception as e:
    #     print(f"[错误] 更新 VJoy 轴失败:{e.__class__} {e}")

def read_from_serial():
    # try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)  # 等待串口稳定
        print(f"[上位机] 已连接串口 {SERIAL_PORT}，等待数据 (格式: Roll,Pitch,Throttle,Yaw | 范围 1000~2000) ...")

        while True:
            try:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 8:
                        try:
                            roll    = int(parts[0])
                            pitch   = int(parts[1])
                            throttle= int(parts[2])
                            yaw     = int(parts[3])
                            A=int(parts[4])
                            B=int(parts[5])
                            C=int(parts[6])
                            D=int(parts[7])

                            # 检查范围（调试用，可选）
                            if not (1000 <= roll <= 2000 and 1000 <= pitch <= 2000 and
                                    1000 <= throttle <= 2000 and 1000 <= yaw <= 2000):
                                print(f"[警告] 数据超出范围: R={roll}, P={pitch}, T={throttle}, Y={yaw}")

                            update_vjoy_axes(roll, pitch, throttle, yaw,A,B,C,D)

                        except ValueError:
                            print(f"[错误] 数据解析失败，非整数: {line}")
                    else:
                        print(f"[错误] 数据字段数量不对，期望 4 个，收到: {len(parts)}，内容: {line}")
            except UnicodeDecodeError:
                print("[错误] 串口数据解码失败（非 UTF-8 文本）")
            # except Exception as e:
            #     print(f"[错误] 串口读取异常: {e}")
    # except Exception as e:
    #     print(f"[致命错误] 无法打开串口 {SERIAL_PORT}: {e}")

if __name__ == "__main__":
    print("[上位机] 启动 ESP32 数据接收 & 虚拟手柄轴映射程序")
    print(f"    → 数据格式：Roll, Pitch, Throttle, Yaw （范围 1000~2000，用逗号分隔）")
    print(f"    → 映射到：PyVJoy 轴 Rx(X轴), X(Y轴), Z(油门), Y(偏航)")
    print(f"    → 请在 KSP 输入设置里绑定对应轴！")
    read_from_serial()