try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
import time

GPIO.setmode(GPIO.BOARD)

#line followers
GPIO.setup(1, GPIO.IN)
GPIO.setup(2, GPIO.IN)
#GPIO.setup(3, GPIO.IN)
#GPIO.setup(4, GPIO.IN)


#Ultrasonic
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.OUT)
#motor forward
GPIO.setup(7, GPIO.OUT)

#steering bit 1
GPIO.setup(8, GPIO.OUT)
#steering bit 2
GPIO.setup(9, GPIO.OUT)
#steering bit 3
GPIO.setup(10, GPIO.OUT)


Laps = 3

def modFourIncrement(x):
    y = (x + 1) % 4
    return y

def measure():
    GPIO.output(6, 1)
    time.sleep(0.00001)
    GPIO.output(6, 0)
    
    startTime = time.time()
    stopTime = time.time()
    while GPIO.input(5) == 0:
        startTime = time.time()
    while GPIO.input(6) == 1:
        stopTime = time.time()
    deltaTime = stopTime - startTime
    distance = (deltaTime * 34300) / 2
    return distance

 state = 0
 Direction = 'halt'
 dt = 0
 dist = 0.00
 
 
 
 
 
 while state >= 0:
 
 
    if GPIO.input(1) == 1:
        if GPIP.input(2) == 1:
            state == 1
        else:
            state == 2
    else:
        if GPIP.input(2) == 1:
            state == 3
        else:
            state == 4
 
    dist = measure()

    if state == 0:
        elif state == 1:
            Direction = 'Straight'
        elif state ==2:
            Direction = 'Left'
        elif state == 3:
            Direction = 'Right'
        elif state == 4:
            Direction = 'Halt'
            
            
            
    print(“Left:1    Right:0    Direction:” + Direction +'     Barrier: ' + dist +'cm' , end=”\r”)