from argparse import ArgumentParser, Namespace


def parse_args() -> Namespace:
    p = ArgumentParser()
    subparsers = p.add_subparsers(dest="command", required=True)

    hello = subparsers.add_parser("hello")
    hello.add_argument("-n", "--name", type=str, default="World")

    return p.parse_args()


def main() -> None:
    args = parse_args()
    if args.command == "hello":
        print(f"Hello, {args.name}!")
