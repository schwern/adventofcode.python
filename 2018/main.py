def main():
    with open("2018/input") as f:
        inputs = [int(line.rstrip()) for line in f]
        print(calculate_frequency(inputs))


def calculate_frequency(changes):
    return sum(changes)


if __name__ == "__main__":
    main()
