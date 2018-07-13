""" Reads in an expression in Postfix form, and evaluates the expression. 6/30/2018 """
import InfixToPostfix
from collections import deque

def main(variables):
    keep_evaluating = True
    prev_ans        = 0
    print ("Valid operators are +, -, *, /, %, ^, and (). Enter an expression, or q to quit.")
    while keep_evaluating:
        expression = enter_expression(prev_ans, variables)
        if expression[0][0] != "q":
            postfix = InfixToPostfix.main(expression).split()
            prev_ans = evaluate_expression(postfix)
            print (prev_ans)
        keep_evaluating = False if expression[0][0] == "q" else True

def enter_expression(prev_ans, variables):
    valid_expression = False
    while not valid_expression:
        expression = input("> ")
        expression = expression.replace("ans", str(prev_ans))
        for key, value in variables.items():
            expression = expression.replace(key, str(value))
        tokens = expression.split()
        valid_expression = tokens[0][0] == "q" or check_expression(tokens) 
    return tokens

def check_expression(tokens):
    for token in tokens:
        if not InfixToPostfix.represents_float(token) and not InfixToPostfix.is_operator(token):
            print ("token \"" + token + "\" was invalid. Enter a valid operator, and be sure to put a space between the operators and numbers.")
            return False
    return True

def evaluate_expression(postfix):
    values = deque()
    for token in postfix:
        if InfixToPostfix.represents_float(token):
            values.append(token)
        elif InfixToPostfix.is_operator(token):
            val2 = values.pop()
            val1 = values.pop()
            values.append(evaluate_op(float(val1), float(val2), token))
    return values.pop()

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

if __name__ == "__main__":
    main()