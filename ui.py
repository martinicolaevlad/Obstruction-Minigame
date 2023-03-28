from src.obstruction.exceptions import RowError, ColumnError, PositionAlreadyFilledError


class Ui:
    def __init__(self, the_game):
        self.__game = the_game

    @staticmethod
    def read_position():
        row = int(input("row = "))
        column = int(input("column = "))
        return row, column

    def start_game(self):
        first_player = input("Do you want to play first?  (yes/no) :")

        moves = 0
        if first_player == "yes":
            is_human_turn = True
        else:
            is_human_turn = False

        while self.__game.someone_won_the_game() is False:
            print("Game board:")
            print(self.__game.get_the_game_board())

            try:
                if is_human_turn:
                    row, column = self.read_position()
                    self.__game.human_move(row, column, 'X')
                    moves += 1
                else:
                    if moves == 0:
                        self.__game.move_computer_first_position_random('O')
                    else:
                        self.__game.computer_move('O')

                if self.__game.someone_won_the_game():
                    print("Game board:")
                    print(self.__game.get_the_game_board())
                    if is_human_turn:
                        print("You win!")
                    else:
                        print("I win!")
                is_human_turn = not is_human_turn

            except ValueError:
                print("The row and the column must be between 0 and 5")
            except RowError:
                print("The row must be between 0 and 5")
            except ColumnError:
                print("The column must be between 0 and 5")
            except PositionAlreadyFilledError:
                print("You can't use this position, is already filled")



