import machine

import imu
import time


i2c_extend = machine.SoftI2C(scl = machine.Pin(16), sda = machine.Pin(17), freq = 50000)
xsensor = imu.MPU6050(i2c_extend)
while True:
    accel , gyro =xsensor.sensors
    print(accel.x)
    print(accel.y)
    print(accel.z)

    print('------------')
    time.sleep(0.5)