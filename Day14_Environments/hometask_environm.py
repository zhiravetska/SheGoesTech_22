# TODO
# put the imports first

# create a function that returns a list of random dice throws
# it should have two parameters
# - number of dice in each throw, default 4
# - number of throws, default 100


# even better would be a another function to which you give the list of dice throws and it
# plots the histogram
# this function would have two parameters
# - the list of dice throws - no default
# - the name of the file to save the plot to - default - empty string
# if the file name is empty string, the plot should be shown on the screen

# use the first function to create a list of 1000 dice throws with 6 dice in each throw
# pass the result to 2nd function to plot the histogram and save it to a file
# BONUS: file name should have current date and time in it


# ideally you would then run them from main guard
# which means this file would be a module, that can be imported

import random
import matplotlib.pyplot as plt


def dice_throw(dice, throw):

    throw_list = []
    a = 0
    # i = 0
    for i in range(throw):
        dice_list = []
        for a in range(dice):

            if a <= dice:
                number = random.randint(1, 6)
                dice_list.append(number)
                a += 1
            # i += 1
        throw_list.append(dice_list)

    print(throw_list)
    return throw_list


dice_throw(4, 100)

# plot histogram of data


# def my_hist_graph(x, throw):

#     n_bins = throw
#     x = dice_throw
#     fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=4)
#     ax1.hist(x, n_bins, color='blue', edgecolor='black')
#     ax2.hist(x, n_bins, color2='red', edgecolor='black')
#     ax3.hist(x, n_bins, color3='green', edgecolor='black')
#     ax4.hist(x, n_bins, color4='yellow', edgecolor='black')
#     fig.suptitle('Histogram of Random Dice Throws')
#     ax.set_xlabel('Random Dice')
#     ax.set_ylabel('Trows')

#     plt.show()


# my_hist_graph(dice_throw, 100)

#x = [random.randint(0, 10) for _ in range(100)]

# def dice_throw(dice, throw):

#     throw_list = []
#     dice_list = []
#     a = 0
#     for i in range(dice):
#         number = random.randint(1, 6)
#         dice_list.append(number)
#         if a <= throw:
#             throw_list.append(dice_list)
#             a += 1
#     print(throw_list)


# dice_throw(4, 10)

# listoflists = []
# list = []
# for i in range(0, 10):
#     list.append(i)
#     if len(list) > 3:
#         list.remove(list[0])
#         listoflists.append((list, list[0]))
# print(listoflists)

# def roll():
#     print('The computer will now simulate the roll of a dice 100 times')
#     number = random.randint(1, 6)
#     print([number])


# roll()

# print([random.randint(1, 6) for _ in range(100)])
# def random_dice_throws(numdice, numthrow):
#     rdth[]

#     return rdth[]

# random_dice_throws(4, 100) # https://realpython.com/python-dice-roll/
