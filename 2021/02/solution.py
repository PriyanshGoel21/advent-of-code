def parse_data():
    with open("input.txt", "r") as file:
        data = [line.strip() for line in file]
    return data


def part_one(data: list[str]):
    forward = 0
    depth = 0
    for command in data:
        com, x = command.split()
        match com:
            case "forward":
                forward += int(x)
            case "down":
                depth += int(x)
            case "up":
                depth -= int(x)
    return forward * depth


def part_two(data: list[str]):
    forward = 0
    depth = 0
    aim = 0
    for command in data:
        com, x = command.split()
        match com:
            case "forward":
                forward += int(x)
                depth += aim * int(x)
            case "down":
                aim += int(x)


def main():
    data = parse_data()
    print(part_one(data))
    print(part_two(data))


if __name__ == "__main__":
    main()
