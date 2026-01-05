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


# --- ADDING THE VORTEX SPIN (MAGNETIC COMPONENT) ---
# We want the field to not just point OUT, but also SWIRL around the center.
# The 'Spin' force is perpendicular to the radial vector.

# Calculate the distance from center (0,1)
Rx = X - 0
Ry = Y - 1
Dist = np.sqrt(Rx**2 + Ry**2) + 0.1

# Define a Spin Vector (Perpendicular to Radius)
# (-y, x) creates a counter-clockwise rotation
SpinX = -Ry / Dist
SpinY = Rx / Dist

# How strong is the spin?
Spin_Strength = 3.0  # Try changing this!

# --- TOTAL FIELD WITH TORSION ---
# New Field = Electric Push (Radial) + Magnetic Spin (Tangential)
Ex_Torsion = Ex_total + (Spin_Strength * SpinX)
Ey_Torsion = Ey_total + (Spin_Strength * SpinY)

# --- VISUALIZE ---
fig, ax = plt.subplots(figsize=(10, 8))
# Plot the new swirling field
ax.streamplot(X, Y, Ex_Torsion, Ey_Torsion, color='cyan', density=2.0, arrowsize=1.5)

plt.title("The Plasma Vortex: Electric Field + Magnetic Spin", color='white')
plt.show()
