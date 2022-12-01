# TODO
# 1. plot a graph of x and y
# x would be values from -10 to 10 (21 values)
# y would be the cube of x + 5

# you could use a different library than matplotlib but it is the most popular one
# will will explore other ones later on in the course

import random
import matplotlib.pyplot as plt
# x = [random.randint(0, 10) for _ in range(100)]

# # plot histogram of data
# fig, ax = plt.subplots()
# ax.hist(x, bins=11, color='blue', edgecolor='black')
# fig.suptitle('Histogram of Random Data')
# ax.set_xlabel('Value')
# ax.set_ylabel('Frequency')
# plt.show()

plt.style.use('_mpl-gallery')

x = list(range(-10, 11))
y = [(n+5)**3 for n in x]
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)
plt.show()


# create a function that returns a list of random dice throws
# - number of dice, default 4
#  - number of throws, default 100
#  use the function to create a list of 100 dice throws with 6 dice in each trow
#  plot the histogram of the results
#  save the plot into a file called dice.png
# ..............
