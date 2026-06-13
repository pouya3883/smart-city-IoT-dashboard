import time
import random
import requests
# import json

# Coordinates --> near Downtown Dubai
vehicles = [
    {"vehicle_id": "DXB-TRUCK-001", "lat": 25.1972, "lng": 55.2744, "fuel": 100.0},
    {"vehicle_id": "DXB-TRUCK-002", "lat": 25.2048, "lng": 55.2708, "fuel": 100.0},
    {"vehicle_id": "DXB-TRUCK-003", "lat": 25.1224, "lng": 55.2301, "fuel": 100.0},
]

print("Starting IoT Vehicle Simulator... Press CTRL+C to stop.\n")

url = "http://127.0.0.1:8000/telemetry"

while True:
    for vehicle in vehicles:
        current_time = int(time.time())

        vehicle["lat"] += 0.0002
        vehicle["lat"] = round(vehicle["lat"], 4)
        vehicle["lng"] += 0.0003
        vehicle["lng"] = round(vehicle["lng"], 4)

        vehicle["fuel"] -= random.uniform(0.1, 0.3)
        vehicle["fuel"] = max(0, round(vehicle["fuel"], 2))

        vehicle.update({"speed": random.randint(60, 80), "timestamp": current_time})

        response = requests.post(url, json=vehicle)

        print(
            f"Broadcasted {vehicle['vehicle_id']} -> Server Response: {response.status_code}"
        )

    print("-" * 50)
    time.sleep(3)
