import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Ensure GUI backend works on Windows
import matplotlib.pyplot as plt

# --- Data ---
X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
Y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

# --- Linear Regression Coefficients ---
b = np.cov(X, Y)[0, 1] / np.var(X)  # slope
a = np.mean(Y) - b * np.mean(X)     # intercept

print(f"Slope (b) = {b:.3f}")
print(f"Intercept (a) = {a:.3f}")

# --- Predicted Y values ---
Y_pred = a + b * X

# --- Plotting ---
plt.scatter(X, Y, color='blue', label='Data Points')
plt.plot(X, Y_pred, color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression Fit')
plt.legend()

# --- Save plot to file ---
plt.savefig('linear_regression_plot.png')
print("Plot saved as 'linear_regression_plot.png'")

# --- Show plot (optional) ---
plt.show()
