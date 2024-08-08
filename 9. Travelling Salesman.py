import itertools
import math

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def tsp_brute_force(cities):
    num_cities = len(cities)
    min_distance = float('inf')
    best_route = None

    # Generate all possible routes
    for route in itertools.permutations(range(num_cities)):
        route_distance = 0
        for i in range(num_cities - 1):
            route_distance += distance(cities[route[i]], cities[route[i+1]])
        route_distance += distance(cities[route[-1]], cities[route[0]])  # Add distance from last city back to first city

        if route_distance < min_distance:
            min_distance = route_distance
            best_route = route

    return best_route, min_distance

# Example usage:
cities = [(0, 0), (10, 0), (5, 5), (0, 10), (10, 10)]  # Define the cities
route, distance = tsp_brute_force(cities)
print("Best route:", route)
print("Total distance:", distance)
