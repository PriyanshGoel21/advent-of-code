def parse_data():
    with open("input.txt", "r") as file:
        data = [int(line) for line in file]
    return data


def part_one(data: list):
    solution = 0
    for index, value in enumerate(data):
        if value > data[index - 1] and index != 0:
            solution += 1
    return solution


def part_two(data: list):
    solution = 0
    for index, value in enumerate(data):
        if value > data[index - 3] and index > 2:
            solution += 1
    return solution


def part_one_esoteric(data):
    return sum(i > j for j, i in zip(data, data[1:]))


def part_two_esoteric(data):
    return sum(i > j for j, i in zip(data, data[3:]))


def main():
    data = parse_data()
    print(part_one(data))
    print(part_two(data))


if __name__ == "__main__":
    main()
