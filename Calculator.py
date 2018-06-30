""" A simple calculator implemented in Python. Can perform algebraic operations. 6/30/2018 """
import AlgebraicExpression

def main():
    options = {0:"Algebraic expression"}
    keep_looping = True
    print ("Welcome to the Python 3 Calculator. ")
    while keep_looping:
        print ("Your options are: ")
        print_options(options)
        option = input("Enter your choice: ")
        if option == "0":
            algebraic_expression()
        keep_looping = True if input("Enter Y to continue looping: ") == "Y" else False



def print_options(options):
    for key, value in options.items():
        print ("Enter " + str(key) + " for " + value)

def algebraic_expression():
    AlgebraicExpression.main()    


if __name__ == "__main__":
    main()