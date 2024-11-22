# buat ngendaliin motor

import RPi.GPIO as GPIO
import time

# Pin setup
PWM_L = 18
PWM_R = 19
R_EN = 23
L_EN = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup([PWM_L, PWM_R, R_EN, L_EN], GPIO.OUT)

# Inisialisasi PWM
pwm_l = GPIO.PWM(PWM_L, 100)
pwm_r = GPIO.PWM(PWM_R, 100)
pwm_l.start(0)
pwm_r.start(0)

# Fungsi gerak
def forward(speed):
    GPIO.output(R_EN, GPIO.HIGH)
    GPIO.output(L_EN, GPIO.LOW)
    pwm_l.ChangeDutyCycle(speed)
    pwm_r.ChangeDutyCycle(speed)

def backward(speed):
    GPIO.output(R_EN, GPIO.LOW)
    GPIO.output(L_EN, GPIO.HIGH)
    pwm_l.ChangeDutyCycle(speed)
    pwm_r.ChangeDutyCycle(speed)

def stop():
    pwm_l.ChangeDutyCycle(0)
    pwm_r.ChangeDutyCycle(0)

# Contoh gerakan
try:
    forward(50)
    time.sleep(2)
    stop()
except KeyboardInterrupt:
    GPIO.cleanup()



#########################################################################