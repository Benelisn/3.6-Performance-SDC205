def functionOne():
    print("My Student ID is Josfar6040")


def functionTwo():
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a number: "))
    sumResult = num1 + num2
    print(f"The sum of {num1} and {num2} is {sumResult}.")
    return sumResult


def functionThree(sumValue):
    if sumValue > 5:
        print("The sum is greater than 5.")
    else:
        print("The sum is 5 or less.")
    studentIdNumber = 6040
    return studentIdNumber


def main():
    functionOne()                          # calls functionOne(); it prints the ID line and returns nothing
    sumResult = functionTwo()              # calls functionTwo(); stores its returned sum in sumResult
    idNumber = functionThree(sumResult)    # passes sumResult in; stores the returned ID number
    print(f"functionThree returned the value of {idNumber}.")  # prints the value functionThree() sent back


main()
