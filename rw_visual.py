import time
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
# Make a random walk, and plot the points.
while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=10)
    plt.show()
    time.sleep(7)

    keep_running = input("Make another walk?  (y/n): ")
    if keep_running == 'n':
         break
