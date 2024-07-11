class DataProcessor:
    def __init__(self):
        self.fire_threshold = 70  
    def detect_fire(self, smoke_level):
        if smoke_level > self.fire_threshold:
            return True
        else:
            return False

if __name__ == "__main__":
    processor = DataProcessor()
    smoke_level = 75  # Example smoke level read from sensor
    if processor.detect_fire(smoke_level):
        print("Fire detected! Alerting...")
        # Code to send alert to cloud or connected devices
    else:
        print("No fire detected.")
