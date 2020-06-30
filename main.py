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


generate_board()
