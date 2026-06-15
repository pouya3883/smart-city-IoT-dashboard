const map = L.map("map").setView([25.1972, 55.2744], 12);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution: "© OpenStreetMap contributors",
}).addTo(map);

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
