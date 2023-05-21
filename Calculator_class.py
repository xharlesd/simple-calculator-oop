# class Calculator
class Calculator:

    # constructor
    def __init__(self):
        self.num1 = 0.0
        self.num2 = 0.0
        self.result = ""

    # get numbers
    def get_numbers(self):
        try:
            self.num1 = float(input("Enter first number: "))
            self.num2 = float(input("Enter second number: "))
        except:
            print("ERROR! Invalid input.")

    # choose operation
    # display result
