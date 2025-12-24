def split_route(distance_miles, step=100):
    points = []
    current = 0
    while current < distance_miles:
        points.append(current)
        current += step
    points.append(distance_miles)
    return points
