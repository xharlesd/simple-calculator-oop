import pyfiglet
from colorama import Fore, Style
import time
from Calculator_try_again import try_again

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
        print(Style.BRIGHT + Fore.LIGHTCYAN_EX + "\033[1m-" * 109 + '\033[0m')

    # get numbers
    def get_numbers(self):
        while True:
            try:
                self.num1 = float(input(Fore.CYAN + "\033[1m" + "\n\t FIRST NUMBER:    \033[0m" + Fore.CYAN))
                self.num2 = float(input(Fore.CYAN + "\033[1m" + "\t SECOND NUMBER:   \033[0m" + Fore.CYAN))
                break
            except:
                print(Fore.RED + "\t [ERROR] Invalid input. Please enter numerical values only.")
                try_again()

    # choose operation
    def choose_operation(self): 
        while True:
            try:
                self.operation = input(Fore.YELLOW + "\033[1m" + "\n\t OPERATION [ + , - , * , / ]:   \033[0m" + Fore.YELLOW)
                match self.operation:
                    case "+": self.result = self.num1 + self.num2
                    case "-": self.result = self.num1 - self.num2
                    case "*": self.result = self.num1 * self.num2
                    case "/": self.result = self.num1 / self.num2
                print(Fore.YELLOW + "\n\t [Calculating....................]")
                time.sleep(2.5)
                break
            
            except:
                print(Fore.RED + "\t [ERROR] Invalid input. Please choose among the four operations only.")
                try_again()
    
    # display result
    def display_result(self):
        result = round(self.result, 4)
        print(Fore.GREEN + "\033[1m" + f"\n\t RESULT:     {result} \033[0m ")



    
        

