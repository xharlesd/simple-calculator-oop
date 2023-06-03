# call calculator class
from Calculator_class import Calculator
from Calculator_child_class import CalculatorChild

calc = Calculator()
child = CalculatorChild()

# program title
calc.title()

# instructions
calc.instructions()

while True:
    # get numbers
    child.get_numbers()  

    # choose operation
    child.choose_operation()

    # display result
    child.display_result() 
    
    # try again
    child.try_again()
