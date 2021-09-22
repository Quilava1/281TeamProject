#!/usr/bin/python3
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
import time
import os

LFL = 3
LFR = 5
USin = 7
USout = 11
GPIO.setmode(GPIO.BOARD)

#line followers
GPIO.setup(LFL, GPIO.IN) #left follower
GPIO.setup(LFR, GPIO.IN) #right follower
#GPIO.setup(3, GPIO.IN)
#GPIO.setup(4, GPIO.IN)


#Ultrasonic
GPIO.setup(USin, GPIO.IN)
GPIO.setup(USout, GPIO.OUT)
#motor forward
#GPIO.setup(7, GPIO.OUT)

#steering bit 1
#GPIO.setup(8, GPIO.OUT)
#steering bit 2
#GPIO.setup(9, GPIO.OUT)
#steering bit 3
#GPIO.setup(10, GPIO.OUT)


Laps = 3

def modFourIncrement(x):
    y = (x + 1) % 4
    return y

def measure():
    GPIO.output(USout, 1)
    time.sleep(0.00001)   #set trigger for 10 microseonds for 8 cycle sonic
    GPIO.output(USout, 0)
    startTime = time.time()
    stopTime = time.time()
    while  GPIO.input(USin) == 0: #set start time until posedge of input
        startTime = time.time()
    while GPIO.input(USin) == 1: #set stoptime till negedge of input
        stopTime = time.time()
    deltaTime = stopTime - startTime
    distance = (deltaTime * 34300) / 2
    return distance

state = 0
Direction = 'halt'
tolerance = 20
dist = 0.00
 
 
 
 
 
while state >= 0:
 
 
    if GPIO.input(LFL) == 1:
        if GPIO.input(LFR) == 1:
            state = 1
        else:
            state = 2
    else:
        if GPIO.input(LFR) == 1:
            state = 3
        else:
            state = 4
 
    dist = measure()
    
    if dist < tolerance:
        state = 4
    
    
    if state != 0:
        if state == 1:
            Direction = 'Straight'
        elif state ==2:
            Direction = 'Left'
        elif state == 3:
            Direction = 'Right'
        elif state == 4:
            Direction = 'Halt'
            
            
    os.system('cls' if os.name=='nt' else 'clear')        
    print('Left:' +str(GPIO.input(LFL)) +   '  Right:' +str(GPIO.input(LFR))  +  '  Direction:' + Direction +'    Barrier: ' + str(dist) +'cm' , end = '\r')
    time.sleep(1)
