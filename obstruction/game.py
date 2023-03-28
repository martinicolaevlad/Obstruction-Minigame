import random

from src.obstruction.exceptions import RowError, ColumnError


class Game:
    def __init__(self, the_board):
        self.__game_board = the_board

    def someone_won_the_game(self):
        """
        someone won if the board is full
        :return: true if the board is full else return false
        """
        return self.__game_board.check_if_board_is_full()

    def get_the_game_board(self):
        """
        :return: the board in string representation
        """
        return self.__game_board.board_to_str()

    def human_move(self, x, y, value):
        """
        :param x: row
        :param y: column
        :param value: x or 0
        """
        if x < 0 or x > 5:
            raise RowError("x must be between 0 and 5")
        if y < 0 or y > 5:
            raise ColumnError("y must be between 0 and 5")

        self.__game_board.set_board_value(x, y, value)

    def computer_move(self, value):
        """
        The computer will try to find an ideal position to place the value and will try to cover around this value
        as many positions on the table as is possible, and after we find the ideal spot the value will be set.
        :param value: x or 0
        """

        larger_number_of_fields_covered, best_row, best_column = 0, 0, 0

        for row in range(6):
            for column in range(6):
                empty_fields = 0
                if self.__game_board.get_table_position_value(row, column) == 0:
                    empty_fields += 1
                    if row - 1 >= 0:
                        if self.__game_board.get_table_position_value(row - 1, column) == 0:
                            empty_fields += 1
                        if column + 1 <= 5 and self.__game_board.get_table_position_value(row - 1, column + 1) == 0:
                            empty_fields += 1
                        if column - 1 >= 0 and self.__game_board.get_table_position_value(row - 1, column - 1) == 0:
                            empty_fields += 1
                    if row + 1 <= 5:
                        if self.__game_board.get_table_position_value(row + 1, column) == 0:
                            empty_fields += 1
                        if column + 1 <= 5 and self.__game_board.get_table_position_value(row + 1, column + 1) == 0:
                            empty_fields += 1
                        if column - 1 >= 0 and self.__game_board.get_table_position_value(row + 1, column - 1) == 0:
                            empty_fields += 1
                    if column - 1 >= 0 and self.__game_board.get_table_position_value(row, column - 1) == 0:
                        empty_fields += 1
                    if column + 1 <= 5 and self.__game_board.get_table_position_value(row, column + 1) == 0:
                        empty_fields += 1

                    if empty_fields > larger_number_of_fields_covered:
                        larger_number_of_fields_covered = empty_fields
                        best_row = row
                        best_column = column
        self.__game_board.set_board_value(best_row, best_column, value)

    def move_computer_first_position_random(self, value):
        """
        if the computer is the first player, the first position will be set randomly
        :param value: X or O
        """
        self.__game_board.set_board_value(random.randint(0, 5), random.randint(0, 5), value)