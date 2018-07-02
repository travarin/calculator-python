""" Reads in an expression in Infix form, and converts it to Postfix. 

Implements the Shunting Yard Algorithm. 6/24/2018

"""
from collections import deque

def main():
    output     = deque()
    operators  = deque()
    precedence = {"+":0, "-":0, "*":1, "/":1, "%":1, "^":2}
    tokens     = enter_expression()
    for token in tokens:
        if represents_int(token):
            output.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            prev_op = operators.pop()
            while len(operators) > 0 and prev_op != "(":
                output.append(prev_op)
                prev_op = operators.pop()
        elif is_operator(token):
            prev_op = operators.pop() if len(operators) > 0 else ""
            while len(operators) > 0 and prev_op != "(" and precedence.get(prev_op) >= precedence.get(token):
                output.append(prev_op)
                prev_op = operators.pop()
            operators.append(prev_op)
            operators.append(token)

    while len(operators) > 0:
        op = operators.pop()
        output.append(op)
    result = ""
    while len(output) > 0:
        result += output.popleft() + " "
    return result


def represents_int(token):
    try:
        int(token)
        return True
    except ValueError:
        return False

def is_operator(token):
    return token == "+" or token == "-" or token == "*" or token == "/" or token == "%" or token == "^" or token == "(" or token == ")"

def enter_expression():
    valid_expression = False
    while not valid_expression:
        expression = input("Valid operators are +, -, *, /, %, ^, and (). Enter an expression: ").split()
        valid_expression = check_expression(expression)
    return expression

def check_expression(tokens):
    for token in tokens:
        if not represents_int(token) and not is_operator(token):
            print ("token \"" + token + "\" was invalid. Enter a valid operator, and be sure to put a space between the operators and numbers.")
            return False
    return True

if __name__ == "__main__":
    main()