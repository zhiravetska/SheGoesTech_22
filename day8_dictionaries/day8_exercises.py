# # 1. What's the frequency?

# Write a function: get_char_count(text) that receives a string and returns a dictionary with the number of single letter counts.

# get_char_count("hubba bubba") -> {'h': 1, 'u': 2, 'b': 5, 'a': 2, ' ': 1}

# # dictionary sequence doesn't matter and the whole alphabet doesn't have to be included

#  There may also be a solution with Counter from standard Python library but this is definitely not necessary, although it is very elegant smile

# IN PLACE - meaning we change the original dictionary


def get_char_count(text):
    new_dict = {}
    for i in text:
        my_count = text.count(i)
        new_dict[i] = my_count
    print(new_dict)
    return new_dict


def get_char_count(text):
    new_dict = {}
    for i in text:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    print(new_dict)
    return new_dict


get_char_count("hubba bubba")
get_char_count("I love you my darling")

# 2. Dictionary editor


# Write replace_dict_value(d, bad_val, good_val), which returns a dictionary with changed values

# The parameters of the function are the dictionary d to be processed and the values ​​bad_val to be changed to good_val

# clean_dict_value ({'a': 5, 'b': 6, 'c': 5}, 5, 10) -> {'a': 10, 'b': 6, 'c': 10}, because 5 was the value to be replaced

# def replace_dict_value(d, bad_val, good_val)

dictionary = {'a': 5, 'b': 6, 'c': 5}


def replace_dict_value(d, bad_val, good_val):
    clean_dict = {}
    for i in dictionary:
        if d[i] == bad_val:
            clean_dict[i] = good_val
        else:
            clean_dict[i] = d[i]
    print(clean_dict)
    return clean_dict


replace_dict_value(dictionary, 5, 10)


# # 3. Dictionary cleaner


# 3a. Write clean_dict_value(d, bad_val), which returns a cleaned dictionary without any keys with the value bad_val

# The parameters of the function are the dictionary d to be processed and the value bad_val to be disposed of together with its key.

# Example:

# clean_dict_value ({'a': 5, 'b': 6, 'c': 5}, 5) -> {'b': 6}, because 5 was a value for both a and c keys to get rid of.

# my_dict = {'a': 5, 'b': 6, 'c': 5}


# def clean_dict_value(d, bad_val):
#     clean_dict = {}
#     for i in my_dict:
#         if my_dict[i] != bad_val:
#             clean_dict[i] = my_dict[i]
#     print(clean_dict)
#     return clean_dict


# clean_dict_value(my_dict, 5)


# 3b Write clean_dict_values ​​(d, v_list), which returns a cleaned dictionary

# The parameters of the function are the dictionary d to be processed and the list of values ​​v_list to get rid of.

# clean_dict_values ​​({'a': 5, 'b': 6, 'c': 5, 'd':3}, [3,4,5]) -> {'b': 6} because 3 and 5 were in the list of values to delete.

# my_dict = {'a': 5, 'b': 6, 'c': 5, 'd': 3}
# v_list = [3, 5]


# def clean_dict_values(d, v_list):
#     clean_dict = {}
#     opp_dict = {}
#     for key, value in my_dict.items():
#         if value in v_list:
#             opp_dict[key] = value
#         else:
#             clean_dict[key] = value

#     print(clean_dict)
#     return clean_dict


# clean_dict_values(my_dict, v_list)


# PS. Remember we can use del d['a'] only if the key 'a' exists.

# !! When resizing a dictionary, we are not allowed to iterate at the same time!


# There are two options: either walk through the copy my_dict.copy.items(), or build a new dictionary.
# Dictionary comprehension would be one option.
