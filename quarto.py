from enum import Enum, auto
from itertools import product
import random
DIM = 4

class Piece():
    def __init__(self, type):
        self.type = type

    def __str__(self):
        if(self.type):
            brackets, close_brackets, fill, height, color = "","","","",""
            representation = f"{brackets}{fill}{height}{color}{close_brackets}"
            if(self.type[0]=="LIGHT"):
                color = "L"
            else:
                color = "D"

            if(self.type[2]=="SHORT"):
                height = "_"
            else:
                height = "^"

            if(self.type[3]=="ROUND"):
                brackets = "["
                close_brackets = "]"
            else:
                brackets = "("
                close_brackets = ")"

            if(self.type[1]=="HOLLOW"):
                fill = "□"
            else:
                fill = "▣"

            return  "{brackets}{fill}{height}{color}{close_brackets}".format(brackets=brackets, fill=fill, height=height, color=color, close_brackets=close_brackets)
        else:
            return "    "

COLORS = ["LIGHT", "DARK"]
FILLS = ["HOLLOW", "SOLID"]
HEIGHTS = ["TALL", "SHORT"]
SHAPES = ["ROUND", "SQUARE"]

NONE_TUPLE = (None, None, None, None)

class Tile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.piece = None


class Board():
    # board = [[None] * DIM for i in range(DIM)]
    # for i in range(DIM):
    #     for j in range(DIM):
    #         board[i][j] = Tile(i, j)

    def __init__(self):
        indices = []
        board = [[None] * DIM for i in range(DIM)]
        for i in range(DIM):
            for j in range(DIM):
                board[i][j] = Tile(i, j)
                indices.append((i,j))
        self.board = board
        self.playable_indices = indices

    @staticmethod
    def row_to_string(row):
        return " " + " |  ".join(row)

    def __repr__(self):
         hrule = "\n" + ("-" * 6  + "  ") * DIM + "\n"
         clone_board = self.board[:]

         for row in range(DIM):
             for column in range(DIM):
                clone_board[row][column] = str(self.board[row][column].piece)
         rows_stringy = [Board.row_to_string(clone_board[i]) for i in range(DIM)]
         stringified_board =  hrule.join(rows_stringy)
         return stringified_board

    def __str__(self):
        return repr(self)

    def __getitem__(self, idx):
        return self.board[idx]




class Player():
    def __init__(self):
        self.currentPiece = None

    def choose_piece(self, idx, game):
        piece = None
        next_player = game.determine_next_player()

        for i in range(1,len(game.playable_pieces)+1):
            print(i, ": ", game.playable_pieces[i-1])

        piece = game.playable_pieces[idx]

        if(idx < 0 or idx > 15):
            raise Exception("Idx is wrong")
        else:
            game.playable_pieces.remove(piece)

        next_player.currentPiece = piece
        game.current_player = next_player
        print("CURRENT PLAYER: ", repr(self))
        print("PIECE GIVEN TO " , repr(next_player))


    def place_piece(self,coordinate, game):
        board = game.board.board
        if(self.currentPiece==None):
            print(repr(self))
            raise Exception("The player has no current piece.")
        if(board[coordinate[0]][coordinate[1]].piece):
            raise Exception("There is a piece there.")
        else:
            piece = self.currentPiece
            board[coordinate[0]][coordinate[1]].piece = piece
            game.remove_idx(coordinate)
            print(f"Piece {piece} has been placed at: {coordinate[0]} , {coordinate[1]}")


class RandomSolver(Player):
    def __init__(self):
        self.currentPiece = None

    def choose_piece(self, game):
        if(len(game.playable_pieces) > 0):
            next_player = game.determine_next_player()
            piece = random.choice(game.playable_pieces)
            next_player.currentPiece = piece
            game.current_player = next_player
            print("Random player chose: ", piece)
        else:
            Exception("No more pieces.")
        #pick random piece from game.playable_pieces
    def place_piece(self, game):
        piece = self.currentPiece
        coordinate = random.choice(game.board.playable_indices)
        game.board.board[coordinate[0]][coordinate[1]] = piece
        print(f"Random player placed {piece} at: {coordinate[0]} , {coordinate[1]}")
