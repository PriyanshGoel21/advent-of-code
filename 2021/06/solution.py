def parse_data():
    fishes = [0] * 10
    with open("input.txt", "r") as file:
        for fish in map(int, file.read().strip().split(",")):
            fishes[fish] += 1
        return fishes


def calculate(data, days):
    data = data.copy()
    for day in range(days):
        data[9] = data[0]
        data[7] += data[0]
        data[0] = 0
        for fish in range(1, 10):
            data[fish - 1] = data[fish]
            data[fish] = 0
    return sum(data[:9])


def main():
    data = parse_data()
    print(calculate(data, 80))
    print(calculate(data, 256))


if __name__ == "__main__":
    main()
