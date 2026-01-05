import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. SETUP THE 3D GRID ---
# We create a box of space from -2 to 2 on all axes
x = np.linspace(-2, 2, 10)
y = np.linspace(-2, 2, 10)
z = np.linspace(0, 4, 8) # Z goes up from ground (0) to sky (4)

X, Y, Z = np.meshgrid(x, y, z)

# --- 2. DEFINE THE PHYSICS (THE VORTEX) ---
# We want a "Tornado" shape:
# A. ROTATION: Spirals around the Z-axis (-y, x)
# B. COMPRESSION: Gets tighter/faster as it goes UP (or down)
# C. LIFT: Flows upwards (+z)

# Distance from the center axis (Radius)
R = np.sqrt(X**2 + Y**2) + 0.1 # Add 0.1 to avoid division by zero

# -- The Equation of the Vortex --
# 1. Tangential Velocity (Spin): Faster near the center (Conservation of Angular Momentum)
Spin_Strength = 1.0
U_spin = -Y / R * Spin_Strength  # X-direction spin
V_spin =  X / R * Spin_Strength  # Y-direction spin

# 2. Radial Velocity (Implosion): Suction INWARDS towards the center
Implosion_Strength = 0.5
U_in = -X / R * Implosion_Strength
V_in = -Y / R * Implosion_Strength

# 3. Vertical Velocity (Lift): The "Anti-Gravity" push
# The flow moves FASTER as it gets tighter (Bernoulli Principle)
W_lift = 2.0 / R 

# -- COMBINE THEM --
# Total Vector (U, V, W)
U = U_spin + U_in
V = V_spin + V_in
W = W_lift

# --- 3. VISUALIZATION ---
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the vectors
# length=0.5 makes the arrows shorter so they don't overlap too much
ax.quiver(X, Y, Z, U, V, W, length=0.3, normalize=True, color='cyan', alpha=0.8)

# Add the "Central Axis" (The Zero Point)
ax.plot([0, 0], [0, 0], [0, 4], color='red', linewidth=3, label='Vacuum Core (Zero Point)')

# Styling
ax.set_facecolor('black')
ax.grid(False)
ax.set_axis_off() # Hide the box to make it look like space
ax.set_title("3D Hyperbolic Vortex (The Engine of Implosion)", color='white', size=15)
plt.legend()

plt.show()
