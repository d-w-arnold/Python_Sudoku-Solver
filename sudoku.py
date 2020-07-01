import numpy as np
import random as rnd


class Sudoku:
    BASE = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [4, 5, 6, 7, 8, 9, 1, 2, 3],
                     [7, 8, 9, 1, 2, 3, 4, 5, 6],
                     [2, 3, 4, 5, 6, 7, 8, 9, 1],
                     [5, 6, 7, 8, 9, 1, 2, 3, 4],
                     [8, 9, 1, 2, 3, 4, 5, 6, 7],
                     [3, 4, 5, 6, 7, 8, 9, 1, 2],
                     [6, 7, 8, 9, 1, 2, 3, 4, 5],
                     [9, 1, 2, 3, 4, 5, 6, 7, 8]], ndmin=2)
    board = np.zeros((9, 9), dtype=np.int)
    emptyCoords = list()
    tries = dict()

    def __init__(self):
        self.generate_board()

    def print_board(self):
        print(self.board)
        print()

    def generate_board(self):
        for x in range(9):
            for y in range(9):
                if bool(rnd.getrandbits(1)):
                    self.board[x, y] = self.BASE[x, y]
        self.setEmptyCoords()

    def setEmptyCoords(self):
        for x in range(len(self.board)):
            row = self.board[x]
            for y in range(len(row)):
                if row[y] == 0:
                    self.emptyCoords.append((x, y))
        self.setTries()

    def setTries(self):
        for x in self.emptyCoords:
            self.tries[x] = set()

    # Starting solving the Sudoku game using backtracking algorithm:
    # Source: https://dev.to/aspittel/how-i-finally-wrote-a-sudoku-solver-177g
    def solve(self):
        index = 0
        while index < len(self.emptyCoords):
            cd = self.emptyCoords[index]
            for v in range(1, 10):
                pu = not (self.prevUsed(cd, v))
                vr = self.validRow(cd, v)
                vc = self.validCol(cd, v)
                vsm = self.validSubMatrix(cd, v)
                if pu and vr and vc and vsm:
                    self.board[cd[0], cd[1]] = v
                    tmp = set()
                    for n in range(1, v + 1):
                        tmp.add(n)
                    self.tries[cd] = tmp
                    index = index + 1
                    break
                elif v == 9:
                    self.tries[cd] = set()
                    index = index - 1
                    break
        print("Sudoku board completed!")
        print()

    def prevUsed(self, coord, value):
        return value in self.tries[coord]

    def validRow(self, coord, value):
        row_id = coord[0]
        col_id = coord[1]
        row = self.board[row_id]
        for i in range(0, len(row)):
            if i == col_id:
                continue
            if row[i] == value:
                return False
        return True

    def validCol(self, coord, value):
        row_id = coord[0]
        col_id = coord[1]
        for i in range(0, len(self.board)):
            if i == row_id:
                continue
            cellVal = self.board[i, col_id]
            if cellVal == value:
                return False
        return True

    def validSubMatrix(self, coord, value):
        subMatrixVals = self.getSubMatrixSet(coord)
        return not (value in subMatrixVals)

    def getSubMatrixSet(self, coord):
        row_id = coord[0]
        col_id = coord[1]
        if row_id < 3 and col_id < 3:
            return self.getSubMatrixSetHelper(coord, 3, 3)
        elif row_id < 3 and col_id < 6:
            return self.getSubMatrixSetHelper(coord, 3, 6)
        elif row_id < 3 and col_id < 9:
            return self.getSubMatrixSetHelper(coord, 3, 9)
        elif row_id < 6 and col_id < 3:
            return self.getSubMatrixSetHelper(coord, 6, 3)
        elif row_id < 6 and col_id < 6:
            return self.getSubMatrixSetHelper(coord, 6, 6)
        elif row_id < 6 and col_id < 9:
            return self.getSubMatrixSetHelper(coord, 6, 9)
        elif row_id < 9 and col_id < 3:
            return self.getSubMatrixSetHelper(coord, 9, 3)
        elif row_id < 9 and col_id < 6:
            return self.getSubMatrixSetHelper(coord, 9, 6)
        elif row_id < 9 and col_id < 9:
            return self.getSubMatrixSetHelper(coord, 9, 9)
        return set()

    def getSubMatrixSetHelper(self, coord, row, col):
        tmp = set()
        for i in range(row - 1, row - 1 - 3):
            for j in range(col - 1, col - 1 - 3):
                if coord[0] == i and coord[1] == j:
                    continue
                tmp.add(self.board[i, j])
        return tmp
