import RPi.GPIO as GPIO
import time
from RPLCD.i2c import CharLCD

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# SR04 Pins
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# LEDs & Buzzer
LED_GREEN = 17
LED_YELLOW = 27
LED_RED = 22
BUZZER = 25
BUTTON = 18

for pin in [LED_GREEN, LED_YELLOW, LED_RED, BUZZER]:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# LCD Setup
lcd = CharLCD('PCF8574', 0x27)
lcd.clear()

buzzer_muted = False
last_btn_state = 1

def get_distance():
    GPIO.output(TRIG, False)
    time.sleep(0.000002)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO) == 0:
        start_time = time.time()
    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    elapsed = stop_time - start_time
    return (elapsed * 34300) / 2

try:
    while True:
        # Button debounce/mute logic
        btn_state = GPIO.input(BUTTON)
        if btn_state == 0 and last_btn_state == 1:
            buzzer_muted = not buzzer_muted
            time.sleep(0.2)
        last_btn_state = btn_state

        dist = get_distance()
        
        # Clear LEDs and Buzzer
        GPIO.output(LED_GREEN, False)
        GPIO.output(LED_YELLOW, False)
        GPIO.output(LED_RED, False)
        GPIO.output(BUZZER, False)

        # Update LCD
        lcd.clear()
        lcd.write_string(f"Dist: {dist:.1f} cm")
        lcd.cursor_pos = (1, 0)
        status = "SAFE" if dist > 30 else ("CAUTION" if dist > 10 else "DANGER")
        lcd.write_string(f"Status: {status}")

        # Control outputs based on distance
        if dist > 30:
            GPIO.output(LED_GREEN, True)
        elif dist > 10:
            GPIO.output(LED_YELLOW, True)
        else:
            GPIO.output(LED_RED, True)
            if not buzzer_muted:
                GPIO.output(BUZZER, True)
                time.sleep(0.1)
                GPIO.output(BUZZER, False)

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    lcd.clear()
