""" Reads in an expression in Infix form, and converts it to Postfix. 

Implements the Shunting Yard Algorithm. 6/24/2018

"""
from collections import deque

def main():
    output     = deque()
    operators  = deque()
    precedence = {"+":0, "-":0, "*":1, "/":1, "%":1}
    expression = input("Enter an expression: ")
    tokens     = expression.split()
    for token in tokens:
        if represents_int(token):
            output.append(token)
        elif is_operator(token):
            prev_op = operators.pop() if len(operators) > 0 else ""
            while len(operators) > 0 and precedence.get(prev_op) >= precedence.get(token):
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
    print (result)


def represents_int(token):
    try:
        int(token)
        return True
    except ValueError:
        return False

def is_operator(token):
    return token == "+" or token == "-" or token == "*" or token == "/" or token == "%"

if __name__ == "__main__":
    main()