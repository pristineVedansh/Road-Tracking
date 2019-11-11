import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import RPi.GPIO as GPIO

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

# Raspberry Pi Pin Config:
lcd_rs = digitalio.DigitalInOut(board.D22)
lcd_en = digitalio.DigitalInOut(board.D5)
lcd_d7 = digitalio.DigitalInOut(board.D26)
lcd_d6 = digitalio.DigitalInOut(board.D19)
lcd_d5 = digitalio.DigitalInOut(board.D13)
lcd_d4 = digitalio.DigitalInOut(board.D6)
lcd_backlight = digitalio.DigitalInOut(board.D4)

# Initialise the lcd class
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

try:
    GPIO.setmode(GPIO.BCM)

    PIN_TRIGGER = 23
    PIN_ECHO = 24

    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    time.sleep(2)

    GPIO.output(PIN_TRIGGER, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    while GPIO.input(PIN_ECHO)==0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO)==1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)

    lcd.backlight = True

    lcd.message = distance

finally:
      GPIO.cleanup()



