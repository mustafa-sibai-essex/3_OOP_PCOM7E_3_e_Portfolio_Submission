# In ‘Packaging & Testing’ (unit 9), we examined the use of documentation to support code developments. Add appropriate commenting and documentation for the code below.
# Simple calulcator program


def add(x, y):
    """Adds two numbers"""
    return x + y


def subtract(x, y):
    """Subtract two numbers"""
    return x - y


def multiply(x, y):
    """Multiplies two numbers"""
    return x * y


def divide(x, y):
    """Divides two numbers"""
    return x / y


# Prints to the user the choices they have
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Start an infinite while loop
while True:
    # Asks the user to choice from the above choices by calling the
    # input function which takes the user keyboard input
    choice = input("Enter choice(1/2/3/4): ")

    # Check if the user has picked one of the 4 valid choices
    if choice in ("1", "2", "3", "4"):

        # Converts the first number input which comes as a string to a float to do the math on
        num1 = float(input("Enter first number: "))

        # Converts the second number input which comes as a string to a float to do the math on
        num2 = float(input("Enter second number: "))

        # if the choice was 1 call the add function
        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))

        # if the choice was 2 call the subtract function
        elif choice == "2":
            print(num1, "-", num2, "=", subtract(num1, num2))

        # if the choice was 3 call the multiply function
        elif choice == "3":
            print(num1, "*", num2, "=", multiply(num1, num2))

        # if the choice was 4 call the divide function
        elif choice == "4":
            print(num1, "/", num2, "=", divide(num1, num2))

        # Check and ask the user if they want to do another mathematical operation
        next_calculation = input("Let's do next calculation? (yes/no): ")

        # If the answer is not break the loop and exit the application
        if next_calculation == "no":
            break

    # If the user picked something other than 1, 2, 3, 4 prints the below statment
    else:
        print("Invalid Input")

# Source: Progamiz. (n.d.) Python Program to Make a Simple Calculator.
