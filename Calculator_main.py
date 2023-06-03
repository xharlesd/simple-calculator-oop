# call calculator class
from Calculator_class import Calculator
from Calculator_try_again import try_again
from Calculator_child_class import CalculatorChild

calc = Calculator()
child = CalculatorChild()

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
    
    # try again
    try_again()
