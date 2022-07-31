from enum import Enum, auto
from itertools import product
DIM = 4


class Board():
    def __init__(self):
        self.board = [[Piece(None)] * DIM for row in range(DIM)]
    @staticmethod
    def row_to_string(row):
        return " " + " |  ".join(row)

    def __repr__(self):
         hrule = "\n" + ("-" * 6  + "  ") * DIM + "\n"
         clone_board = self.board[:]

         for row in range(DIM):
             for column in range(DIM):
                clone_board[row][column] = str(self.board[row][column])
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

    def pick():
        pass

    def place_piece():
        pass

    def make_move(game):
        game.choose_piece(int(piece)-1)

class RandomSolver(Player):
    def pick(game):
        pass
        #pick random piece from game.playable_pieces
    def place_piece():
        pass
        #place picked random piece in random spot on board with no other piece on it
        #Perhaps I should keep track of indices

        #Idea: tile class that can have a piece
        #Having a list of playable positions is much easier if I do it like this and it makes my random solver super easy to implemet


class Piece():
    def __init__(self, type):
        self.type = type
        self.played = False
        self.player = None


    def __str__(self):
        if(self.type):
            brackets, close_brackets, fill, height, color = "","","","",""
            representation = f"{brackets}{fill}{height}{color}{close_brackets}"
            if(self.type[0]=="LIGHT"):
                color = "L"
            else:
                color = "D"

            if(self.type[1]=="SHORT"):
                height = "^"
            else:
                height = "_"

            if(self.type[2]=="ROUND"):
                brackets = "["
                close_brackets = "]"
            else:
                brackets = "("
                close_brackets = ")"

            if(self.type[2]=="HOLLOW"):
                fill = "O"
            else:
                fill = "#"
            return representation.format(brackets, fill, height, color, close_brackets)
        else:
            return "    "

COLORS = ["LIGHT", "DARK"]
FILLS = ["HOLLOW", "SOLID"]
HEIGHTS = ["TALL", "SHORT"]
SHAPES = ["ROUND", "SQUARE"]
POSSIBLE_PIECES = [Piece(type) for type in list(product(COLORS, FILLS, HEIGHTS, SHAPES))]
NONE_TUPLE = (None, None, None, None)


POSSIBLE_PIECES[0].type
class Tile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.piece = None

class Game():
    """
    Class handles logic and Board-Player interactions.

    Automatically sets up a two player game of Quarto.

    @param Player player1, the first player to move
    @param Player player2, technically the first player to move in the game, as they must choose p1's piece
    @param board a DIMxDIM string matrix board which will be used to play the game
    @param pieces, a tuple of Piece objects, one of each of type, accessible to both players
    """

    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.board = Board()
        self.playable_pieces = POSSIBLE_PIECES
        self.current_player = self.player2
        self.winnable_positions = [True for i in range(10)]

    #
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


    def place_piece(self,coordinate):
        if(self.current_player.currentPiece==None):
            raise Exception("The player has no current piece.")
        if(self.board.board[coordinate[0]][coordinate[1]].type):
            raise Exception("There is a piece there.")
        else:
            piece = self.current_player.currentPiece
            self.board.board[coordinate[0]][coordinate[1]] = piece
            piece.played = True
            piece.player = self.current_player
            print(f"Piece {piece} has been placed at: {coordinate[0]} , {coordinate[1]}")




    def choose_piece(self, idx):
        [print(piece.played) for piece in POSSIBLE_PIECES]
        #why are 3 already played?
        piece = None
        if(self.current_player==self.player1):
            next_player = self.player2
        else:
            next_player = self.player1

        for i in range(1,len(self.playable_pieces)+1):
            if(not self.playable_pieces[i-1].played):
                print(i, ": ", self.playable_pieces[i-1])
                piece = self.playable_pieces[i-1]

        if(idx < 0 or idx > 15):
            raise Exception("Idx is wrong")
        if(self.playable_pieces[idx].played):
            raise Exception("Piece already played")
        else:
            piece = self.playable_pieces[idx]
        self.current_player.currentPiece = piece
        next_player.currentPiece = piece
        self.current_player = next_player


    def check_types(self, piece1, piece2):
        return piece1.type[0]==piece2.type[0] or piece1.type[1]==piece2.type[1] or piece1.type[2]==piece2.type[2] or piece1.type[3]==piece2.type[3]

    def check_horizontal(self,coordinates):
        x = coordinates[0]
        y = coordinates[1]
        if(self.winnable_positions[x]):
            for i in range(1,DIM-1):
                current_elem = self.board[x][i]
                first_elem = self.board[x][0]

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
                current_elem = self.board[i][y]
                first_elem = self.board[0][y]

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
                current_elem = self.board[i][i]
                first_elem = self.board[0][0]

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
                current_elem = self.board[i][DIM-i-1]
                first_elem = self.board[3][0]

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

g = Game()

# g.play_game()
# print(g.board)
# g.play_game()


"""
S = SOLID
H = HOLLOW
T = TALL
Sh = SHORT
R = ROUND
Sq = SQUARE
L = LIGHT
D = DARK
"""
