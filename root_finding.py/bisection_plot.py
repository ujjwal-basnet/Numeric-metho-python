import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 4

# Create an array of x values for plotting
x = np.linspace(-2, 5, 100)

# Calculate the corresponding f(x) values
y = f(x)

# Plot the function
plt.figure(figsize=(8, 6))
plt.plot(x, y)

# Draw vertical lines at x = 1 and x = 3
plt.vlines(1, -5, 5, linestyles='dashed', colors='r', label='x = 1')
plt.vlines(3, -5, 5, linestyles='dashed', colors='g', label='x = 3')

# Add labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x) = x^2 - 4')
plt.legend()

# Show the plot
plt.show()