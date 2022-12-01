
import random


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
