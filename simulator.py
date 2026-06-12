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
current_lat = 25.1972
current_lng = 55.2744
vehicle_id = "DXB-TRUCK-001"
fuel_level = 100.0

print("Starting IoT Vehicle Simulator... Press CTRL+C to stop.\n")

while True:
    current_lat += 0.0002
    current_lng += 0.0003

    fuel_level -= random.uniform(0.1, 0.3)
    fuel_level = max(0, round(fuel_level, 2))

    current_time = int(time.time())

    telemetry_payload = {
        "vehicle_id": vehicle_id,
        "lat": round(current_lat, 6),
        "lng": round(current_lng, 6),
        "fuel": fuel_level,
        "timestamp": current_time,
    }

    json_string = json.dumps(telemetry_payload)
    print(json_string)

    time.sleep(3)
