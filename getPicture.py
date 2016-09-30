import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    #camera.exposure_compensation = 2
    #camera.exposure_mode = 'spotlight'
    #camera.meter_mode = 'matrix'
    #camera.image_effect = 'gpen'
    # Give the camera some time to adjust to conditions
    time.sleep(2)
    camera.capture('myFace.jpg')
    camera.stop_preview()
