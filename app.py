import sys


def average(nums):
    total = sum(nums[1:])
    count = len(nums)
    return total / count


def maximum(nums):
    return max(nums)


def minimum(nums):
    return min(nums)


def main(argv):
    commands = {"avg": average, "max": maximum, "min": minimum}
    if len(argv) < 2 or argv[1] not in commands:
        print("usage: python app.py avg|max|min [NUMBER ...]")
        return 1
    nums = [float(x) for x in argv[2:]]
    if argv[1] != "avg" and not nums:
        print("max/min need at least one number")
        return 1
    print(commands[argv[1]](nums))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
