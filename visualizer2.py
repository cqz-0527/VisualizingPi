import random
import math
import matplotlib.pyplot as plt

# NOTE: this is the entire circle, notice how we go from -1 to 1 in both the x and y axes. 

def visualize_pi(n):
    points_in_circle = []
    points_outside_circle = []

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance_from_origin = math.sqrt(x**2 + y**2)

        if distance_from_origin <= 1:
            points_in_circle.append((x, y))
        else:
            points_outside_circle.append((x, y))

    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Plot circle
    circle = plt.Circle((0, 0), 1, fill=False, color='r')
    ax.add_artist(circle)

    # Plot points
    in_circle_x, in_circle_y = zip(*points_in_circle)
    outside_circle_x, outside_circle_y = zip(*points_outside_circle)
    ax.scatter(in_circle_x, in_circle_y, color='red', label='Inside Circle')
    ax.scatter(outside_circle_x, outside_circle_y, color='blue', label='Outside Circle')

    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect('equal')
    ax.set_title('Point Distribution')
    ax.legend()

    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

points = int(input("Enter the number of points: "))
visualize_pi(points)
