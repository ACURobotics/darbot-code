""""Class-ified" Robot code from Tanner Marlar's 'thetest.py'.

by Darby Hewitt 9/14/2016
"""
import spidev


class Robot(object):
    """This is the base Robot class.

    All subsequently defined darbot classes
    will inherit properties of this class.

    Requires: spidev
    """

    def __init__(self):
        """Initialize robot.

        Mainly, this prepares the spi interface for
        writing to the wheelchair controller;
        also, the DOFs are initialized to be still
        """
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 2000000

        self.setFB(0)
        self.setLR(0)

    def _writePot(self, input):
        """Write specified value to digital pot controlling DOFs.

        Helper function to control the digital potentiometer
        which governs the two degrees of motion for the robot
        """
        msb = input >> 8
        lsb = input & 0xFF
        self.spi.xfer([msb, lsb])

    def setFB(self, value):
        """Set the forward/backward motion."""
        # value is an integer range from -3 to 3
        if(value == 3):
            self._writePot(0x1050)  # writes 7V to LR
        elif(value == 2):
            self._writePot(0x1075)  # writes ~6.6V to LR
        elif(value == 1):
            self._writePot(0x1098)  # writes ~6.3V to LR
        elif(value == 0):
            self._writePot(0x10B9)  # writes 6V to LR
        elif(value == -1):
            self._writePot(0x10CC)  # writes ~5.7V to LR
        elif(value == -2):
            self._writePot(0x10DE)  # writes ~5.4V to LR
        elif(value == -3):
            self._writePot(0x10EF)  # writes 5V to FB
        else:
            self._writePot(0x10B9)  # writes 6V to LR

    def setLR(self, value):
        """Set the left/right motion."""
        # value is an integer range from -3 to 3
        if(value == 3):
            self._writePot(0x0050)  # writes 7V to LR
        elif(value == 2):
            self._writePot(0x0075)  # writes ~6.6V to LR
        elif(value == 1):
            self._writePot(0x0098)  # writes ~6.3V to LR
        elif(value == 0):
            self._writePot(0x00B9)  # writes 6V to LR
        elif(value == -1):
            self._writePot(0x00CC)  # writes ~5.7V to LR
        elif(value == -2):
            self._writePot(0x00DE)  # writes ~5.4V to LR
        elif(value == -3):
            self._writePot(0x00EF)  # writes 5V to FB
        else:
            self._writePot(0x00B9)  # writes 6V to LR

    def __del__(self):
        """Stop the chair before wiping Robot."""
        # set both channels to 0; this stops the chair
        self.setLR(0)
        self.setFB(0)

if __name__ == "__main__":
    # do a little dance to prove it works
    import time
    darbot = Robot()

    while True:
        for val in range(1, 4):     # range(1, 4) == [1, 2, 3]
            darbot.setFB(val)
            time.sleep(2)
            darbot.setFB(0)
            time.sleep(2)
            darbot.setFB(-val)
            time.sleep(2)
            darbot.setFB(0)
            time.sleep(2)

            darbot.setLR(val)
            time.sleep(2)
            darbot.setLR(0)
            time.sleep(2)
            darbot.setLR(-val)
            time.sleep(2)
            darbot.setLR(0)
            time.sleep(2)
