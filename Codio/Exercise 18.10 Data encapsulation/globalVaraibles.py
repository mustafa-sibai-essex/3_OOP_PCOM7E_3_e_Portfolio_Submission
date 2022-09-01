# global variables
ages = [10, 20, 24, 23, 55, 31, 30, 16]


def sumAllAges():
    sum = 0

    for age in ages:
        sum += age

    return sum


def main():
    result = sumAllAges()
    print(result)


main()
