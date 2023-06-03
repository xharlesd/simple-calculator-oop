import pyfiglet
from colorama import Fore, Style
import time
from Calculator_class import Calculator

class CalculatorChild(Calculator):
    def try_again(self):
        retry = None
        while retry is None:
            time.sleep(1)
            again = input(Fore.MAGENTA + "\n\t Do you want to try again (YES/NO)?  ")

            # the program will run again if the user inputted YES
            if again == "Y" or again == "Yes" or again == "YES" or again == "yes":
                retry = str(again)
                continue

            # the program will terminate if the user inputted NO
            if again == "N" or again == "No" or again == "NO" or again == "no":
                time.sleep(0.5)
                print(Fore.CYAN + "\t [Program will be terminated..............]")

                time.sleep(1.5)
                print("\n")
                print(Fore.CYAN + "\033[1m-" * 110 + '\033[0m')
                print(" ")

                end = pyfiglet.figlet_format("   THANK YOU !!   ", font = "banner3",  width = 110, justify = "center")
                print(Style.BRIGHT + Fore.CYAN + end)
                exit()

            else:
                print(Fore.RED + "\t [ERROR] Please choose either YES or NO only.")
    
    def get_numbers(self):
        while True:
            try:
                self.num1 = float(input(Fore.YELLOW + "\033[1m" + "\n\t FIRST NUMBER:    \033[0m" + Fore.YELLOW))
                self.num2 = float(input(Fore.YELLOW + "\033[1m" + "\t SECOND NUMBER:   \033[0m" + Fore.YELLOW))
                break
            except:
                print(Fore.RED + "\t [ERROR] Invalid input. Please enter numerical values only.")
                continue