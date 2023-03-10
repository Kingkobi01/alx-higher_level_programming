#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    num_of_args = len(argv) - 1

    if num_of_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = argv[2]

    operators = "+-/*"

    a = int(argv[1])
    b = int(argv[3])
    result = 0

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "/":
        result = div(a, b)
    elif operator == "*":
        result = mul(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
