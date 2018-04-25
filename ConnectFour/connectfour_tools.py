#Calvin Lui 84152100 & Nicholas sprague 49389270 lab section
import connectfour

def print_game(game:"GameState")-> None:
    """prints a readable game board to console"""
    for col in range(connectfour.BOARD_COLUMNS):
        print(str(col+1)+" ",end="")
    print()
    for row in range(connectfour.BOARD_ROWS):
        for column in range(connectfour.BOARD_COLUMNS):
            if game.board[column][row] == connectfour.NONE:
                x = "."
            elif game.board[column][row] == connectfour.RED:
                x = "R"
            else:
                x = "Y"
            print(x + " ",end = "")
        print()

def valid_input(move:str) -> bool:
    '''determines if given string is a possible move, returns bool'''
    try:
        if move[0] != "d" and move[0] != "p":
            return False
        if move[1] != " ":
            return False
        if not move[2:].isdigit():
            return False
        return True
    except:
        return False

