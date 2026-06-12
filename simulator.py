"""
To-Do:
    Task A: Change the code so it tracks three different trucks (DXB-001, DXB-002, DXB-003)
            simultaneously inside the same loop, instead of just one.

    Task B: Give each truck a different starting location in Dubai so they aren't driving
            stacked on top of each other.

    Task C: Add a new key-value pair to the payload called "speed". Use Python's built-in
            random module to make the speed fluctuate between 60 and 80 (km/h) each loop cycle.
"""

import time
import json
import random

# Coordinates --> near Downtown Dubai
vehicles = [
    {"vehicle_id": "DXB-TRUCK-001", "lat": 25.1972, "lng": 55.2744, "fuel": 100.0},
    {"vehicle_id": "DXB-TRUCK-002", "lat": 25.2048, "lng": 55.2708, "fuel": 100.0},
    {"vehicle_id": "DXB-TRUCK-003", "lat": 25.1224, "lng": 55.2301, "fuel": 100.0},
]

print("Starting IoT Vehicle Simulator... Press CTRL+C to stop.\n")

while True:
    for vehicle in vehicles:
        current_time = int(time.time())

        vehicle["lat"] += 0.0002
        vehicle["lng"] += 0.0003

        vehicle["fuel"] -= random.uniform(0.1, 0.3)
        vehicle["fuel"] = max(0, round(vehicle["fuel"], 2))

        vehicle.update({"speed": random.randint(60, 80), "timestamp": current_time})

        json_string = json.dumps(vehicle)
        print(json_string)

    print("-" * 50)
    time.sleep(3)
