const map = L.map("map").setView([25.1972, 55.2744], 12);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution: "© OpenStreetMap contributors",
}).addTo(map);

const routeBlueprints = {
  "DXB-TRUCK-001": {
    color: "blue",
    coords: [
      [25.0765, 55.1504],
      [25.0932, 55.1645],
      [25.1154, 55.1901],
      [25.1412, 55.2188],
      [25.1685, 55.2455],
      [25.1972, 55.2744],
    ],
  },
  "DXB-TRUCK-002": {
    color: "black",
    coords: [
      [25.132, 55.2612],
      [25.1544, 55.275],
      [25.1788, 55.2905],
      [25.1911, 55.3022],
      [25.2048, 55.2708],
    ],
  },
  "DXB-TRUCK-003": {
    color: "green",
    coords: [
      [25.1102, 55.214],
      [25.1155, 55.221],
      [25.1201, 55.2265],
      [25.1224, 55.2301],
    ],
  },
};

Object.keys(routeBlueprints).forEach((truckId) => {
  const routeInfo = routeBlueprints[truckId];
  L.polyline(routeInfo.coords, {
    color: routeInfo.color,
    weight: 4,
    opacity: 0.6,
    dashArray: "5, 10",
  }).addTo(map);
});

let vehicleMarkers = {};

async function updateFleetPositions() {
  try {
    const response = await fetch("http://127.0.0.1:8000/vehicles/latest");
    const vehicles = await response.json();

    vehicles.forEach((truck) => {
      const { vehicle_id, lat, lng, fuel, speed } = truck;

      const popupText = `
                        <b>ID:</b> ${vehicle_id}<br>
                        <b>Speed:</b> ${speed}<br>
                        <b>Fuel:</b> ${fuel}%
                    `;

      if (vehicleMarkers[vehicle_id]) {
        vehicleMarkers[vehicle_id].setLatLng([lat, lng]);
        vehicleMarkers[vehicle_id].getPopup().setContent(popupText);
      } else {
        const marker = L.marker([lat, lng]).addTo(map).bindPopup(popupText);
        vehicleMarkers[vehicle_id] = marker;
      }
    });
  } catch (error) {
    console.error("Error communicating with data ingestion API:", error);
  }
}

updateFleetPositions();

setInterval(updateFleetPositions, 3000);
