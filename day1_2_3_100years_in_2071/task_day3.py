import datetime
my_name = input("What is your name? ")
my_age = input(f"How old are you, {my_name} ")
a = int(my_age)
print(f"You will be 100 in {100 - a} years")

print("The year is", datetime.datetime.now().year)
my_year = datetime.datetime.now().year
b = int(my_year)
print(f"You will be 100 in {b + a}")
