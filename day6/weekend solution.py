# write a program that asks for two text inputs s1 and s2
# you can use better names than s1 and s2

# then checks if all the characters in first string are in second string
# if they are, print All character counts in the second string
# if not, print Not all characters are in the second string
# example
# s1 = "abc"
# s2 = "abracadabra"
# output: a 5, b 2, c 1, d 1, r 2  # so do not print the empty ones

# example two
# s1 = "abc"
# s2 = "def"
# output: Not all characters are in the second string

# text1 = input("Print the first text: ")
# text2 = input("Print the second text: ")
# j = 0
# for let1 in text1:
#     let2 = text2[j]
#     if let1 == let2:
#         j += 1
#     else:
#         print("Not all characters are in the second string")
# print("All characters count in the second string")

text1 = input("Print the first text: ")
text2 = input("Print the second text: ")
a = 0
# not sure this variable is necessary in this code
b = 0
for let1 in text1:
    if let1 in text2:
        #  the same with a variable ))
        a += 1
    else:
        b += 1
if b == 0:
    print("All characters count in the second string")
elif b != 0:
    print("Not all characters count in the second string")
else:
    print("What does go wrong?!")
