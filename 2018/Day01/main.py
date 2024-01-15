def main():
    with open("2018/input") as f:
        inputs = [int(line.rstrip()) for line in f]
        print(part_one(inputs))


def part_one(changes):
    return sum(changes)


if __name__ == "__main__":
    main()
