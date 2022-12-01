salary = float(input("What is your salary?"))
years = float(input("How many years did you work?"))
if years > 2:
    bonus = salary*0.15*(years-2)
    print("your bonus is ", bonus)
else:
    print("no bonus")
