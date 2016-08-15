import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 2000000

def write_pot(input):
	msb = input >> 8
	lsb = input & 0xFF
	spi.xfer([msb,lsb])

while True:
	#5V
	write_pot(0x10B9)
	write_pot(0xB9)
	time.sleep(3)
	write_pot(0x103F)
	write_pot(0x3F)
	time.sleep(3)
	#6V
	#write_pot(0x10A)
	#time.sleep(4)
	#write_pot(0xEF)
	#time.sleep(4)
	#7V
	#write_pot(0x102F)
	#time.sleep(1)
	#write_pot(0xEF)
	#time.sleep(1)
	#write_pot(0xFF)
	#time.sleep(1)
	#write_pot(0x10BF)
	#time.sleep(1)
	#write_pot(0xBF)
	#time.sleep(1)
	#write_pot(0x101F)
	#time.sleep(1)
	#write_pot(0x00)
	#time.sleep(1)
	#for i in range(0x00,0x1FF,1):
	#	write_pot(i)
	#	time.sleep(0.005)
	#for i in range(0x1FF,0x00, -1):
	#	write_pot(i)
	#	time.sleep(0.005)