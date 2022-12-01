a = float(input("What is your temperature?"))
if a < 35:
    print("a is less than 35")
    print("not too cold")
elif 35 <= a <= 37:
    print("all right")
else:
    print("a is larger than 37")
    print("possible fever")
