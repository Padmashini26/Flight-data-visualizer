# visualize_flight_data.py

import pandas as pd
import matplotlib.pyplot as plt

# Load flight data
df = pd.read_csv("flight_data.csv")

# Plot Altitude over Time
plt.figure(figsize=(10, 5))
plt.plot(df['Time (min)'], df['Altitude (m)'], label='Altitude (m)')
plt.xlabel('Time (min)')
plt.ylabel('Altitude (m)')
plt.title('Flight Altitude Over Time')
plt.legend()
plt.grid(True)
plt.savefig("altitude_plot.png")

# Plot Speed over Time
plt.figure(figsize=(10, 5))
plt.plot(df['Time (min)'], df['Speed (km/h)'], color='orange', label='Speed (km/h)')
plt.xlabel('Time (min)')
plt.ylabel('Speed (km/h)')
plt.title('Flight Speed Over Time')
plt.legend()
plt.grid(True)
plt.savefig("speed_plot.png")

# Plot Pressure over Time
plt.figure(figsize=(10, 5))
plt.plot(df['Time (min)'], df['Pressure (hPa)'], color='green', label='Pressure (hPa)')
plt.xlabel('Time (min)')
plt.ylabel('Pressure (hPa)')
plt.title('Cabin Pressure Over Time')
plt.legend()
plt.grid(True)
plt.savefig("pressure_plot.png")

print("Plots saved as PNG files.")
