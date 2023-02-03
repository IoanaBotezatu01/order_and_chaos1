import board
import random

class Game:
    def __init__(self, board):
        self.__board = board

    def verify_player_win(self):
        counter = 0
        table = self.__board.get_board()
        # testing for rows
        for row in range(6):
            counter = 0
            for col in range(5):
                if table[row][col] == table[row][col + 1] and table[row][col] != ' ':
                    counter += 1
                    if counter == 4:
                        return True
                else:
                    counter = 0
        # testing for columns
        counter = 0
        for col in range(6):
            counter = 0
            for row in range(5):
                if table[row][col] == table[row + 1][col] and table[row][col] != ' ':
                    counter += 1
                    if counter == 4:
                        return True
                else:
                    counter = 0
        counter = 0
        for col in range(5):

            if table[col][col] == table[col + 1][col + 1] and table[col][col] != ' ':
                counter += 1

                if counter == 4:
                    return True
            else:
                counter = 0
        counter = 0
        row = 1
        for col in range(4):
            if table[row][col] == table[row + 1][col + 1] and table[row][col] != ' ':
                counter += 1
                if counter == 4:
                    return True
            else:
                counter = 0
            if row <= 4:
                row += 1
            else:
                break

        row = 0
        counter = 0
        for col in range(1, 5):
            if table[row][col] == table[row + 1][col + 1] and table[row][col] != ' ':
                counter += 1
                if counter == 4:
                    return True
            else:
                counter = 0
            if row <= 3:
                row += 1
            else:
                break
        row = 0
        counter = 0
        for col in range(5, 0, -1):
            if table[row][col] == table[row + 1][col - 1] and table[row][col] != ' ':

                counter += 1
                if counter == 4:
                    return True
            else:
                counter = 0

            if row <= 4:
                row += 1
            else:
                break

        row = 0
        counter = 0
        for col in range(4, 0, -1):
            if table[row][col] == table[row + 1][col - 1] and table[row][col] != ' ':

                counter += 1
                if counter == 4:
                    return True
            else:
                counter = 0

            if row <= 3:
                row += 1
            else:
                break

        row = 1
        counter = 0
        for col in range(5, 1, -1):
            if table[row][col] == table[row + 1][col - 1] and table[row][col] != ' ':

                counter += 1
                if counter == 4:
                    return True
            else:
                counter = 0

            if row <= 4:
                row += 1
            else:
                break


    def verify_computer_win(self):
        table = self.__board.get_board()
        empty_squares = 0
        for row in range(6):
            for column in range(6):
                if table[row][column] == ' ':
                    empty_squares = 1

        if empty_squares == 1:
            return False
        else:
            return True

    def computer_move(self):
        table = self.__board.get_board()
        empty_squares = 0
        move=0

        for row in range(6):
            for col in range(6):
                if table[row][col] == ' ':
                    empty_squares += 1
        if empty_squares == 1:  # TRY TO WIN
            for row in range(6):
                for col in range(6):
                    if table[row][col] == ' ':
                        table[row][col] = 'X'
                        if self.verify_player_win() != True:
                            self.__board.make_move_on_board(row,col,'X')
                            move=1
                        else:
                            table[row][col] = 'O'
                            if self.verify_player_win() != True:
                                self.__board.make_move_on_board(row,col,'O')
                                move=1

                            else:  # if there is one empty square but for any option there will be 5 symbols in a row
                                self.__board.make_move_on_board(row, col,'X')  # the player will still win so we put 'X'
                                move=1

        else:  # if there are more empty squares,the computers tries to make the player lose
            for row in range(6):
                for col in range(6):
                    if table[row][col] == ' ':
                        table[row][col] = 'X'
                        if self.verify_player_win() == True:  # verify if player wins for 'X' is that square
                            table[row][col] = 'O'    #the computer verifies if the same place makes player win for 'O'
                            if self.verify_player_win() == True:  # the player wins ,so computer verifies other places
                                   table[row][col] = ' '
                            else:
                                self.__board.make_move_on_board(row,col,'O')
                                move=1
                        else:  # verify if player wins for 'O' in that empty square
                            table[row][col] = 'O'  # the computer already verified if player wins for 'X',which is False
                            if self.verify_player_win() == True:  # if the player wins for 'O',the computer puts 'X'
                                table[row][col]=' '
                                self.__board.make_move_on_board(row, col, 'X')
                                move=1
                            else:
                                table[row][col] = ' '



        if move==0:     #if no move was made,the computer places randomly

            row=random.randint(0,5)
            col=random.randint(0,5)
            symbol=random.choice(['X','O'])
            if table[row][col]==' ':
                self.__board.make_move_on_board(row,col,symbol)
            else:
                while True:
                    row=random.randint(0,5)
                    col=random.randint(0,5)
                    symbol=random.choice(['X','O'])
                    if table[row][col]==' ':
                        self.__board.make_move_on_board(row,col,symbol)
                        break

