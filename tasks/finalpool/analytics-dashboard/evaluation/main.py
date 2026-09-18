import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, 100)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label='Noisy sine wave')
plt.title('Signal Processing Demo')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.savefig('signal_plot.png')
plt.close()

print('Plot saved as signal_plot.png')