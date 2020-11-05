import random


def randomise_board(board, per_row=5):
    randomised_board = []
    for x in range(len(board)):
        count = 0
        row = []
        for y in range(len(board[x])):
            if bool(random.getrandbits(1)) and count < per_row:
                row.append(0)
                count = count + 1
            else:
                row.append(board[x][y])
        randomised_board.append(row)
    return randomised_board


def print_board(msg, board):
    print(msg)
    x_sep = "-------------------------"
    y_sep = "| "
    print(x_sep)
    for x in range(len(board)):
        x_str = y_sep
        for y in range(len(board[x])):
            x_str += str(board[x][y]) + " "
            if (y + 1) % 3 == 0:
                x_str += y_sep
        print(x_str)
        if (x + 1) % 3 == 0:
            print(x_sep)
    print()


class Sudoku:
    # The sudoku board
    board = list(list())  # list(list(int))
    # The cells on the sudoku board that are yet to be complete - designated by 0
    tbc_cells = list()  # list(tuple(int, int))
    # The last number tried in each of the yet to be completed cells
    tbc_cells_last_tries = dict()  # tuple(int, int) -> int

    def __init__(self, board):
        self.board = board

    def get_board(self):
        return self.board

    def populate_data_structures(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == 0:
                    cell = tuple([x, y])
                    self.tbc_cells.append(cell)
                    self.tbc_cells_last_tries[cell] = 0

    def valid_row(self, n, x, y):
        for i in range(len(self.board[x])):
            if i == y:
                continue
            if self.board[x][i] == n:
                return False
        return True

    def valid_col(self, n, x, y):
        for i in range(len(self.board)):
            if i == x:
                continue
            if self.board[i][y] == n:
                return False
        return True

    def get_sub_square_helper(self, x, y, x_bound, y_bound):
        sub_square_res = set()
        for i in range(x_bound - 3, x_bound):
            for j in range(y_bound - 3, y_bound):
                if i == x and j == y:
                    continue
                sub_square_res.add(self.board[i][j])
        return sub_square_res

    def get_sub_square(self, x, y):
        if x < 3 and y < 3:
            return self.get_sub_square_helper(x, y, 3, 3)
        elif x < 3 and y < 6:
            return self.get_sub_square_helper(x, y, 3, 6)
        elif x < 3 and y < 9:
            return self.get_sub_square_helper(x, y, 3, 9)
        elif x < 6 and y < 3:
            return self.get_sub_square_helper(x, y, 6, 3)
        elif x < 6 and y < 6:
            return self.get_sub_square_helper(x, y, 6, 6)
        elif x < 6 and y < 9:
            return self.get_sub_square_helper(x, y, 6, 9)
        elif x < 9 and y < 3:
            return self.get_sub_square_helper(x, y, 9, 3)
        elif x < 9 and y < 6:
            return self.get_sub_square_helper(x, y, 9, 6)
        elif x < 9 and y < 9:
            return self.get_sub_square_helper(x, y, 9, 9)

    def valid_sub_square(self, n, x, y):
        return n not in self.get_sub_square(x, y)

    def solve(self):
        self.populate_data_structures()
        index = 0
        while index < len(self.tbc_cells):
            cell = self.tbc_cells[index]
            x = cell[0]
            y = cell[1]
            force_br = False
            for n in range(self.tbc_cells_last_tries[cell] + 1, len(self.board) + 1):
                if self.valid_row(n, x, y) and self.valid_col(n, x, y) and self.valid_sub_square(n, x, y):
                    self.tbc_cells_last_tries[cell] = n
                    self.board[x][y] = n
                    force_br = True
                    break
            if force_br:
                # Found a valid number option for this cell - no row, column or sub square collisions
                index = index + 1
            else:
                # Cannot find a valid number option for this cell, so backtrack to the last to be completed cell
                self.tbc_cells_last_tries[cell] = 0
                self.board[x][y] = 0
                index = index - 1
