""" A simple calculator implemented in Python. Can perform algebraic operations. 6/30/2018 """
import AlgebraicExpression

def main():
    options = {0:"Algebraic expression"}
    keep_looping = True
    print ("Welcome to the Python 3 Calculator. \n")
    while keep_looping:
        print ("Your options are: ")
        print_options(options)
        option = input("\nEnter your choice, or q to quit: ")
        if option == "0":
            algebraic_expression()
        elif option == "q":
            keep_looping = False
        



def print_options(options):
    for key, value in options.items():
        print ("Enter " + str(key) + " for " + value)

def algebraic_expression():
    AlgebraicExpression.main()    


if __name__ == "__main__":
    main()