from unittest import TestCase

from sudoku import Sudoku, randomise_board, print_board


class TestSudoku(TestCase):
    def test_solve(self):
        board = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [4, 5, 6, 7, 8, 9, 1, 2, 3],
                 [7, 8, 9, 1, 2, 3, 4, 5, 6],
                 [2, 3, 4, 5, 6, 7, 8, 9, 1],
                 [5, 6, 7, 8, 9, 1, 2, 3, 4],
                 [8, 9, 1, 2, 3, 4, 5, 6, 7],
                 [3, 4, 5, 6, 7, 8, 9, 1, 2],
                 [6, 7, 8, 9, 1, 2, 3, 4, 5],
                 [9, 1, 2, 3, 4, 5, 6, 7, 8]]
        r = randomise_board(board)
        print_board("Randomised Sudoku Board:", r)
        s = Sudoku(r)
        s.solve()
        print_board("Completed Sudoku Board:", s.get_board())
        self.assertListEqual(board, s.get_board())
