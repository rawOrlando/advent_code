
class BingoBoard:

    def __init__(self, text_lines):
        index = 0
        self.board = [[0]*5]*5
        for line in text_lines[1:]:
            self.board[index] = [int(number) for number in line.split()]
            index += 1
            if index >= 5:
                break

    def mark_number_and_has_won(self, number):
        index_y, index_x = self.mark_number(number)
        if index_y is None:
            return False
        return self._has_won_from_square(index_y, index_x)



    def mark_number(self, number):
        index_y = 0
        while index_y < len(self.board):
            index_x = 0
            while index_x < len(self.board[0]):
                if number == self.board[index_y][index_x]:
                    self.board[index_y][index_x] = -1
                    return index_y, index_x
                index_x += 1
            index_y += 1
        return None, None


    def has_won(self):
        pass

    def _has_won_from_square(self, index_y, index_x):
        if (self._has_won_from_down(index_x) or
            self._has_won_from_across(index_y)):
            return True
        if index_y == index_x or index_y + index_x == 4:
            return self._has_won_diagonal()
        return False


    def _has_won_from_down(self, index_x):
        index_y = 0
        while index_y < len(self.board):
            if self.board[index_y][index_x] != -1:
                return False
            index_y += 1

        return True

    def _has_won_from_across(self, index_y):
        index_x = 0
        while index_x < len(self.board):
            if self.board[index_y][index_x] != -1:
                return False
            index_x += 1

        return True

    def _has_won_diagonal(self):
        return self._has_won_diagonal_v() or self._has_won_diagonal_y()

    def _has_won_diagonal_v(self):
        # goign \
        index_x = 0
        while index_x < len(self.board):
            if self.board[index_x][index_x] != -1:
                return False
            index_x += 1
        return True

    def _has_won_diagonal_y(self):
        # goign /
        index_x = 0
        while index_x < len(self.board):
            if self.board[index_x][4-index_x] != -1:
                return False
            index_x += 1
        return True

    def score(self, last_number):
        # this feels bad.
        return sum([x if x != -1 else 0 for line in self.board for x in line])*last_number

    def __str__(self):
        return self.board.__str__()

def read_bingo_numbers(line):
    return [int(number) for number in line.split(",")]

bingo_numbers = list()
bingo_tiles = list()

with open('day_04_puzzle_input.txt') as f:
    lines = f.readlines()
    # Read Bingo  numbers
    bingo_numbers = read_bingo_numbers(lines[0])

    #not eis there a better way to do this with itertools
    index = 1
    while index < len(lines) - 5:
        # Read Bingo  numbers
        bingo_tiles.append(BingoBoard(lines[index:index+6]))

        index += 6




for number in bingo_numbers:
    for bingo_tile in list(bingo_tiles):
        if bingo_tile.mark_number_and_has_won(number):
            print("WON")
            print(bingo_tile.score(number))
            bingo_tiles.remove(bingo_tile)



