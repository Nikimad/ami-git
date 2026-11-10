import argparse
from collections.abc import Callable, Sequence

from statscli.stats import average, maximum, minimum

COMMANDS: dict[str, Callable[[Sequence[float]], float]] = {
    "avg": average,
    "max": maximum,
    "min": minimum,
}

def number(text: str) -> int | float:
    try:
        return int(text)
    except ValueError:
        return float(text)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="statscli",
        description="Calculates simple statistics for a list of numbers.",
    )
    parser.add_argument("command", choices=COMMANDS, help="what to calculate")
    parser.add_argument("numbers", nargs="*", type=number, help="input numbers")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command != "avg" and not args.numbers:
        parser.error(f"{args.command} needs at least one number")
    print(COMMANDS[args.command](args.numbers))
    return 0