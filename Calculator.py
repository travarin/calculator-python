""" A simple calculator implemented in Python. Can perform algebraic operations. 6/30/2018 """
import AlgebraicExpression

def main():
    options      = {0:"Algebraic Expression", 1:"Store Variable", 2:"Print Variable"}
    keep_looping = True
    variables    = {}
    print ("Welcome to the Python 3 Calculator.")
    while keep_looping:
        print ("\nYour options are: ")
        print_options(options)
        option = input("\nEnter your choice, or q to quit: ")
        if option == "0":
            algebraic_expression(variables)
        elif option == "1":
            store_variable(variables)
        elif option == "2":
            print_variables(variables)
        elif option == "q":
            keep_looping = False
        
def print_options(options):
    for key, value in options.items():
        print ("Enter " + str(key) + " for " + value)

def algebraic_expression(variables):
    AlgebraicExpression.main(variables)

def store_variable(variables):
    var_name = input("\nEnter variable name: ")
    var_value = float(input("Enter variable value: "))
    variables[var_name] = var_value

def print_variables(variables):
    for key, value in variables.items():
        print (str(key) + " = " + str(value))

if __name__ == "__main__":
    main()