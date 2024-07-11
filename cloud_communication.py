# Example code for cloud communication (simplified)
import requests
import json

class CloudClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.example.com/fireguard"

    def send_data(self, data):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        endpoint = f"{self.base_url}/data"
        try:
            response = requests.post(endpoint, headers=headers, json=data)
            if response.status_code == 200:
                print("Data sent successfully to cloud.")
            else:
                print(f"Failed to send data. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error sending data to cloud: {str(e)}")

# Example usage:
if __name__ == "__main__":
    client = CloudClient(api_key="your_api_key")
    data = {"smoke_level": 75, "status": "fire_detected"}
    client.send_data(data)
