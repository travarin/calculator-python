""" Reads in an expression in Infix form, and converts it to Postfix. 

Implements the Shunting Yard Algorithm. 6/24/2018

"""
from collections import deque

def main(tokens):
    output     = deque()
    operators  = deque()
    precedence = {"+":0, "-":0, "*":1, "/":1, "%":1, "^":2}
    for token in tokens:
        if represents_float(token):
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


def represents_float(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

def is_operator(token):
    return token == "+" or token == "-" or token == "*" or token == "/" or token == "%" or token == "^" or token == "(" or token == ")"

if __name__ == "__main__":
    main()