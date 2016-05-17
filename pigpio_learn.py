import time
import pigpio

motor_1_pin = 4

#connect to pigpiod daemon
pi = pigpio.pi()

# setup pin as an output
pi.set_mode(motor_1_pin, pigpio.OUTPUT)

# pi set frequency
pi.set_PWM_frequency(motor_1_pin, 1000)
pi.set_PWM_range(motor_1_pin, 100)

for i in range(5, 100, 5):
    pi.set_PWM_dutycycle(motor_1_pin,75)
    time.sleep(0.1)

for i in range(100, 5, -5):
    pi.set_PWM_dutycycle(motor_1_pin,25)
    time.sleep(0.1)

#cleanup
pi.set_PWM_dutycycle(motor_1_pin,0)
pi.set_mode(motor_1_pin, pigpio.INPUT)
#disconnect
pi.stop()
