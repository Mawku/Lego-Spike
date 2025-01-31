from hub import port
from hub import motion_sensor
import color_sensor
import runloop
import motor
import time
from time import sleep


async def walk():
    a=60-color_sensor.reflection(port.A)
    v=0.1*a
    sx=int(150.0-v)
    dx=int(-150.0-v)
    reflectionA=color_sensor.reflection(port.A)
    reflectionB=color_sensor.reflection(port.B)
    if reflectionA<60:
        motor.run_for_degrees(port.D,40, sx)
    elif reflectionB<60:
        motor.run_for_degrees(port.C,40,dx)
    else:
        motor.run_for_time(port.C,500,dx)
        motor.run_for_time(port.D,500,sx)

def color_check():
    colorA=color_sensor.color(port.A)
    colorB=color_sensor.color(port.B)
    
    if colorA == 6 :
        return 1;
    elif colorB == 6:
        return 2;
    else:
        return 0;

async def color_act():
    a=60-color_sensor.reflection(port.B)
    v=0.1*a
    sx=int(400.0-v)
    dx=int(-400.0-v)
    getcolor = 0
    getcolor=color_check();
    if(getcolor==1):
        motor.run_for_degrees(port.D,720,dx)
    elif(getcolor==2):
        motor.run_for_degrees(port.C,720,dx)
    elif(getcolor==3):
        motor.run_for_degrees(port.C,2880,dx)



async def main():

    
    while True: 
        runloop.run (walk())
        runloop.run (color_act())     
            

runloop.run(main())