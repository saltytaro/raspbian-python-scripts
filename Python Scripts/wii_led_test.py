import RPi.GPIO as GPIO
import time, cwiid

LedPin = 11    # pin11

def setup():
  GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
  GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
  GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to turn on led

def blink():
  ledOn = False
  ledOnPrev = False

  while True:
    buttons = wii.state['buttons']

    if (buttons & cwiid.BTN_A) and ledOn == False:
      ledOn = True
      GPIO.output(LedPin, GPIO.HIGH)
      print 'LED on'
    elif not (buttons & cwiid.BTN_A) and ledOn == True:
      ledOn = False
      GPIO.output(LedPin, GPIO.LOW)
      print 'LED off'

    time.sleep(0.1)

def destroy():
  GPIO.output(LedPin, GPIO.LOW)   # led off
  GPIO.cleanup()                  # Release resource

if __name__ == '__main__':     # Program start from here
  print 'Press 1 + 2 on your Wii Remote now ...'
  time.sleep(1)
 
  # Connect to the Wii Remote. If it times out
  # then quit.
  try:
    wii=cwiid.Wiimote()
  except RuntimeError:
    print "Error opening wiimote connection"
    quit()
 
  print 'Wii Remote connected...\n'
    
  wii.rpt_mode = cwiid.RPT_BTN

  setup()
  try:
    blink()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()
