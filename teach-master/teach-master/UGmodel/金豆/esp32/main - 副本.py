# main.py -- put your code here!
import machine
import oled128x64
from expression_picture import Happy
import time

i2c_extend = machine.SoftI2C(scl=machine.Pin(16), sda=machine.Pin(17), freq=400000)
oled = oled128x64.OLED(i2c_extend, address=0x3c, font_address=0x3A0000)

# 显示 Happy 表情图
oled.image(Happy)
time.sleep(3)

# 清除整屏
oled.fill(0)
oled.show()

# 启动加载动画
dots = ['。', '。。', '。。。']
while True:
    for d in dots:
        oled.fill_rect(0, 20, 128, 16, 0)  # 只清除一行文字区域
        oled.shows('正在启动' + d, x=0, y=20, size=1, space=0, center=False)
        oled.show()
        time.sleep(0.2)
