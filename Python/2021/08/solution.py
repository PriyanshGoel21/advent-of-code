def parse_data():
    with open("input.txt", "r") as file:
        for line in file:
            pattern, output = line.split("|")
            yield pattern.strip().split(" "), output.strip().split(" ")


def part_one(data):
    counter = 0
    for i in data:
        for number in i[1]:
            if len(number) in [2, 4, 3, 7]:
                counter += 1
    return counter


KEY = {
    (6, 2, 3): "0",
    (2, 2, 2): "1",
    (5, 1, 2): "2",
    (5, 2, 3): "3",
    (4, 2, 4): "4",
    (5, 1, 3): "5",
    (6, 1, 3): "6",
    (3, 2, 2): "7",
    (7, 2, 4): "8",
    (6, 2, 4): "9"

}


def part_two(data):
    output = 0
    for training, actual in data:
        training = sorted(training, key=len)
        one = set(str(training[0]))
        four = set(str(training[2]))
        digit_s = ""
        for digit in actual:
            digit = set(digit)
            digit = KEY[(len(digit), len(digit.intersection(one)), len(digit.intersection(four)))]
            digit_s += digit
        output += int(digit_s)
        output += int(digit_s)
    return output


def main():
    data = tuple(parse_data())
    print(part_one(data))
    print(part_two(data))


if __name__ == "__main__":
    main()
