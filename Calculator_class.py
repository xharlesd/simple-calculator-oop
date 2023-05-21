# class Calculator
class Calculator:

    # constructor
    def __init__(self):
        self.num1 = 0.0
        self.num = 0.0
        self.operation = ""
        self.result = None

    # get numbers
    def get_numbers(self):
        try:
            self.num1 = float(input("Enter first number: "))
            self.num2 = float(input("Enter second number: "))
        except:
            print("ERROR! Invalid input.")

    # choose operation
    def choose_operation(self): 
        match self.operation:
            case "+": self.result = self.num1 + self.num2
            case "-": self.result = self.num1 - self.num2
            case "*": self.result = self.num1 * self.num2
            case "/": self.result = self.num1 / self.num2
    
    # display result
    def display_result(self):
        print("Result: ", self.result)
