#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    num_of_args = len(argv) - 1
    if num_of_args == 0:
        print("{:d} arguments.".format(num_of_args))
    else:
        print(
            "{:d} {:s}:".format(
                num_of_args, "argument" if num_of_args == 1 else "arguments"
            )
        )
        for i in range(1, len(argv)):
            print("{:d}: {:s}".format(i, argv[i]))
