from board import Board
from ui import Ui
from game import  Game
def main():
    board=Board()
    game = Game(board)
    ui=Ui(board,game)


    ui.run()


if __name__=="__main__":
    main()