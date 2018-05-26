import RPi.GPIO as GPIO
import time         

FREQ = 50

class Servo:
	def __init__(self, PIN):
		self.PIN = PIN
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM) 
		GPIO.setup(PIN,GPIO.OUT)
		self.pwm = GPIO.PWM(PIN, FREQ) 
		self.pwm.start(2.5)
		self.angle = None

	def changeAngle(self, angle):
		convertAngle = {
			0: 2.7,
			22.5: 3.9,
			45: 5.2,
			67.5: 6.4,
			90: 7.6,
			112.5: 9,
			135: 10.25,
			157.5: 11.6,
			180: 12.9
		}
		if self.angle != angle:
			GPIO.output(self.PIN, True)
			self.pwm.ChangeDutyCycle(convertAngle.get(angle))
			self.angle = angle
			print self.angle
			time.sleep(1)
			GPIO.output(self.PIN, False)
		self.pwm.ChangeDutyCycle(0)

### Testcases
#servo = Servo(03)
#servo.changeAngle(0)
#servo.changeAngle(22.5)
#servo.changeAngle(45)
#servo.changeAngle(67.5)
#servo.changeAngle(90)
#servo.changeAngle(112.5)
#servo.changeAngle(135)
#servo.changeAngle(157.5)
#servo.changeAngle(180)
#servo.changeAngle(0)