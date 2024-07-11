# Example main script integrating sensor, data processing, and cloud communication
from fire_sensor import FireSensor
from data_processing import DataProcessor
from cloud_communication import CloudClient

if __name__ == "__main__":
    sensor = FireSensor()
    processor = DataProcessor()
    client = CloudClient(api_key="your_api_key")

    while True:
        smoke_level = sensor.read_sensor_data()
        print(f"Smoke Level: {smoke_level}")

        if processor.detect_fire(smoke_level):
            print("Fire detected! Alerting...")
            data = {"smoke_level": smoke_level, "status": "fire_detected"}
            client.send_data(data)
        else:
            print("No fire detected.")

        time.sleep(5)  # Simulate real-time reading every 5 seconds
