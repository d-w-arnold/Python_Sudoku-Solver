import numpy as np
import random as rnd

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


def generate_board():
    for x in range(9):
        for y in range(9):
            if bool(rnd.getrandbits(1)):
                board[x, y] = BASE[x, y]
    setEmptyCoords()


def setEmptyCoords():
    for x in range(len(board)):
        row = board[x]
        for y in range(len(row)):
            if row[y] == 0:
                emptyCoords.append((x, y))
    setTries()


def setTries():
    for x in emptyCoords:
        tries[x] = set()


# Starting solving the Sudoku game using backtracking algorithm:
# Source: https://dev.to/aspittel/how-i-finally-wrote-a-sudoku-solver-177g
def solve():
    index = 0
    while index < len(emptyCoords):
        cd = emptyCoords[index]
        for v in range(1, 10):
            pu = not (prevUsed(cd, v))
            vr = not (validRow(cd, v))
            vc = not (validCol(cd, v))
            vsm = not (validSubMatrix(cd, v))
            if pu and vr and vc and vsm:
                board[cd[0], cd[1]] = v
                tmp = set()
                for n in range(1, v + 1):
                    tmp.add(n)
                tries[cd] = tmp
                index = index + 1
                break
            elif v == 9:
                tries[cd] = set()
                index = index - 1
                break
    print()
    print("Sudoku board completed!")
    print()


def prevUsed(coord, value):
    return value in tries[coord]


def validRow(coord, value):
    row_id = coord[0]
    col_id = coord[1]
    row = board[row_id]
    for i in range(0, len(row)):
        if i == col_id:
            continue
        if row[i] == value:
            return False
    return True


def validCol(coord, value):
    row_id = coord[0]
    col_id = coord[1]
    for i in range(0, len(board)):
        if i == row_id:
            continue
        cellVal = board[i, col_id]
        if cellVal == value:
            return False
    return True


def validSubMatrix(coord, value):
    subMatrixVals = getSubMatrixSet(coord)
    return not (value in subMatrixVals)


def getSubMatrixSet(coord):
    row_id = coord[0]
    col_id = coord[1]
    if row_id < 3 and col_id < 3:
        return getSubMatrixSetHelper(coord, 3, 3)
    elif row_id < 3 and col_id < 6:
        return getSubMatrixSetHelper(coord, 3, 6)
    elif row_id < 3 and col_id < 9:
        return getSubMatrixSetHelper(coord, 3, 9)
    elif row_id < 6 and col_id < 3:
        return getSubMatrixSetHelper(coord, 6, 3)
    elif row_id < 6 and col_id < 6:
        return getSubMatrixSetHelper(coord, 6, 6)
    elif row_id < 6 and col_id < 9:
        return getSubMatrixSetHelper(coord, 6, 9)
    elif row_id < 9 and col_id < 3:
        return getSubMatrixSetHelper(coord, 9, 3)
    elif row_id < 9 and col_id < 6:
        return getSubMatrixSetHelper(coord, 9, 6)
    elif row_id < 9 and col_id < 9:
        return getSubMatrixSetHelper(coord, 9, 9)
    return set()


def getSubMatrixSetHelper(coord, row, col):
    tmp = set()
    for i in range(row - 1, row - 1 - 3):
        for j in range(col - 1, col - 1 - 3):
            if coord[0] == i and coord[1] == j:
                continue
            tmp.add(board[i, j])
    return tmp


def main():
    generate_board()
    print(board)
    print()
    solve()
    print(board)
    print()


if __name__ == '__main__':
    main()
