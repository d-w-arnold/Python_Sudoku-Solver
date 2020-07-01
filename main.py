from sudoku import Sudoku


def main():
    sudoku = Sudoku()
    sudoku.print_board()
    sudoku.solve()
    sudoku.print_board()


if __name__ == '__main__':
    main()
