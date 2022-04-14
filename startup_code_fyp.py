# INSTRUCTIONS:

# CLICK THE GREEN PLAY BUTTON TO START (AT TOP OF THIS WINDOW)
# PRESS THE GREEN DEVICE BUTTON AS MANY TIMES TO TAKE PICTURES
# CLICK THE RED STOP BUTTON TO STOP
# DEVICE WILL BE SAFE TO SHUT DOWN AFTER THE PROGRAMME STOPS

# ----------------------------------------------------------

# For normal functions
import RPi.GPIO as GPIO
from gpiozero import TonalBuzzer, LED, Button
from gpiozero.tones import Tone
#from RPLCD import i2c
from picamera import PiCamera
from signal import pause
from datetime import datetime
from time import sleep
#from subprocess import check_output

# Assign GPIO pins
buzzer = TonalBuzzer(22) # Start up buzzer
torch = LED(21) # Light source LED
led = LED(4) # Start up LED
cam_button = Button(27) # Button to launch camera
#exit_button = Button(17) # Button to exit program
camera = PiCamera()

# # Assign LCD constants
# lcdmode = 'i2c'
# cols = 16
# rows = 2
# charmap = 'A00'
# i2c_expander = 'PCF8574'
# 
# address = 0x27
# port = 1
# 
# lcd = i2c.CharLCD(i2c_expander, address, port=port, charmap=charmap, cols=cols, rows=rows)
# 
# # Start up light
# lcd.close(clear=True)
# lcd.write_string('Starting...')

buzzer.play(Tone("C4")) #Play starting arpeggio
sleep(0.5)
buzzer.play(Tone("E4")) #Play starting arpeggio
sleep(0.5)
buzzer.play(Tone("G4")) #Play starting arpeggio
sleep(0.5)
buzzer.play(Tone("C5")) #Play starting arpeggio
sleep(0.5)
buzzer.stop()

# lcd.close(clear=True)

# Camera action
camera.resolution = (2592, 1944) # Max resolution (3280, 2464) / (2592, 1944) / (640, 480)
camera.framerate = 15 # Frame rate has to be activated for max res to work
camera.brightness = 55

# Button functions
def capture():
    timestamp = datetime.now().isoformat()
    camera.capture('/home/pi/Desktop/Capture Images/%s.png' % timestamp) # Captures image with time stamp

# def stop_code():
#     lcd.close(clear=True)
#     lcd.write_string('Stopping...')
#     lcd.close(clear=True)
#     buzzer.play(Tone("E4"))
#     sleep(1)
#     buzzer.stop()
#     exit()

while True:
    
    #exit_button.when_pressed = stop_code
    
#     lcd_line_1 = "Press green button to start"
#     lcd.write_string(lcd_line_1)
    
    cam_button.wait_for_press() # Code will stop until button is pressed
#    lcd.close(clear=True)

    # When cam_button is pressed
#    lcd.write_string("Capturing photos...")
    torch.on()
    camera.start_preview()
    
    buzzer.play(Tone("C4"))
            
    for i in range(1): # Captures 1 image only
        
        # Adjust time here
        sleep(10)
        
        buzzer.play(Tone("E4"))
        sleep(0.5)
        buzzer.play(Tone("G4"))
        sleep(0.5)
        capture()
            
    camera.stop_preview()
#    lcd.close(clear=True)

    buzzer.stop() # Stop playing
    torch.off()
#    lcd.write_string("Done")
#    lcd.close(clear=True)






