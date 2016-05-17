import time
import pigpio

motor_1_pwm = 4
motor_1_in1 = 17
motor_1_in2 = 27


#connect to pigpiod daemon
pi = pigpio.pi()

# setup pin as an output
pi.set_mode(motor_1_pwm, pigpio.OUTPUT)
pi.set_mode(motor_1_in1, pigpio.OUTPUT)
pi.set_mode(motor_1_in2, pigpio.OUTPUT)

# pi set frequency
pi.set_PWM_frequency(motor_1_pwm, 1000)
pi.set_PWM_range(motor_1_pwm, 100)


def command_motor_1(speed):
    if speed > 0:
        pi.write(motor_1_in1, 1)
        pi.write(motor_1_in2, 0)
        pi.set_PWM_dutycycle(motor_1_pwm,speed)
    elif speed < 0:
        pi.write(motor_1_in1, 0)
        pi.write(motor_1_in2, 1)
        pi.set_PWM_dutycycle(motor_1_pwm,abs(speed))
    else:
        pi.set_PWM_dutycycle(motor_1_pwm,0)
        pi.write(motor_1_in1, 0)
        pi.write(motor_1_in2, 0)
        

command_motor_1(25)
time.sleep(0.5)

command_motor_1(-25)
time.sleep(0.5)

#cleanup
pi.set_PWM_dutycycle(motor_1_pwm,0)
pi.set_mode(motor_1_pwm, pigpio.INPUT)
pi.write(motor_1_in1,0)
pi.set_mode(motor_1_in1, pigpio.INPUT)
pi.write(motor_1_in2,0)
pi.set_mode(motor_1_in2, pigpio.INPUT)
#disconnect
pi.stop()
