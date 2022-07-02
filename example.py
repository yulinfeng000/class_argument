# example.py
from arguments import Argument, Option


class ComputeArg(Argument):
    """
    THIS IS A DESCRIPTION ! ! ! !

    a compute program
    """

    x = Option("x", type=int, help="variable x")
    y = Option("y", type=int, help="variable y")
    opt = Option("--operator", "-opt", type=str, required=True, help="operator")


if __name__ == "__main__":

    args = ComputeArg()

    if args.opt == "x":
        print(args.x * args.y)
    elif args.opt == "+":
        print(args.x + args.y)
    elif args.operator == "-":
        print(args.x - args.y)
    elif args.operator == "/":
        print(args.x / args.y)
    else:
        print("error operator")
