import math


def parse_data():
    fishes = [0] * 10
    with open("input.txt", "r") as file:
        return tuple(map(int, file.read().strip().split(",")))


def calculate(data, part_two=False):
    min_fuel = math.inf
    for x in range(min(data), max(data) + 1):
        fuel = sum(
            [int(((abs(position - x) ** 2) + abs(position - x)) / 2) if part_two else abs(position - x) for position in
             data])
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel


def main():
    data = parse_data()
    print(calculate(data))
    print(calculate(data, True))


if __name__ == "__main__":
    main()
