import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 14, 7]

# Create the plot
plt.plot(x, y, label='Line', color='blue', marker='o')

# Add title and labels
plt.title('Simple Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Show legend
plt.legend()

# Display the plot
plt.show()
