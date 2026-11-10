import sys

from stats import average, maximum, minimum

COMMANDS = {"avg": average, "max": maximum, "min": minimum}


def main(argv):
    if len(argv) < 2 or argv[1] not in COMMANDS:
        print("usage: python cli.py avg|max|min [NUMBER ...]")
        return 1
    nums = [float(x) for x in argv[2:]]
    if argv[1] != "avg" and not nums:
        print("max/min need at least one number")
        return 1
    print(COMMANDS[argv[1]](nums))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
