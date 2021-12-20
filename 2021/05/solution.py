import re


def parse_data():
    with open("input.txt", "r") as file:
        for x1, y1, x2, y2 in re.findall(r"(\d+),(\d+) -> (\d+),(\d+)", file.read()):
            yield (int(x1), int(y1)), (int(x2), int(y2))


def plot(data, diagonals=False):
    points = {}
    for line in data:
        x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
        gradiant = int((y2 - y1) / (x2 - x1)) if x2 - x1 != 0 else None
        if gradiant is None:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if (x1, y) not in points:
                    points[(x1, y)] = 1
                else:
                    points[(x1, y)] += 1
        else:
            constant = y1 - (gradiant * x1)
            if (gradiant == 0 and diagonals is False) or diagonals is True:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    y = gradiant * x + constant
                    if (x, y) not in points:
                        points[(x, y)] = 1
                    else:
                        points[(x, y)] += 1
    intersections = 0
    for point in points.values():
        if point > 1:
            intersections += 1
    return intersections


def part_one(data):
    return plot(data)


def part_two(data):
    return plot(data, diagonals=True)


def main():
    data = tuple(parse_data())
    print(part_one(data))
    print(part_two(data))


if __name__ == "__main__":
    main()
