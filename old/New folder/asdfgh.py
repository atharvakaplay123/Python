import matplotlib.pyplot as plt
import numpy as np

# Generate Fibonacci series up to n terms
n = 10
fib_series = [0, 1]  # Initialize the Fibonacci series with the first two terms
if n <= 2:
    fib_series = fib_series[:n]  # Return the series if n is 1 or 2
else:
    for _ in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]  # Compute the next Fibonacci term
        fib_series.append(next_term)  # Add the next term to the series

# Calculate the coordinates of points for the Fibonacci spiral
theta = np.linspace(0, 2*np.pi, len(fib_series))  # Generate angles from 0 to 2*pi
radii = np.sqrt(fib_series)  # Use the square root of Fibonacci numbers as radii
x = radii * np.cos(theta)  # Calculate x-coordinates
y = radii * np.sin(theta)  # Calculate y-coordinates

# Plotting the Fibonacci spiral
plt.figure(figsize=(6, 6))
plt.plot(x, y, marker='o', linestyle='-', color='blue')
plt.title('Fibonacci Spiral')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.grid(True)
plt.show()
