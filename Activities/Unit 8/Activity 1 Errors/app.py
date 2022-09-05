# Incorporate the following code into a Python program to handle exceptions.

try:
    x = int(input("Please enter the first number: "))
    y = int(input("Please enter the second number: "))

    r = x / y
    assert r == 1
    pass

except ValueError:
    print("Wrong value. Value must be a number")
    pass

except (TypeError, ZeroDivisionError):
    print("Type error or division by zero error")
    pass

except:
    print("Error was caught")
    pass
