# main.py -- put your code here!
from machine import Pin
from neopixel import NeoPixel
import oled
import uasyncio as asyncio

import myservo
import uart
import led

# 初始化发射
myservo.fa_she_init()
# 初始化炮台
myservo.tai_init()
#屏幕初始化
oled.power_on()



zhuangtai = 0
async def main ():
    print("main")
    asyncio.create_task(led.flowing())
    while True:
        uart.read_info()
        await asyncio.sleep(0)


asyncio.run(main())
