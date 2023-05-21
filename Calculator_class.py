import pyfiglet
from colorama import Fore, Style

# class Calculator
class Calculator:

    # get numbers
    def get_numbers(self):
        try:
            self.num1 = float(input(Fore.CYAN + "\033[1m" + "\n\t Enter first number:   \033[0m" + Fore.CYAN))
            self.num2 = float(input(Fore.CYAN + "\033[1m" + "\t Enter second number:   \033[0m" + Fore.CYAN))
        except:
            print("ERROR! Invalid input.")

    # choose operation
    def choose_operation(self): 
        try:
            self.operation = input("Enter operation to be used: ")
            match self.operation:
                case "+": self.result = self.num1 + self.num2
                case "-": self.result = self.num1 - self.num2
                case "*": self.result = self.num1 * self.num2
                case "/": self.result = self.num1 / self.num2
            return self.result
        except:
            print("ERROR! Invalid input.")
    
    # display result
    def display_result(self):
        print(f"Result: {self.result}")
        

