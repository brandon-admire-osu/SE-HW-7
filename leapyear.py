usr_input = int(input("Please enter the year: "))

if(leap_check(usr_input)):
    print(f"{usr_input} is a leap year!")
else:
    print(f"{usr_input} is not a leap year.")

def leap_check(x):
    if (x % 4 == 0):
        if (x % 100 == 0 and x % 400 != 0):
            return False
        else:
            return True
    else:
        return False