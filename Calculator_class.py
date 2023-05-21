# class Calculator
class Calculator:

    # get numbers
    def get_numbers(self):
        try:
            self.num1 = float(input("Enter first number: "))
            self.num2 = float(input("Enter second number: "))
        except:
            print("ERROR! Invalid input.")

    # choose operation
    def choose_operation(self): 
        self.operation = input("Enter operation to be used: ")
        match self.operation:
            case "+": self.result = self.num1 + self.num2
            case "-": self.result = self.num1 - self.num2
            case "*": self.result = self.num1 * self.num2
            case "/": self.result = self.num1 / self.num2
        return self.result
    
    # display result
    def display_result(self):
        print("Result: ", self.result)
