""" Reads in an expression in Postfix form, and evaluates the expression. 6/30/2018 """
import InfixToPostfix
from collections import deque

def main():
    keep_evaluating = True
    print ("Valid operators are +, -, *, /, %, ^, and (). Enter an expression, or q to quit.")
    while keep_evaluating:
        expression = enter_expression()
        if expression[0][0] != "q":
            postfix = InfixToPostfix.main(expression).split()
            values     = deque()
            for token in postfix:
                if InfixToPostfix.represents_int(token):
                    values.append(token)
                elif InfixToPostfix.is_operator(token):
                    val2 = values.pop()
                    val1 = values.pop()
                    values.append(evaluate_op(int(val1), int(val2), token))
            print (values.pop())
        keep_evaluating = False if expression[0][0] == "q" else True

def evaluate_op(val1, val2, operator):
    if operator == "+":
        return val1 + val2
    elif operator == "-":
        return val1 - val2
    elif operator == "*":
        return val1 * val2
    elif operator == "/":
        return val1 / val2
    elif operator == "%":
        return val1 % val2
    elif operator == "^":
        return val1 ** val2

def enter_expression():
    valid_expression = False
    while not valid_expression:
        expression = input("> ").split()
        valid_expression = expression[0][0] == "q" or check_expression(expression) 
    return expression

def check_expression(tokens):
    for token in tokens:
        if not InfixToPostfix.represents_int(token) and not InfixToPostfix.is_operator(token):
            print ("token \"" + token + "\" was invalid. Enter a valid operator, and be sure to put a space between the operators and numbers.")
            return False
    return True

if __name__ == "__main__":
    main()