# 1a. Average value

# Write a program that prompts the user to enter numbers (float).


# The program shows the average value of all entered numbers after each entry.
# PS. 1a can do without a list

# 1b. The program shows both the average value of the numbers and ALL the numbers entered

# PS Exit the program  by entering "q"

# 1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 and of course still average.


# numbers = input("Input numbers: ")
# numbers_list = numbers.split(" ")
# print(numbers_list)
# numbers_list = [float(i) for i in numbers_list]
# print(numbers_list)
# # a = 0
# # for i in numbers_list:
# #     a = a + i
# # result = a / len(numbers_list)
# total = sum(numbers_list)
# av = total / len(numbers_list)
# print("Average is", av)

# # 2. Cubes

# The user enters the beginning (integer) and end number.

# The output is the entered numbers and their cubes

# For example: inputs 2 and 5 (two inputs)

# Output

# 2 cubed: 8
# 3 cubed: 27
# 4 cubed: 64
# 5 cubed: 125

# All cubes: [8,27,64,125]

# PS could theoretically do without a list, but with a list it will be more convenient

num1 = input("Enter the start number: ")
num2 = input("Enter the end number: ")
num1 = int(num1)
num2 = int(num2)
print(num1, num2)
myList = list(range(num1, num2, 1))
print(myList)
cubed = []
for cu in myList:
    cubed.append(cu**3)
print(cubed)

# 3. Reversed words

# The user enters a sentence.

# We output all the words of the sentence in a reverse form.
# - not the whole text reversed!!

# Example

# Alus kauss mans -> Sula ssuak snam
# notice how each word was reversed separately

# PS Split and join operations could be useful here.

# hometask for thursday
# Find and output the first 20
# (even better option to choose how many first primes we want)
# prime numbers in the form of a list i.e. [2,3,5,7,11, ...
# so remember we already know how to find a single prime number
# from previous exercise
# https://github.com/ValRCS/Python_SheGoesTech_22/blob/main/Day_4_Loops/day4_exercise_3.py
