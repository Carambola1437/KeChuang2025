from machine import UART, Pin
import time
import button
import myservo

#通讯模块


# 初始化 UART2（TX=17, RX=16）
uart = UART(2, baudrate=9600, tx=22, rx=23)


zhuangtai = 0



def uart_init():
    # 给模块发送数据
    uart.write("Hello from ESP32\r\n")
    
    
def read_info():
    if uart.any():  # 如果接收到数据
        data = uart.read()
        try:
            # 尝试转成字符串并打印
            text = data.decode('utf-8').strip()
            print("接收到：", text)
            # 根据收到的内容做响应
            panduan(text)

        except Exception as e:
            print("接收解码错误：", e)
def panduan(mingling):
    
    '''
    ###a:开炮
    b:升起炮台
    e:落下炮台
    f:瞄准
    g:关闭瞄准
    '''
    global zhuangtai
    
    if mingling=='b':
        if zhuangtai == 0:
            time.sleep(1)
            myservo.tai_qi()
            zhuangtai = 1
       
    if mingling=='e':
        if zhuangtai == 1:
            time.sleep(1)
            myservo.tai_luo()
            zhuangtai = 0
    if mingling=='f':
        button.miaozhun_kai()      
    if mingling=='g':
        button.miaozhun_guan()         
        
    if mingling=='a' and zhuangtai == 1 :
        time.sleep(1)
        myservo.fa_she()
        myservo.fa_she_init()
        
    
        
        
        
        