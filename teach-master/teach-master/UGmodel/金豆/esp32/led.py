import machine
import neopixel
import time
import uasyncio as asyncio

# 初始化
led_pin = machine.Pin(18)       # 替换为你使用的引脚
num_leds = 7
np = neopixel.NeoPixel(led_pin, num_leds)

# 生成彩虹色列表（wheel 是常用的彩虹映射函数）
def wheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)

# 生成 47 个不同的颜色点（均匀分布在 0~255 的色轮上）
color_list = [wheel(int(i * 255 / (num_leds - 1))) for i in range(num_leds)]

# 清除所有灯
def clear():
    for i in range(num_leds):
        np[i] = (0, 0, 0)
    np.write()

# 炫彩充能效果
async def rainbow_charge(delay=0.01):
    for i in range(num_leds):
        np[i] = color_list[i]
        np.write()
        #time.sleep(delay)
        await asyncio.sleep(delay)
        #print("led")


async def flowing():
    # 主程序循环
    #print("led")
    while True:
        clear()
        await rainbow_charge(1)  # 充能速度调节
        #time.sleep(1)         # 等待 1 秒，显示完整效果
        await asyncio.sleep(0)

