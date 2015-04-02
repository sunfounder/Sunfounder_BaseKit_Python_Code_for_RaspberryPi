#!/usr/bin/env python
import RPi.GPIO as GPIO
import ADC0832

LedPin = 15

def printMsg():
	print 'Press Ctrl+C to end the program...'

def adcInit():
	ADC0832.setup()

def ledInit():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LedPin, GPIO.OUT)
	GPIO.output(LedPin, GPIO.LOW)  # led off

def loop():
	p = GPIO.PWM(LedPin, 1000) # Set PWM Frequence to 1000Hz
	p.start(0)
	while True:
		res = ADC0832.getResult()
		if res > 100:
			res = 100
		p.ChangeDutyCycle(res)   # Change the duty cycle according to res
		
if __name__ == '__main__':
	printMsg()
	adcInit()
	ledInit()
	try:
		loop()
	except KeyboardInterrupt: 
		ADC0832.destroy()
		print 'The end !'
