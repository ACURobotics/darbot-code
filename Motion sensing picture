#from gpiozero import MotionSensor
#import time
#import picamera import Picamera

#pir = MotionSensor(4)

#with picamera.PiCamera() as camera:
    #camera.resolution = (1024, 768)
    #camera.start_preview()
    
    #camera.exposure_compensation = 2
    #camera.exposure_mode = 'spotlight'
    #camera.meter_mode = 'matrix'
    #camera.image_effect = 'gpen'
    # Give the camera some time to adjust to conditions
    #while True:
    #if pir.motion_detected:
        #camera.start_preview()
        #time.sleep(2)
        
        #a = 'Darbot_Picture'
        #b = '.jpeg'
        #c = 0
        #d = str(c)
        #c = c+1
        #ruby = a + b + d
        
        #camera.capture(ruby)
        #camera.stop_preview()
        
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor

while True:
       i=GPIO.input(11)
       if i==0:                 #When output from motion sensor is LOW
             print "No intruders",i
             
             time.sleep(0.1)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             
             time.sleep(0.1)
