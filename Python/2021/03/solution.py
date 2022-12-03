import copy


def parse_data():
    with open("input.txt", "r") as file:
        data = [[c for c in line.strip()] for line in file]
        return data


def part_one(data: list[list[str]]):
    gama = ""
    epsilon = ""
    for column in zip(*data):
        if column.count("1") > column.count("0"):
            gama += "1"
            epsilon += "0"
        else:
            gama += "0"
            epsilon += "1"
    gama = int(gama, 2)
    epsilon = int(epsilon, 2)
    return gama * epsilon


def part_two(data: list[list[str]]):
    count = 0
    data2 = data.copy()
    while len(data) > 1:
        i = list(zip(*data))[count]
        if i.count("1") < i.count("0"):
            common = "0"
        else:
            common = "1"
        data = [x for x in data if x[count] == common]
        count += 1
    count = 0
    while len(data2) > 1:
        i = list(zip(*data2))[count]
        if i.count("1") < i.count("0"):
            common = "1"
        else:
            common = "0"
        data2 = [x for x in data2 if x[count] == common]
        count += 1
    return int("".join(data[0]), 2) * int("".join(data2[0]), 2)


def main():
    data = parse_data()
    print(part_one(data))
    print(part_two(data))


if __name__ == "__main__":
    main()
