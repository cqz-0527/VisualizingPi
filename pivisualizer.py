
import random
import math
# Notes for the Pi visualizer
#
# Consider the areas of a circle with radius s that is inscribed in a square with side length 2 * s 
#
# Area of circle = pi * (s/2)^2 = (pi * s^2)/4
# Area of square = (2 * s)^2

def estimate_pi(n): 
# as n gets bigger, the closer our result is to pi. 
    num_points_in_circle = 0
    num_points_in_total = 0 
    for _ in range(n): 
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        # calculate distance from origin
        # if distance < 1, point is within circle
        # if distance > 1, point is outside circle
        distance_from_origin = math.sqrt(x**2 + y**2)
        if distance_from_origin <= 1: 
            num_points_in_circle += 1 
        num_points_in_total += 1 # keep a running total

    return 4 * num_points_in_circle / num_points_in_total
points = int(input("Enter the number of points: "))
actual_pi = math.pi
estimated_pi = estimate_pi(points)
print(estimated_pi)
print("Estimated pi:", estimated_pi)
print("Actual pi:", actual_pi)
percent_error = (abs(estimated_pi - actual_pi) / actual_pi) * 100
print("Percent error (in %): ", percent_error)
    
