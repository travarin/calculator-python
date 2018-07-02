""" Reads in an expression in Postfix form, and evaluates the expression. 6/30/2018 """
import InfixToPostfix
from collections import deque

def main():
    expression = InfixToPostfix.main().split()
    values     = deque()
    for token in expression:
        if InfixToPostfix.represents_int(token):
            values.append(token)
        elif InfixToPostfix.is_operator(token):
            val2 = values.pop()
            val1 = values.pop()
            values.append(evaluate_op(int(val1), int(val2), token))
    print (values.pop())


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