from routing.constants import MAX_RANGE_MILES, MPG, RESERVE_MILES
from routing.data import load_fuel_prices

PRICE_COLUMN = "retail price"

def select_fuel_stops(distance_miles):
    fuel_df = load_fuel_prices()

    remaining_range = MAX_RANGE_MILES
    current_mile = 0
    fuel_stops = []
    total_cost = 0.0

    while current_mile < distance_miles:
        remaining_range -= RESERVE_MILES

        if remaining_range <= 0:
            cheapest = fuel_df.loc[fuel_df[PRICE_COLUMN].idxmin()]

            gallons_needed = MAX_RANGE_MILES / MPG
            cost = gallons_needed * float(cheapest[PRICE_COLUMN])

            fuel_stops.append({
                "location": cheapest.get("city", "unknown"),
                "state": cheapest.get("state", ""),
                "price_per_gallon": float(cheapest[PRICE_COLUMN]),
                "gallons": gallons_needed
            })

            total_cost += cost
            remaining_range = MAX_RANGE_MILES

        current_mile += RESERVE_MILES

    return fuel_stops, round(total_cost, 2)
