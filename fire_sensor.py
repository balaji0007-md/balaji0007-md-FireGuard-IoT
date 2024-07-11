import time
import random

class FireSensor:
    def __init__(self):
        self.smoke_threshold = 50  #Example threshold for smoke level

    def read_sensor_data(self):
        smoke_level = random.randint(0, 100)
        return smoke_level

if __name__ == "__main__":
    sensor = FireSensor()
    while True:
        smoke_level = sensor.read_sensor_data()
        print(f"Smoke Level: {smoke_level}")
        time.sleep(5)
