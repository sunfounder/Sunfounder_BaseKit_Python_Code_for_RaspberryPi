#!/usr/bin/env python
import RPi.GPIO as GPIO
import ADC0832
import time

BeepPin = 15

def printMsg():
	print 'Press Ctrl+C to end the program...'

def adcInit():
	ADC0832.setup()

def beepInit():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(BeepPin, GPIO.OUT)
	GPIO.output(BeepPin, GPIO.LOW)

def beep():
	GPIO.output(BeepPin, GPIO.HIGH)
	time.sleep(0.2)
	GPIO.output(BeepPin, GPIO.LOW)
	time.sleep(0.2)

def loop():
	while True:
		res = ADC0832.getResult()
		print 'res = %d' % res
		if res > 200:
			beep()
		
if __name__ == '__main__':
	printMsg()
	adcInit()
	beepInit()
	try:
		loop()
	except KeyboardInterrupt: 
		ADC0832.destroy()
		print 'The end !'
