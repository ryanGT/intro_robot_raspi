import time
import pigpio

motor_1_pin = 4
motor_2_pin = 17

#connect to pigpiod daemon
pi = pigpio.pi()

# setup pin as an output
pi.set_mode(motor_1_pin, pigpio.OUTPUT)
pi.set_mode(motor_2_pin, pigpio.OUTPUT)

# pi set frequency
pi.set_PWM_frequency(motor_1_pin, 1000)
pi.set_PWM_range(motor_1_pin, 100)
pi.set_PWM_frequency(motor_2_pin, 1000)
pi.set_PWM_range(motor_2_pin, 100)

pi.set_PWM_dutycycle(motor_1_pin,75)
pi.set_PWM_dutycycle(motor_2_pin,25)
time.sleep(0.5)

pi.set_PWM_dutycycle(motor_1_pin,25)
pi.set_PWM_dutycycle(motor_2_pin,50)
time.sleep(0.5)

#cleanup
pi.set_PWM_dutycycle(motor_1_pin,0)
pi.set_mode(motor_1_pin, pigpio.INPUT)
pi.set_PWM_dutycycle(motor_2_pin,0)
pi.set_mode(motor_2_pin, pigpio.INPUT)
#disconnect
pi.stop()
