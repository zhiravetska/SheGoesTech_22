# for n in range(1, 101):
#     if n % 5 == 0:
#         print("Fizz, ", end="")
#     elif n % 7 == 0:
#         print("Buzz, ", end="")
#     elif n % 5 == 0 and n % 7 == 0:
#         print("FizzBuzz, ", end="")
#     else:
#         print(f"{n}, ", end="")

height = int(input("Enter the height of the tree"))
for i in range(1, height+1):
    print(" " * (height-i), "*" * (i + (i-1)))
i = i + 1
print("What a lovely Christmas tree!!!")

# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199

# n = int(input("Enter a positive number"))
# for i in range(2, n):
#     if n % i == 0:
#         print("This is not a prime number")
#         break
# else:
#     print("This is a prime number")

# n = int(input("Enter a positive number:"))
# for i in range(2, n):
#     if n % i == 0:
#         print(f"{n} is not a prime number")
#         break
# else:
#     print(f"{n} is a prime number")


# if 5 > 2:
#     print("ochenj horosho")
# else:
#     print("ploho")
