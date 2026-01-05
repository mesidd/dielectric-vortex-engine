import numpy as np
import matplotlib.pyplot as plt

# --- THE BIEFELD-BROWN SETUP ---
# Define the grid of space
Y, X = np.mgrid[-3:3:100j, -3:3:100j]

# --- DEFINE ELECTRODES ---
# Electrode 1: The "Sharp" Point (Positive Anode) at location (0, 1)
# It is a single intense point source.
Ex1 = X - 0
Ey1 = Y - 1
R1 = np.sqrt(Ex1**2 + Ey1**2)
# Inverse square law for field strength (very intense close up)
E1_strength = 5.0 / (R1**2 + 0.1)

# Electrode 2: The "Flat" Plate (Negative Cathode) at line y = -1
# It is a spread out, weaker pull downwards across the whole bottom.
Ey2 = Y - (-1)
# Field is uniform downwards towards the plate
E2_strength = -2.0 * (Ey2 / (np.abs(Ey2) + 0.1)) 

# --- TOTAL FIELD (Superposition) ---
# The sharp point pushes out, the flat plate pulls down.
Ex_total = E1_strength * (Ex1/R1) 
Ey_total = E1_strength * (Ey1/R1) + E2_strength
# Calculate Field Density (Magnitude) to visualize pressure
Density = np.sqrt(Ex_total**2 + Ey_total**2)

# --- VISUALIZATION ---
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the field density as a heat map (Warmer color = Higher Pressure)
heatmap = ax.contourf(X, Y, Density, levels=50, cmap='inferno')
plt.colorbar(heatmap, label='Electric Field Density (Ether Pressure)')

# Plot the field lines showing direction of flow
# Notice how they crowd around the top point!
ax.streamplot(X, Y, Ex_total, Ey_total, color='cyan', density=1.5, linewidth=1, arrowsize=1.5)

# Draw the physical electrodes
circle = plt.Circle((0, 1), 0.1, color='red', label='Sharp Anode (+)')
plate = plt.Rectangle((-3, -1.1), 6, 0.2, color='blue', label='Flat Cathode (-)')
ax.add_patch(circle)
ax.add_patch(plate)

ax.set_facecolor('black')
plt.title("Asymmetrical Capacitor Field (The Thrust Mechanic)", color='white')
plt.legend(loc='upper right')
plt.show()
