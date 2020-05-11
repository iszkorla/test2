import matplotlib.pyplot as plt

#input_values = [1, 2, 3, 4, 5]
#squares = [1, 4, 9, 16, 25]
#plt.plot(input_values, squares, linewidth=5)

# Set chart title and label axis
#plt.title("Square Numbers", fontsize=16)
#plt.xlabel("Value", fontsize=14)
#plt.ylabel("Square of Value", fontsize=14)

# Set the size of tick labels.
#plt.tick_Yparams(axis='both', labelsize=14)
#
# ABOVE BASIC PLOT
#

#
# BELOW SQUARES PLOT
#
#x_values = list(range(1, 1001))
#y_values = [x**2 for x in x_values]
#plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.hsv, edgecolor='none', s=60)

# Set chart title and label axis
#plt.title("Square Numbers", fontsize=24)
#plt.xlabel("Value", fontsize=14)
#plt.ylabel("Square of Value", fontsize=14)
#plt.axis([0, 1100, 1, 1100000])

# Set size of tick labels.
#plt.tick_params(axis='both', which='major', labelsize=14)

# Save plot to a file; Make sure to plt.savfig() before plt.show();
# if plt.show() happens first, a blank plot will be saved;
#plt.savefig('square_plot.png', bbox_inches='tight')
#plt.show()

from random import choice

class RandomWalk():
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction to go in that direction.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere;
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)



