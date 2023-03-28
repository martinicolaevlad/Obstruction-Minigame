from src.obstruction.exceptions import PositionAlreadyFilledError


class Board:
    def __init__(self):
        self.__board = [[0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0]]

    def get_table_position_value(self, x, y):
        """
        :param x: row
        :param y: column
        :return: the value from the table from position: row-x and column-y
        """
        return self.__board[x][y]

    def set_board_value(self, x, y, value):
        """
        set x or y on a position and a border around this position
        :param x: row
        :param y: column
        :param value: x or y
        """
        if self.get_table_position_value(x, y) != 0:
            raise PositionAlreadyFilledError("invalid position")

        self.__board[x][y] = value

        if x - 1 >= 0:
            self.__board[x - 1][y] = '*'
            if y + 1 <= 5:
                self.__board[x - 1][y + 1] = '*'
            if y - 1 >= 0:
                self.__board[x - 1][y - 1] = '*'

        if y - 1 >= 0:
            self.__board[x][y - 1] = '*'

        if x + 1 <= 5:
            self.__board[x + 1][y] = '*'
            if y - 1 >= 0:
                self.__board[x + 1][y - 1] = '*'
            if y + 1 <= 5:
                self.__board[x + 1][y + 1] = '*'

        if y + 1 <= 5:
            self.__board[x][y + 1] = '*'

    def check_if_board_is_full(self):
        """
        :return: true if the board is full else return false
        """
        for row in range(6):
            for column in range(6):
                if self.get_table_position_value(row, column) == 0:
                    return False
        return True

    def board_to_str(self):
        """
        convert the numeric board list to a string representation
        :return: the string board
        """
        column_indicator = 0
        board = "  0 1 2 3 4 5 \n"
        for row in range(6):
            board += str(column_indicator)
            board += ' '
            column_indicator += 1
            for column in range(6):

                if self.get_table_position_value(row, column) == 0:
                    board += '_ '
                else:
                    board += self.get_table_position_value(row, column)
                    board += ' '
            board += '\n'
        return board