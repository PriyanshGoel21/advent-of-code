class Square:
    def __init__(self, value):
        self.value = value
        self.marked = False


class Board:
    def __init__(self, squares: list[list[Square]]):
        self.squares = squares
        self.win_index = None
        self.win_number = None

    def mark(self, number: int):
        for row in self.squares:
            for square in row:
                if square.value == number:
                    square.marked = True

    def check_win(self):
        for x in range(5):
            flag = True
            for y in range(5):
                if self.squares[x][y].marked is False:
                    flag = False
                    break
            if flag is True:
                return True
        for y in range(5):
            flag = True
            for x in range(5):
                if self.squares[x][y].marked is False:
                    flag = False
                    break
            if flag is True:
                return True
        return False

    def score(self):
        total = 0
        for x in range(5):
            for y in range(5):
                if self.squares[x][y].marked is False:
                    total += self.squares[x][y].value
        return total * self.win_number


def parse_data(file: str = "input.txt"):
    with open(file, "r") as f:
        data = f.read().split("\n\n")
        numbers = list(map(int, data[0].split(",")))
        boards = []
        for board in data[1:]:
            rows = []
            for y, row in enumerate(board.split("\n")):
                values = []
                for x, value in enumerate(row.replace("  ", " ").strip().split(" ")):
                    values.append(Square(int(value)))
                rows.append(values)
            boards.append(Board(rows))
        return numbers, boards


def simulate_game(numbers, boards):
    win_index = 0
    for number in numbers:
        for index, board in enumerate(boards):
            if board.win_index is not None:
                continue
            board.mark(number)
            if board.check_win():
                board.win_index = win_index
                win_index += 1
                board.win_number = number


def get_board(boards, index):
    for board in boards:
        if board.win_index == index:
            return board.score()


def main():
    numbers, boards = parse_data()
    simulate_game(numbers, boards)
    print(get_board(boards, 0))  # Part 1
    print(get_board(boards, len(boards) - 1))  # Part 2


if __name__ == "__main__":
    main()
