import requests
from django.conf import settings

ORS_URL = "https://api.openrouteservice.org/v2/directions/driving-car"

def get_route(start_coords, end_coords):
    headers = {
        "Authorization": settings.ORS_API_KEY,
        "Content-Type": "application/json",
    }

    payload = {
        "coordinates": [start_coords, end_coords]
    }

    response = requests.post(
        ORS_URL,
        json=payload,
        headers=headers,
        timeout=10
    )
    response.raise_for_status()
    return response.json()
