import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to update the plot in each frame
def update(frame):
    # Clear the previous frame
    plt.clf()

    # Create some data for the plot (you can replace this with your own data)
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x + frame * 0.1)

    # Plot the data
    plt.plot(x, y, label='Animated Line')
    plt.title('Animating Line Plot')
    plt.legend()

# Create a figure
fig, ax = plt.subplots()

# Set the number of frames
num_frames = 100

# Create the animation
animation = FuncAnimation(fig, update, frames=num_frames, interval=50)

# Show the animation
plt.show()
