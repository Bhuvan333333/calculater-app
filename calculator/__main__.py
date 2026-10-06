"""CLI: python -m calculator <add|subtract|multiply> <a> <b>"""
import argparse

from . import add, subtract, multiply

OPERATIONS = {"add": add, "subtract": subtract, "multiply": multiply}


def main(argv=None):
    parser = argparse.ArgumentParser(prog="calculator")
    parser.add_argument("operation", choices=OPERATIONS)
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    args = parser.parse_args(argv)
    try:
        print(OPERATIONS[args.operation](args.a, args.b))
    except (TypeError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
