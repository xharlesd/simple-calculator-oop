import pyfiglet
from colorama import Fore, Style

# class Calculator
class Calculator:

    # get numbers
    def get_numbers(self):
        try:
            self.num1 = float(input(Fore.GREEN + "\033[1m" + "\n\t Enter first number:   \033[0m" + "\033[0;32m"))
            self.num2 = float(input(Fore.GREEN + "\033[1m" + "\t Enter second number:   \033[0m" + "\033[0;32m"))
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