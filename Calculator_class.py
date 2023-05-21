import pyfiglet
from colorama import Fore
import time

# class Calculator
class Calculator:

    # program title
    def title(self):
        print("")
        title = pyfiglet.figlet_format("CALCULATOR", font = "banner3-d", width = 110, justify = "center")
        print(Fore.LIGHTCYAN_EX + title)

    # instructions
    def instructions(self):
        print(Fore.LIGHTCYAN_EX + "\033[1m-" * 109 + '\033[0m')
        ins = "PLEASE ENTER NUMERICAL VALUES FOR FIRST AND SECOND NUMBER, THEN SELECT THE OPERATION TO USE." 
        ins_centered = ins.center(110)
        print( "\033[1m" + ins_centered) 
        print(Fore.LIGHTCYAN_EX + "\033[1m-" * 109 + '\033[0m')

    # get numbers
    def get_numbers(self):
        try:
            self.num1 = float(input(Fore.CYAN + "\033[1m" + "\n\t FIRST NUMBER:    \033[0m" + Fore.CYAN))
            self.num2 = float(input(Fore.CYAN + "\033[1m" + "\t SECOND NUMBER:   \033[0m" + Fore.CYAN))
        except:
            print(Fore.RED + "\t [ERROR] Invalid input. Please enter numerical values only.")

    # choose operation
    def choose_operation(self): 
        try:
            self.operation = input(Fore.YELLOW + "\033[1m" + "\n\t OPERATION [ + , - , * , / ]:   \033[0m" + Fore.YELLOW)
            match self.operation:
                case "+": self.result = self.num1 + self.num2
                case "-": self.result = self.num1 - self.num2
                case "*": self.result = self.num1 * self.num2
                case "/": self.result = self.num1 / self.num2
            print(Fore.YELLOW + "\n\t [Calculating....................]")
            time.sleep(2.5)
            return self.result
        except:
            print(Fore.RED + "\t [ERROR] Invalid input. Please choose among the four operations only.")
    
    # display result
    def display_result(self):
        result = round(self.result, 4)
        print(Fore.GREEN + "\033[1m" + f"\n\t RESULT:     {result} \033[0m \n")
        

