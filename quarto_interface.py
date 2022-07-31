import re

ERROR_MESSAGES =  {
    0: "\n🤓 <Invalid Move: A player cannot move twice in a row!)\n",
    1: "\n🤓 <Invalid Move: That coordinate is out of bounds!)\n",
    2: "\n🤓 <Invalid Move: There's already a player at that spot!)\n",
    3: "\n🤓 <Your coordinates are not formatted correctly. Please try again.)\n"
    }

DIM = 4
MAX_IDX = 7
MIN_IDX = 0
def prompt_turn(player, board):
    match = False

    while(match is False):
        print(board)
        response = input(f"Please select a coordinate to play. Separate coordinates with a comma like so: \"a,b\":\n" )
        coord_pattern = "(\d+),(\d+)"
        match = re.search(coord_pattern, response)

        if(match):
            string_tuple = match.group(1,2)
            coord = (int(string_tuple[0]), int(string_tuple[1]))
            return coord
        else:
            show_error(3)

def win_message(win_code, player):
    if(win_code.name=="TIE"):
        print(f"Players have tied!")
    if(win_code.name=="WIN"):
        print(f"Player {player.name} has won the game!")

def show_error(error_code):
    print(ERROR_MESSAGES.get(error_code))
