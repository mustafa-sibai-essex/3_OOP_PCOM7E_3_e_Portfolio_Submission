class AgeCalculator:
    def __init__(self, ages):
        self.ages = ages

    def sumAllAges(self):
        sum = 0

        for age in self.ages:
            sum += age

        return sum


def main():
    result = AgeCalculator([10, 20, 24, 23, 55, 31, 30, 16]).sumAllAges()
    print(result)


main()
