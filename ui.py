from board import Board

class Ui:
    def __init__(self,board,game):
        self.__board=board
        self.__game=game

    def run(self):
        print(self.__board)
        while True:
            option=input("Order moves (row,col,symbol):")
            option=option.split(',')
            if len(option)!=3:
                while True:
                    print("Wrong input!")
                    option = input("Order moves (row,col,symbol):")
                    option = option.split(',')
                    if len(option)==3:
                        break

            try:
                self.__board.make_move_on_board(int(option[0]),int(option[1]),option[2])
                self.__game.computer_move()
            except ValueError as ve:
                print(ve)




            print(self.__board)

            if self.verify()==True:
                return



    def verify(self):
        verify = self.__game.verify_player_win()
        if verify == True:
            print("Human Wins!")
            return True
        else:
            verify = self.__game.verify_computer_win()
            if verify == True:
                print("Computer Wins!")
                return True