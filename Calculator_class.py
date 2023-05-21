import pyfiglet
from colorama import Fore, Style

# class Calculator
class Calculator:
    def title(self):
        print("")
        title = pyfiglet.figlet_format("CALCULATOR", font = "banner3-d", width = 110, justify = "center")
        print(Fore.LIGHTCYAN_EX + title)

    # get numbers
    def get_numbers(self):
        try:
            self.num1 = float(input(Fore.CYAN + "\033[1m" + "\n\t FIRST NUMBER:    \033[0m" + Fore.CYAN))
            self.num2 = float(input(Fore.CYAN + "\033[1m" + "\t SECOND NUMBER:   \033[0m" + Fore.CYAN))
        except:
            print(Fore.RED + "\t [ERROR] Invalid input.")

    # choose operation
    def choose_operation(self): 
        try:
            self.operation = input(Fore.YELLOW + "\033[1m" + "\n\t OPERATION [ + , - , * , / ]:   \033[0m" + Fore.YELLOW)
            match self.operation:
                case "+": self.result = self.num1 + self.num2
                case "-": self.result = self.num1 - self.num2
                case "*": self.result = self.num1 * self.num2
                case "/": self.result = self.num1 / self.num2
            return self.result
        except:
            print(Fore.RED + "\t [ERROR] Invalid input.")
    
    # display result
    def display_result(self):
        result = round(self.result, 4)
        print(Fore.GREEN + "\033[1m" + f"\n\t RESULT:     {result} \033[0m \n")
        

