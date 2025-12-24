from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def health(request):
    return Response({"status": "ok"})

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from routing.services import get_route
from routing.fuel_optimizer import select_fuel_stops

@api_view(['GET'])
def health(request):
    return Response({"status": "ok"})


@api_view(['POST'])
def route_with_fuel(request):
    start = request.data.get("start")
    end = request.data.get("end")

    if not start or not end:
        return Response(
            {"error": "start and end are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Hardcoded coordinates
    start_coords = [-118.2437, 34.0522]  # Los Angeles
    end_coords = [-74.0060, 40.7128]     # New York

    route_data = get_route(start_coords, end_coords)
    route_summary = route_data["routes"][0]["summary"]
    distance_miles = route_summary["distance"] / 1609.34

    fuel_stops, total_cost = select_fuel_stops(distance_miles)

    return Response({
        "distance_miles": round(distance_miles, 2),
        "fuel_stops": fuel_stops,
        "total_fuel_cost": total_cost
    })
