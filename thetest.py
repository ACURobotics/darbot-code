import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 2000000

def write_pot(input):
	msb = input >> 8
	lsb = input & 0xFF
	spi.xfer([msb,lsb])
try:
	while True:
		#7V f/b
		write_pot(0x1050)
		#6V l/r
		write_pot(0x00B9)

		time.sleep(4)

		#6V f/b
		write_pot(0x10B9)
		#7V l/r
		write_pot(0x0050)

		time.sleep(1)

except KeyboardInterrupt:
	write_pot(0x00B9)
	write_pot(0x10B9)