class Game():
    """
    Class handles logic and Board-Player interactions.

    Automatically sets up a two player game of Quarto.

    @param Player player1, the first player to move
    @param Player player2, technically the first player to move in the game, as they must choose p1's piece
    @param board a DIMxDIM string matrix board which will be used to play the game
    @param pieces, a tuple of Piece objects, one of each of type, accessible to both players
    """

    def __init__(self, p1, p2):
        self.player1 = p1
        self.player2 = p2
        self.board = Board()
        self.playable_pieces = [Piece(type) for type in list(product(COLORS, FILLS, HEIGHTS, SHAPES))]
        self.current_player = p2
        self.winnable_positions = [True for i in range(10)]

    def determine_next_player(self):
        if(self.current_player is self.player1):
            next_player = self.player2
        else:
            next_player = self.player1

        print("NEXT PLAYER IS: " , repr(next_player))
        return next_player

    def remove_idx(self,coord):
        self.board.playable_indices.remove(coord)

    def play_game(self):
        gameOver = False

        #The "second" player chooses a piece for the first
        piece = input("Choose a piece")
        self.choose_piece(int(piece))

        while(not gameOver):
            print(self.board)
            coordinates = input("Enter coordinates.")

            coord = (int(coordinates[0]), int(coordinates[2]))

            print(coord)
            self.place_piece(coord)

            if(self.check_win(coord) or self.check_tie()):
                gameOver = True
                print("Game over")
            piece = input("Choose a piece")
            self.current_player.make_move()
            self.current_player =  self.determine_next_player()

    def check_types(self, piece1, piece2):
        return piece1.type[0]==piece2.type[0] or piece1.type[1]==piece2.type[1] or piece1.type[2]==piece2.type[2] or piece1.type[3]==piece2.type[3]

    def check_horizontal(self,coordinates):
        x = coordinates[0]
        y = coordinates[1]
        if(self.winnable_positions[x]):
            for i in range(1,DIM-1):
                current_elem = self.board[x][i].piece
                first_elem = self.board[x][0].piece

                if(current_elem.type and first_elem.type and not self.check_types(first_elem, current_elem)):
                    self.winnable_positions[x] = False
                    return False
                elif(not current_elem.type):
                    return False
            return True
        return False

    def check_vertical(self, coordinates):
        x = coordinates[0]
        y = coordinates[1]

        if(self.winnable_positions[y+4]):
            for i in range(1,DIM-1):
                current_elem = self.board[i][y].piece
                first_elem = self.board[0][y].piece

                # print(f"CURRENT: {current_elem.type}, f{first_elem.type}")
                if(current_elem.type and first_elem.type and not self.check_types(first_elem, current_elem)):
                        self.winnable_positions[y+4] = False
                        return False
                elif(not current_elem.type):
                    return False
            return True
        return False

    def check_maj_diagonal(self, coordinates):
        if(self.winnable_positions[9]):
            for i in range(1,DIM-1):
                current_elem = self.board[i][i].piece
                first_elem = self.board[0][0].piece

                if(current_elem.type and first_elem.type and not self.check_types(first_elem, current_elem)):
                        self.winnable_positions[8] = False
                        return False
                elif(not current_elem.type):
                    return False
            return True
        return False

    def check_min_diagonal(self, coordinates):
        x = coordinates[0]
        y = coordinates[1]

        if(self.winnable_positions[9]):
            for i in range(DIM-1):
                current_elem = self.board[i][DIM-i-1].piece
                first_elem = self.board[3][0].piece

                if(current_elem.type and first_elem.type and not self.check_types(current_elem, first_elem)):
                        self.winnable_positions[9] = False
                        return False
                elif(not current_elem.type):
                    return False
            return True
        return False


    def check_win(self, coordinates):
        if(self.check_min_diagonal(coordinates) or self.check_maj_diagonal(coordinates) or self.check_horizontal(coordinates) or self.check_vertical(coordinates)):
            return True
        return False

    def check_tie(self):
        return True not in self.winnable_positions

# g.play_game()
# print(g.board)
# g.play_game()

g = Game(Player(), RandomSolver())
p1 = g.player1
p2 = g.player2


p2.choose_piece(g)
p1.place_piece((0,0),g)
p1.choose_piece(1,g)
p2.place_piece(g)

"""
Win If You Can
    > For your piece at a given moment, iterate through the possible indices.
    > If any of them result in a win, play the piece there.
    > Determine by premptively calling check_win with the piece

Dont Lose
    > Dont give your opponent a piece they can win with.
    > Given the list of possible indices, if certain properties result in a win,
     remove all the pieces with those properties from the list of pickable pieces for the turn.

     Possible Bugs:
     > Sometimes you have to give them a winning piece. Never let the pickable pieces list run below 0
"""
