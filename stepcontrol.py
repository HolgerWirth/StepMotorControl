from time import sleep
import RPi.GPIO as GPIO

# Define the 4 GPIO ports
A=24
B=25
C=8
D=7
time = 0.005

def Init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(A,GPIO.OUT)
    GPIO.setup(B,GPIO.OUT)
    GPIO.setup(C,GPIO.OUT)
    GPIO.setup(D,GPIO.OUT)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)

def Step1():
    GPIO.output(D, True)
    sleep (time)
    GPIO.output(D, False)

def Step2():
    GPIO.output(D, True)
    GPIO.output(C, True)
    sleep (time)
    GPIO.output(D, False)
    GPIO.output(C, False)

def Step3():
    GPIO.output(C, True)
    sleep (time)
    GPIO.output(C, False)

def Step4():
    GPIO.output(B, True)
    GPIO.output(C, True)
    sleep (time)
    GPIO.output(B, False)
    GPIO.output(C, False)

def Step5():
    GPIO.output(B, True)
    sleep (time)
    GPIO.output(B, False)

def Step6():
    GPIO.output(A, True)
    GPIO.output(B, True)
    sleep (time)
    GPIO.output(A, False)
    GPIO.output(B, False)

def Step7():
    GPIO.output(A, True)
    sleep (time)
    GPIO.output(A, False)

def Step8():
    GPIO.output(D, True)
    GPIO.output(A, True)
    sleep (time)
    GPIO.output(D, False)
    GPIO.output(A, False)

def Clean():
    GPIO.cleanup()

