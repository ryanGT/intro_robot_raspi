from numpy import *
import time
import pigpio

motor_1_pwm = 4
motor_1_in1 = 17
motor_1_in2 = 27

motor_2_pwm = 16
motor_2_in4 = 20
motor_2_in3 = 21

#connect to pigpiod daemon
pi = pigpio.pi()

# set all to outputs
all_list = [motor_1_pwm, motor_1_in1, motor_1_in2, \
            motor_2_pwm, motor_2_in4, motor_2_in3]

for pin in all_list:
    pi.set_mode(pin, pigpio.OUTPUT)

# pi set frequency
pwm_pins = [motor_1_pwm, motor_2_pwm]

# non-pwm pins are direction control pins
direction_pins = [pin for pin in all_list if pin not in pwm_pins]

for pin in pwm_pins:
    pi.set_PWM_frequency(pin, 1000)
    pi.set_PWM_range(pin, 100)


def command_motor_1(speed):
    if speed > 0:
        #print('forward')
        pi.write(motor_1_in1, 0)
        pi.write(motor_1_in2, 1)
        pi.set_PWM_dutycycle(motor_1_pwm,speed)
    elif speed < 0:
        #print('reverse')
        pi.write(motor_1_in1, 1)
        pi.write(motor_1_in2, 0)
        pi.set_PWM_dutycycle(motor_1_pwm,abs(speed))
    else:
        #print('stopping')
        pi.set_PWM_dutycycle(motor_1_pwm,0)
        pi.write(motor_1_in1, 0)
        pi.write(motor_1_in2, 0)


def command_motor_2(speed):
    if speed > 0:
        #print('forward')
        pi.write(motor_2_in3, 0)
        pi.write(motor_2_in4, 1)
        pi.set_PWM_dutycycle(motor_2_pwm,speed)
    elif speed < 0:
        #print('reverse')
        pi.write(motor_2_in3, 1)
        pi.write(motor_2_in4, 0)
        pi.set_PWM_dutycycle(motor_2_pwm,abs(speed))
    else:
        #print('stopping')
        pi.set_PWM_dutycycle(motor_2_pwm,0)
        pi.write(motor_2_in3, 0)
        pi.write(motor_2_in4, 0)


## command_motor_1(50)
## command_motor_2(50)
## time.sleep(1.0)

## command_motor_1(-25)
## command_motor_2(-25)
## time.sleep(0.5)

## command_motor_1(-50)
## command_motor_2(-50)
## time.sleep(1.0)

## command_motor_1(50)
## command_motor_2(-50)
## time.sleep(0.5)

## command_motor_1(-50)
## command_motor_2(50)
## time.sleep(0.5)

def _demo(listin, cmd=command_motor_1, mydelay=1.0):
    for speed in listin:
        print('speed: %i' % speed)
        cmd(speed)
        time.sleep(mydelay)


def demo1(listin, mydelay=1.0):
    _demo(listin, cmd=command_motor_1, mydelay=mydelay)

def demo2(listin, mydelay=1.0):
    _demo(listin, cmd=command_motor_2, mydelay=mydelay)


case = 1

if case == 1:
    list1 = arange(0,105,10)
    demo2(list1)
    list1b = arange(100, -5, -10)
    demo2(list1b)
elif case == 2:
    list1neg = arange(0,-105,-10)
    demo2(list1neg)
    list1negb = arange(-100,5,10)
    demo2(list1negb)
#cleanup
for pin in pwm_pins:
    pi.set_PWM_dutycycle(pin,0)

for pin in direction_pins:
    pi.write(pin,0)
    
for pin in all_list:
    pi.set_mode(pin, pigpio.INPUT)
    
#disconnect
pi.stop()
