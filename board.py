from texttable import Texttable


class Board:
    def __init__(self):
        self._board = []
        for n in range(6):
            self._board.append([' '] * 6)

    def make_move_on_board(self,row,col,symbol):
        if not int(row) and row!=0 :
            raise ValueError("Invalid row!")
        if not int(col) and col!=0:
            raise ValueError("Invalid column!")
        if row<0 or row>5:
            raise ValueError("Invalid row!")
        if col<0 or col>5:
            raise ValueError("Invalid column!")
        if symbol!='X' and symbol!='O':
            raise ValueError("Invalid symbol!")
        if self._board[row][col]!=' ':
            raise ValueError("The square is already used!")
        self._board[row][col]=symbol

    def get_board(self):
        return self._board

    def __str__(self):
        t = Texttable()
        header = ['X']

        for n in range(6):
            header.append(n)

        t.header(header)
        for n in range(6):
            t.add_row([n] + self._board[n])

        return t.draw()




