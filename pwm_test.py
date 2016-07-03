import time
import pigpio

pwm_pin = 4

#connect to pigpiod daemon
pi = pigpio.pi()

# setup pin as an output
pi.set_mode(pwm_pin, pigpio.OUTPUT)


# pi set frequency
freq = 1000
pi.set_PWM_frequency(pwm_pin, freq)
pi.set_PWM_range(pwm_pin, 100)

dc = 75
pi.set_PWM_dutycycle(pwm_pin,dc)
time.sleep(1.0)

#cleanup
pi.set_PWM_dutycycle(pwm_pin,0)
pi.set_mode(pwm_pin, pigpio.INPUT)

#disconnect
pi.stop()
