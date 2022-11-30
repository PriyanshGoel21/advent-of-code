class Dice:
    def __init__(self):
        self.rolls = 0

    def roll(self):
        self.rolls += 1
        roll = self.rolls % 100
        return roll if roll != 0 else 100


class Player:
    def __init__(self, position):
        self.position = position
        self.score = 0

    def turn(self, dice):
        position = (self.position + dice) % 10
        position = position if position != 0 else 10
        self.position = position
        self.score += self.position


def parse_data():
    with open("input.txt", "r") as file:
        data = []
        for line in file:
            line = line.split(":")
            data.append(int(line[1].strip()))
        return data


def part_one(data):
    dice = Dice()
    player_one = Player(data[0])
    player_two = Player(data[1])
    while True:
        roll = sum(dice.roll() for _ in range(3))
        player_one.turn(roll)
        if player_one.score >= 1000:
            return player_two.score * dice.rolls
        roll = sum(dice.roll() for _ in range(3))
        player_two.turn(roll)
        if player_two.score >= 1000:
            return player_one.score * dice.rolls


def part_two(current_pos_p1, current_pos_p2, current_score_p1, current_score_p2):
    ...


def main():
    data = parse_data()
    print(part_one(data))
    print(part_two(data))


if __name__ == "__main__":
    main()
