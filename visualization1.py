import random
import math
import matplotlib.pyplot as plt

def estimate_pi(n):
    num_points_in_circle = 0
    approximations = []  # To store intermediate approximations

    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance_from_origin = math.sqrt(x**2 + y**2)
        if distance_from_origin <= 1:
            num_points_in_circle += 1
        approximation = 4 * num_points_in_circle / (i + 1)
        approximations.append(approximation)

    return approximations

points = int(input("Enter the number of points: "))
approximations = estimate_pi(points)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(range(1, points + 1), approximations, label=' Approximation')
plt.axhline(y=math.pi, color='r', linestyle='--', label='Actual Pi')
plt.xlabel('Number of Points')
plt.ylabel('Approximation of Pi')
plt.title('Visualizing Pi')
plt.legend()
plt.grid(True)
plt.show()
