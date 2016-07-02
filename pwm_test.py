import time
import pigpio

pwm_pin = 4

#connect to pigpiod daemon
pi = pigpio.pi()

# setup pin as an output
pi.set_mode(pwm_pin, pigpio.OUTPUT)

# pi set frequency
pi.set_PWM_frequency(pwm_pin, 1000)
pi.set_PWM_range(pwm_pin, 100)

pi.set_PWM_dutycycle(pwm_pin,75)
#time.sleep(0.5)

#pi.set_PWM_dutycycle(pwm_pin,25)
#time.sleep(0.5)

#cleanup
#pi.set_PWM_dutycycle(pwm_pin,0)
#pi.set_mode(pwm_pin, pigpio.INPUT)

#disconnect
pi.stop()
