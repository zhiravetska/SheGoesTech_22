for n in range(1, 101):
    if n % 5 == 0:
        print("Fizz")
    if n % 7 == 0:
        print("Buzz")
    if n % 5 == 0 and n % 7 == 0:
        print("FizzBuzz")
    else:
        print(n)
