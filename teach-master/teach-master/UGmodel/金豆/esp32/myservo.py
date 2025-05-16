import machine
from machine import Pin, PWM
import servo


#炮台舵机接口21
#tai_pin = PWM(Pin(21), freq=50)



def tai_angle(angle):
    print("zhuandong",angle)
    servo.servo180_angle(16,angle)
#舵机初始化
def tai_init():
    servo.servo180_angle(16,90)
    
    
def tai_qi():
    servo.servo180_angle(16,10)
    
    
def tai_luo():
    servo.servo180_angle(16,90)

def fa_she_init():
    servo.servo180_angle(17,45)
    
def fa_she():
    servo.servo180_angle(17,90)
    


