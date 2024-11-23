import RPi.GPIO as GPIO
from time import time, sleep
from urllib.request import urlopen
import sys

WRITE_API = "YJIG6Y59YC4XR7ZL"  # Replace your ThingSpeak API key here
BASE_URL = "https://api.thingspeak.com/update?api_key={}".format(WRITE_API)

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
TRIG_PIN = 23
ECHO_PIN = 24
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

SensorPrevSec = 0
SensorInterval = 2  # 2 seconds
ThingSpeakPrevSec = 0
ThingSpeakInterval = 20  # 20 seconds

max_distance = 100.0  # Maximum distance in centimeters

def calculate_distance_percentage(distance):
    if distance > max_distance:
        return 0.0
    else:
        return ((max_distance - distance) / max_distance) * 100.0

try:
    while True:

        if time() - SensorPrevSec > SensorInterval:
            SensorPrevSec = time()

            GPIO.output(TRIG_PIN, False)
            sleep(0.5)

            GPIO.output(TRIG_PIN, True)
            sleep(0.00001)
            GPIO.output(TRIG_PIN, False)

            while GPIO.input(ECHO_PIN) == 0:
                pulse_start = time()

            while GPIO.input(ECHO_PIN) == 1:
                pulse_end = time()

            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            distance = round(distance, 2)
            print("Distance:", distance, "cm")
            distance_percentage = calculate_distance_percentage(distance)
            print("Distance Percentage:", distance_percentage, "%")

        if time() - ThingSpeakPrevSec > ThingSpeakInterval:
            ThingSpeakPrevSec = time()

            thingspeakHttp = BASE_URL + "&field1={:.2f}".format(distance_percentage)
            #print(thingspeakHttp)

            conn = urlopen(thingspeakHttp)
            print("Response: {}".format(conn.read()))
            conn.close()

        sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    conn.close()