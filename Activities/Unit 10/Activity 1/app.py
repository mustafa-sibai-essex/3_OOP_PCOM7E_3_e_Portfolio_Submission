# Run the following code using pylint and identify the errors.
# Source: Progamiz. (n.d.) Python Recursion.


def factorial(x):
    if x == 1:
        return 1

    return x * factorial(x - 1)


num = 3
print("The factorial of", num, "is", factorial(num))
