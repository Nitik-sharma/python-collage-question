import cv2
import numpy as np
import matplotlib.pyplot as plt

# Generate some noisy data points along a line
np.random.seed(42)
X = np.linspace(0, 50, 50)
Y = 2*X + 1 + np.random.normal(0, 5, size=X.shape)  # Line y=2x+1 with noise
points = np.column_stack((X, Y))

# Convert to int32 for OpenCV
points = points.astype(np.int32)

# Fit line using RANSAC
[vx, vy, x0, y0] = cv2.fitLine(points, cv2.DIST_L2, 0, 0.01, 0.01)

# Generate line points for plotting
line_x = np.array([min(X), max(X)])
line_y = (vy/vx) * (line_x - x0) + y0

# Plot the noisy points and fitted line
plt.scatter(X, Y, label="Data Points")
plt.plot(line_x, line_y, color="red", label="RANSAC Fitted Line")
plt.legend()
plt.show()
