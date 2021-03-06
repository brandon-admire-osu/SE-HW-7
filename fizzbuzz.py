
def fizzBuzz(x):
    if (x % 3) == 0 and (x % 5) == 0:
        return "FizzBuzz"
    elif (x % 3) == 0:
        return "Fizz"
    elif (x % 5) == 0:
        return "Buzz"
    else:
        return x

for i in range(1,101):
    print(fizzBuzz(i))