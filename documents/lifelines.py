#	Ryan Do - N01044391
#	November 21, 2016
#	Lifelines: Breathalyzer

import time
import RPi.GPIO as GPIO
GPIO.VERSION
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

from smbus import SMBus

bus = SMBus(1)

#read the sensors given the pin
def read_ain(i):    
    global bus
    bus.write_byte(0x48, i)
    bus.read_byte(0x48)
    bus.read_byte(0x48)
    return bus.read_byte(0x48)

while(True):
    alcohol = read_ain(2)*0.001		#read the alcohol sensor on pin 2
    heartrate = read_ain(1)			#read the heartrate sensor on pin 1

    print "-------------------------\n"
    print("Alcohol Sensor: {0:.3f}%".format(alcohol))	#print alcohol reading
	
	#turn on the LED
    if(heartrate<60) or (heartrate>100):
	GPIO.output(11,0)
	GPIO.output(12,1)
    else:
	GPIO.output(11,1)
	GPIO.output(12,0)
	
    print("Heart Rate Sensor: {0:.0f} BPM\n".format(heartrate))		#print heartrate reading
    time.sleep(1)#update every 1 second