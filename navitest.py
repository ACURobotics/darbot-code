import spidev
import time
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 2000000

def write_pot(input):
	msb = input >> 8
	lsb = input & 0xFF
	spi.xfer([msb,lsb])

#def update_v(input):
#	if(input < 50.00):
		#change to 6 V to stop
#		v = 0x10AD
	#else:
		

x = 0

#6V = B9  7V = 3F  5V = EF
v = 0x10B9
vl = 0xB9

#Keep at 7V until see's wall
write_pot(v)
write_pot(vl)

while x == 0:
	GPIO.setmode(GPIO.BCM)
	#Front sensor
	TRIG = 21
	ECHO = 20

	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)

	GPIO.output(TRIG, False)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
	  pulse_start = time.time()

	while GPIO.input(ECHO)==1:
	  pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance_front = pulse_duration * 17150

	distance_front = round(distance_front, 2)
	print "Distance:",distance_front,"cm"
	
	if(distance_front < 50.00):
		#change to 6 V to stop
		v = 0x1050
		write_pot(v)
		vl = 0x58
		write_pot(vl)
		time.sleep(2.5)
		vl = 0xB9
		write_pot(vl)
		#vl = 0xAD
		#write_pot(vl)

	print "v = ", v
	GPIO.cleanup()
	

	GPIO.setmode(GPIO.BCM)
	#Left sensor
	TRIG = 26
	ECHO = 19

	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)

	GPIO.output(TRIG, False)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
	  pulse_start = time.time()

	while GPIO.input(ECHO)==1:
	  pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance_left = pulse_duration * 17150

	distance_left = round(distance_left, 2)
	print "Distance:",distance_left,"cm"
	
	if(distance_left < 25.00):
		vl = 0x3F
		write_pot(vl)
		#time.sleep(1)
		#vl = 0xA5
	else:
		vl = 0xA5
		write_pot(vl)
	print "vl = ", vl
	time.sleep(1)
	GPIO.cleanup()