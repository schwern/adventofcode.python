def main():
    with open("2018/input") as f:
        inputs = [int(line.rstrip()) for line in f]
        calculate_frequency(inputs)


def calculate_frequency(changes):
    print(changes)


if __name__ == "__main__":
    main()
