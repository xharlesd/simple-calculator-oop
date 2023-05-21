import pyfiglet
from colorama import Fore, Style
import time

def try_again():
    retry = None
    while retry is None:
        time.sleep(1)
        again = input(Fore.MAGENTA + "\n\t    Do you want to try again? (YES/NO)  ")

        # the program will run again if the user inputted YES
        if again == "Y" or again == "Yes" or again == "YES" or again == "yes":
            retry = str(again)
            continue

        # the program will terminate if the user inputted NO
        if again == "N" or again == "No" or again == "NO" or again == "no":
            time.sleep(0.5)
            print(Fore.CYAN + "\t    [Program will be terminated..............]")

            time.sleep(1.5)
            print("\n")
            print(Fore.GREEN + "\033[1m-" * 140 + '\033[0m')
            print(" ")

            lab = pyfiglet.figlet_format("   THANK YOU !!   ", font = "banner3",  width = 140, justify = "center")
            print(Style.BRIGHT + Fore.GREEN + lab)
            exit()
        else:
            print(Fore.RED + "\t    [ERROR] Please choose either YES or NO only.")