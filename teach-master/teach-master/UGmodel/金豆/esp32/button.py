from machine import Pin
import time


class ThreeWireButton:
    def __init__(self, pin_num, on_click=None, debounce_ms=50):
        self.button_pin = Pin(pin_num, Pin.IN)
        self.button_pressed = False
        self.press_time = 0
        self.last_trigger_time = 0
        self.debounce_ms = debounce_ms
        self.on_click = on_click

        self.button_pin.irq(
            trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING,
            handler=self._irq_handler
        )

    def _irq_handler(self, pin):
        now = time.ticks_ms()

        # 防抖：距离上次触发太近就忽略
        if time.ticks_diff(now, self.last_trigger_time) < self.debounce_ms:
            return

        self.last_trigger_time = now

        level = pin.value()
        if level == 1:  # 按下
            self.button_pressed = True
            self.press_time = now
            print("检测到按钮按下")
        elif level == 0 and self.button_pressed:  # 抬起
            self.button_pressed = False
            duration = time.ticks_diff(now, self.press_time)
            print("检测到按钮弹起，持续时间:", duration, "ms")
            if self.on_click:
                self.on_click(duration)

#按钮测试回调函数
def on_button_click(duration):
    print(">>> 用户按了一下按钮，持续", duration, "ms")
    miaozhun()
    

#按钮测试

#btn = ThreeWireButton(pin_num=22, on_click=on_button_click)




pin23 = Pin(23, Pin.IN)

# 定义为输出引脚

#红点瞄准引脚
laser_pin = Pin(5, Pin.OUT)

#红点瞄准状态
laser_state = 0  # 当前是关闭状态


def miaozhunqiehuan():
    global laser_pin
    global laser_state
    laser_state = 1 - laser_state  # 0 -> 1, 1 -> 0
    laser_pin.value(laser_state)
    print("红外瞄准器状态：", "开启" if laser_state else "关闭")

def miaozhun_kai():
    global laser_state
    global laser_pin
    laser_pin.value(1)
    laser_state = 1 
def miaozhun_guan():
    global laser_state
    global laser_pin
    laser_pin.value(0)
    laser_state = 0 

miaozhun_guan()