# call calculator class
from Calculator_class import Calculator
from Calculator_try_again import try_again

calc = Calculator()

# program title
calc.title()

# instructions
calc.instructions()

while True:
        
    # get numbers
    calc.get_numbers()  

    # choose operation
    calc.choose_operation()

    # display result
    calc.display_result() 

    try_again()

