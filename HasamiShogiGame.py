# Name: Catherine Potgieter
# Course: CS 162
# Portfolio Project
# Description: This file contains a class named HasamiShogiGame for playing an abstract board game called hasami shogi.
# It uses the rules for "Variant 1" on the Wikipedia page (https://en.wikipedia.org/wiki/Hasami_shogi),
# including the diagram of the starting position.

class HasamiShogiGame:
    """A class that initializes a game of Hasami Shogi """

    def __init__(self):
        """Initialization function that """
        self._game_state = 'UNFINISHED'  # the three possible values: 'UNFINISHED','RED_WON' or 'BLACK_WON'
        self._active_player = 'BLACK'
        self._red_capture_count = 0
        self._black_capture_count = 0
        self._board = [['RED', 'RED', 'RED', 'RED', 'RED', 'RED', 'RED', 'RED', 'RED'],  # a
                       ['_', '_', '_', '_', '_', '_', '_', '_', '_'],  # b
                       ['_', '_', '_', '_', '_', '_', '_', '_', '_'],  # c
                       ['_', '_', '_', '_', '_', '_', '_', '_', '_'],  # d
                       ['_', '_', '_', '_', '_', '_', '_', '_', '_'],  # e
                       ['_', '_', '_', '_', '_', '_', '_', '_', '_'],  # f
                       ['_', '_', '_', '_', '_', '_', '_', '_', '_'],  # g
                       ['_', '_', '_', '_', '_', '_', '_', '_', '_'],  # h
                       ['BLACK', 'BLACK', 'BLACK', 'BLACK', 'BLACK', 'BLACK', 'BLACK', 'BLACK', 'BLACK']]  # i

    def get_game_state(self):
        """Takes no parameters and returns 'UNFINISHED', 'RED_WON' or 'BLACK_WON'."""
        return self._game_state

    def set_game_state(self, new_state):
        """Takes a game state parameter either 'RED_WON' or 'BLACK_WON, and sets the game state to that parameter"""
        self._game_state = new_state

    def get_active_player(self):
        """takes no parameters and returns whose turn it is - either 'RED' or 'BLACK'. """
        return self._active_player

    def set_active_player(self, player):
        """ Takes a player parameter - either 'RED' or 'BLACK' - and updates the active player"""
        self._active_player = player

    def get_num_captured_pieces(self, player):
        """takes one parameter, 'RED' or 'BLACK', and returns the number of pieces of that
        color that have been captured. """
        if player == 'RED':
            return self._red_capture_count
        if player == 'BLACK':
            return self._black_capture_count
        else:
            print('Player input must be RED or BLACK')

    def set_captured_pieces(self, player, num_pieces):
        """Takes in a player parameter - either 'RED' or 'BLACK' -  and updates the capture count
        of that player to be the num_pieces.   """
        if player == 'RED':
            self._red_capture_count = num_pieces
            return
        if player == 'BLACK':
            self._black_capture_count = num_pieces
            return
        else:
            print('Error - Check parameters')

    def get_square_occupant(self, square_string):
        """takes one parameter, a string representing a square (such as 'i7'), and returns 'RED', 'BLACK', or 'NONE',
        depending on whether the specified square is occupied by a red piece, a black piece, or neither. """
        # rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        # y_axis = 0
        # for row in rows:
        #     while square_string[0] == row:
        #         y_axis += 1

        x_axis = int(square_string[1]) - 1
        y_axis = 0

        if square_string[0] == 'a':
            y_axis = 0
        if square_string[0] == 'b':
            y_axis = 1
        if square_string[0] == 'c':
            y_axis = 2
        if square_string[0] == 'd':
            y_axis = 3
        if square_string[0] == 'e':
            y_axis = 4
        if square_string[0] == 'f':
            y_axis = 5
        if square_string[0] == 'g':
            y_axis = 6
        if square_string[0] == 'h':
            y_axis = 7
        if square_string[0] == 'i':
            y_axis = 8

        board = self._board
        if board[y_axis][x_axis] == '_':
            return 'NONE'
        else:
            return board[y_axis][x_axis]

    def set_square_occupant(self, player_value, square_string):
        """Takes as parameters a player - either 'RED', 'BLACK' or 'NONE', and a string representing a square
        (such as 'i7'). Updates that square with the player value """

        x_axis = int(square_string[1]) - 1
        y_axis = 0

        if square_string[0] == 'a':
            y_axis = 0
        if square_string[0] == 'b':
            y_axis = 1
        if square_string[0] == 'c':
            y_axis = 2
        if square_string[0] == 'd':
            y_axis = 3
        if square_string[0] == 'e':
            y_axis = 4
        if square_string[0] == 'f':
            y_axis = 5
        if square_string[0] == 'g':
            y_axis = 6
        if square_string[0] == 'h':
            y_axis = 7
        if square_string[0] == 'i':
            y_axis = 8

        board = self._board
        board[y_axis][x_axis] = player_value

    def make_move(self, move_from, move_to):
        """Takes two parameters - two strings (such as 'i7' and 'i9') representing the square moved from and
        the square moved to. Note: the pieces can only move diagonally and horizontally."""
        player = self.get_active_player()
        # Verify the game is unfinished
        if self.get_game_state() != 'UNFINISHED':
            print('this game has a winner - use the get_game_state method to see who won')
            return False

        # Verify valid move
        if move_from[0] > 'i':
            print("invalid move")
            return False
        if move_to[0] > 'i':
            print("invalid move")
            return False
        if len(move_from) > 2:
            print("invalid move")
            return False
        if move_to == move_from:
            print("this 'move' keeps the piece in the same position")
            return False

        # Verify that move is either horizontal or vertical
        if move_from[0] == move_to[0]:
            return self.validate_move_horizontal(player, move_from, move_to)
        if move_from[1] == move_to[1]:
            return self.validate_move_vertical(player, move_from, move_to)
        else:
            print("Invalid move: player may only move diagonally and horizontally")
            return False

    def validate_move_horizontal(self, player, move_from, move_to):
        """Takes in as parameters the active player ('RED' or 'BLACK') and two strings (such as 'i7' and 'i9')
        representing the square moved from and the square moved to."""
        y_axis = 0
        move_from_x = int(move_from[1]) - 1
        move_to_x = int(move_to[1]) - 1
        board = self._board

    # Establish y_axis
        if move_to[0] == 'a':
            y_axis = 0
        if move_to[0] == 'b':
            y_axis = 1
        if move_to[0] == 'c':
            y_axis = 2
        if move_to[0] == 'd':
            y_axis = 3
        if move_to[0] == 'e':
            y_axis = 4
        if move_to[0] == 'f':
            y_axis = 5
        if move_to[0] == 'g':
            y_axis = 6
        if move_to[0] == 'h':
            y_axis = 7
        if move_to[0] == 'i':
            y_axis = 8

        # Verify that the player has a piece on the move_from square
        if board[y_axis][move_from_x] != player:
            print('Player does not have a piece in the starting position')
            return False

        # Verify that the move_to square is empty
        if board[y_axis][move_to_x] != '_':
            print('There is already a piece on the spot you want to move to')
            return False

        # Check to see if there are any players along the path of move_from to move_from
        # going left?
        if move_from_x > move_to_x:
            current_column = move_from_x - 1
            while current_column != move_to_x:
                if board[y_axis][current_column] != '_':
                    print('path not clear')
                    return False
                current_column = current_column - 1

        # going right?
        if move_from_x < move_to_x:
            current_column = move_from_x + 1
            while current_column != move_to_x:
                if board[y_axis][current_column] != '_':
                    print('path not clear')
                    return False
                current_column = current_column + 1

        # Move the piece
        board[y_axis][move_from_x] = '_'
        board[y_axis][move_to_x] = player

        return self.capture_check(player, move_to)

    def validate_move_vertical(self, player, move_from, move_to):
        """Takes in as parameters the active player ('RED' or 'BLACK') and two strings (such as 'i7' and 'a7')
        representing the square moved from and the square moved to."""
        board = self._board
        move_from_y = 0
        move_to_y = 0
        x_axis = int(move_from[1]) - 1  # since this is a vertical move the x-axis should not change
                                        # between move_from and move_to

        # Establish move_to y_axis
        if move_to[0] == 'a':
            move_to_y = 0
        if move_to[0] == 'b':
            move_to_y = 1
        if move_to[0] == 'c':
            move_to_y = 2
        if move_to[0] == 'd':
            move_to_y = 3
        if move_to[0] == 'e':
            move_to_y = 4
        if move_to[0] == 'f':
            move_to_y = 5
        if move_to[0] == 'g':
            move_to_y = 6
        if move_to[0] == 'h':
            move_to_y = 7
        if move_to[0] == 'i':
            move_to_y = 8

        # Establish move_from y_axis
        if move_from[0] == 'a':
            move_from_y = 0
        if move_from[0] == 'b':
            move_from_y = 1
        if move_from[0] == 'c':
            move_from_y = 2
        if move_from[0] == 'd':
            move_from_y = 3
        if move_from[0] == 'e':
            move_from_y = 4
        if move_from[0] == 'f':
            move_from_y = 5
        if move_from[0] == 'g':
            move_from_y = 6
        if move_from[0] == 'h':
            move_from_y = 7
        if move_from[0] == 'i':
            move_from_y = 8

        # Verify that the player has a piece on the move_from square
        if board[move_from_y][x_axis] != player:
            print('Player does not have a piece in the starting position')
            return False

        # Verify that the move_to square is empty
        if board[move_to_y][x_axis] != '_':
            print('There is already a piece on the spot you want to move to')
            return False

        # Check to see if there are any players along the path of move_from to move_from
        # going up?
        if move_from_y > move_to_y:
            current_row = move_from_y - 1
            while current_row != move_to_y:
                if board[current_row][x_axis] != '_':
                    print('path not clear')
                    return False
                current_row = current_row - 1

        # going down?
        if move_from_y < move_to_y:
            current_row = move_from_y + 1
            while current_row != move_to_y:
                if board[current_row][x_axis] != '_':
                    print('path not clear')
                    return False
                current_row = current_row + 1

        # Move the piece
        board[move_from_y][x_axis] = '_'
        board[move_to_y][x_axis] = player

        return self.capture_check(player, move_to)

    def capture_check(self, player, move_to):
        """ """
        board = self._board
        x_axis = int(move_to[1]) - 1
        y_axis = 0

        # Establish y_axis
        if move_to[0] == 'a':
            y_axis = 0
        if move_to[0] == 'b':
            y_axis = 1
        if move_to[0] == 'c':
            y_axis = 2
        if move_to[0] == 'd':
            y_axis = 3
        if move_to[0] == 'e':
            y_axis = 4
        if move_to[0] == 'f':
            y_axis = 5
        if move_to[0] == 'g':
            y_axis = 6
        if move_to[0] == 'h':
            y_axis = 7
        if move_to[0] == 'i':
            y_axis = 8

        # Establish the opponent
        opponent = None
        if player == 'RED':
            opponent = 'BLACK'
        if player == 'BLACK':
            opponent = 'RED'

        # Check up
        capture_up = []
        current_row = y_axis - 1
        if y_axis > 0:
            while current_row > 0 and board[current_row][x_axis] == opponent:
                coord = str(current_row) + str(x_axis)
                capture_up.append(coord)
                current_row = (current_row - 1)
            if board[current_row][x_axis] == '_':
                capture_up = []

        # Check down
        capture_down = []
        current_row = y_axis + 1
        if current_row < 8:
            while current_row > 9 and board[current_row][x_axis] == opponent:
                coord = str(current_row) + str(x_axis)
                capture_down.append(coord)
                current_row = (current_row + 1)

            if board[current_row][x_axis] == '_' or current_row < 7:
                capture_down = []

        # Check left
        capture_lft = []
        current_col = x_axis - 1
        if x_axis > 0:
            while current_col > 0 and board[y_axis][current_col] == opponent:
                coord = str(y_axis) + str(current_col)
                capture_lft.append(coord)
                current_col = current_col - 1
            if board[y_axis][current_col] == '_':
                capture_lft = []

        # Check right
        capture_rt = []
        current_col = x_axis + 1
        if current_col < 8:
            while current_col < 9 and board[y_axis][current_col] == opponent:
                coord = str(y_axis) + str(current_col)
                capture_rt.append(coord)
                current_col = current_col + 1
            if board[y_axis][current_col] == '_':
                capture_rt = []

        # Check corner capture
        corner_cap_moves = ['a2', 'a8', 'b1', 'b9', 'h1', 'h9', 'i2', 'i8']
        corner_captures = []
        if move_to in corner_cap_moves:
            if move_to == 'a2':                                      # Capture a piece in the a1 corner
                if self.get_square_occupant('a1') == opponent:
                    if self.get_square_occupant('b1') == player:
                        corner_captures.append('00')
            if move_to == 'b1':
                if self.get_square_occupant('a1') == opponent:
                    if self.get_square_occupant('a2') == player:
                        corner_captures.append('00')

            if move_to == 'a8':                                      # Capture a piece in the a9 corner
                if self.get_square_occupant('a9') == opponent:
                    if self.get_square_occupant('b9') == player:
                        corner_captures.append('08')
            if move_to == 'b9':
                if self.get_square_occupant('a9') == opponent:
                    if self.get_square_occupant('a8') == player:
                        corner_captures.append('08')

            if move_to == 'h1':                                     # Capture a piece in the i1 corner
                if self.get_square_occupant('i1') == opponent:
                    if self.get_square_occupant('i2') == player:
                        corner_captures.append('80')
            if move_to == 'i2':
                if self.get_square_occupant('i1') == opponent:
                    if self.get_square_occupant('h1') == player:
                        corner_captures.append('80')

            if move_to == 'i8':                                     # Capture a piece in the i9 corner
                if self.get_square_occupant('i9') == opponent:
                    if self.get_square_occupant('h9') == player:
                        corner_captures.append('88')
            if move_to == 'h9':
                if self.get_square_occupant('i9') == opponent:
                    if self.get_square_occupant('i8') == player:
                        corner_captures.append('88')

        # Gather the 'coordinates' of the eligible captures
        total_captures_coord = []
        if capture_up != []:
            for item in capture_up:
                total_captures_coord.append(item)

        if capture_down != []:
            for item in capture_down:
                total_captures_coord.append(item)

        if capture_rt != []:
            for item in capture_rt:
                total_captures_coord.append(item)

        if capture_lft != []:
            for item in capture_lft:
                total_captures_coord.append(item)

        if corner_captures != []:
            for item in corner_captures:
                total_captures_coord.append(item)

        # Get the count of total captures and add them to the players capture count
        total_captures_num = len(total_captures_coord) + self.get_num_captured_pieces(opponent)
        self.set_captured_pieces(opponent, total_captures_num)

        # Remove the captured pieces
        for piece in total_captures_coord:
            y_coord = int(piece[0])
            x_coord = int(piece[1])
            board[y_coord][x_coord] = '_'

        # update game_status if needed
        if self.get_num_captured_pieces(opponent) >= 8:
            if player == 'RED':
                self.set_game_state('RED_WON')
            if player == 'BLACK':
                self.set_game_state('BLACK_WON')

        # Set active player to be the next player
        self.set_active_player(opponent)

        # Signify that the turn is over by returning True
        return True


# game = HasamiShogiGame()
# move_result = game.make_move('i1', 'e1')
# print(game.get_num_captured_pieces('RED'))
# print(game.get_active_player())
# print(game.get_square_occupant('a4'))
# print(game.get_game_state())
