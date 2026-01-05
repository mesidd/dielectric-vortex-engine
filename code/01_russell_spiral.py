import numpy as np
import matplotlib.pyplot as plt

# --- THE RUSSELL PARAMETERS ---
# We model matter as a centripetal spiral (winding inwards).

# T is time/rotation angle. The higher the number, the more winds.
t = np.linspace(0, 20 * np.pi, 5000)

# The 'Cone' angle. How fast does it compress towards the center?
# A smaller number here means a tighter compression.
compression_factor = 0.1

# --- THE GEOMETRY OF IMPLOSION ---
# As 't' increases, the radius gets smaller (Implosion).
radius = np.exp(-compression_factor * t)

# Standard parametric equations for a 3D spiral
x = radius * np.cos(t)
y = radius * np.sin(t)
# The 'z' height also compresses towards zero
z = -np.exp(-compression_factor * t) + 1 

# --- VISUALIZATION ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the spiral path of light becoming matter
ax.plot(x, y, z, color='cyan', linewidth=1, alpha=0.8, label='Light Winding Up')

# Plot the "Zero Point" center (The resulting 'Atom')
ax.scatter([0], [0], [1], color='red', s=100, label='Zero Point (Matter Formed)')

# Styling to make it look like space
ax.set_facecolor('black')
ax.grid(False)
ax.set_axis_off()
plt.title("The Geometry of Optical Matter (Centripetal Vortex)", color='white')
plt.legend()
plt.show()
