#Calvin Lui 84152100
import Othello_class

def inp(if_condition:bool,error_str:str):
    '''generalized function for requesting input'''
    while True:
        user_inp = input()     
        if if_condition(user_inp):
            return user_inp
        else:
            print(error_str)
            
def can_int(text:str)->bool:
    '''checks if a string can be converted to an int'''
    try:
        int(text)
    except ValueError:
        return False
    else:
        return True
    
def ask_num(comparison:bool,error_message:str)->int:
    "asks for a number and converts the input string into an int"
    return int(inp(comparison,error_message))

def ask_BW(condition:bool,error_message:str)->int:
    "asks for either a B or W and returns the corresponding integer value"
    response = inp(condition,error_message)
    ret = 1
    if response == "B":
        ret = 2    
    return ret

def ask_str(condition:bool,error_message:str)->str:
    '''asks for a string using the generic input function'''
    return inp(condition,error_message)

def row_col_inp(text:str)->tuple:
    '''converts the input into ints for row and col'''
    num = text.split()
    row = int(num[0])-1
    col = int(num[1])-1
    return (row,col)

def winner(text:str,count:tuple)-> str:
    '''picks winner based on the winning condition set'''
    if text == '>':
        if count[0] > count[1]:
            return 'B'
        elif count[0] < count[1]:
            return 'W'
    elif text == '<':
        if count[0] < count[1]:
            return 'B'
        elif count[0] > count[1]:
            return 'W'
    return 'NONE'
        
def print_piece_count(game:'Othello_Gamestate')->None:
    '''takes an othello game object and returns the count of the pieces
       on the board'''
    count = game.count()
    print("B: {}  W: {}".format(count[0],count[1]))

def print_turn(game:'Othello_Gamestate')->None:
    '''prints the turn in the correct format'''
    turn = 'B'
    if game._turn == 1:
        turn = 'W'
    print("TURN:",turn)

def Othello_move(game:'Othello_Gamestate')->None:
    '''takes a players input and makes a move on the othello game passed in the parameter'''
    while True:
        player_move = row_col_inp(input())
        if game.is_valid_move(game._turn,player_move[0],player_move[1]):
            print("VALID")
            game.Make_move(player_move[0],player_move[1])
            break
        else:
            print("INVALID")

if __name__ == "__main__":
    print("FULL")
    row = ask_num(lambda x:can_int(x) and int(x) >= 4 and int(x) <= 16,'sorry invalid number')
    col = ask_num(lambda x:can_int(x) and int(x) >= 4 and int(x) <= 16,'sorry invalid number')
    first = ask_BW(lambda x: x in ['B','W'],'sorry invalid input')
    arrangement = ask_BW(lambda x: x in ['B','W'],'sorry invalid input')
    game_win = ask_str(lambda x: x in ['>','<'],'sorry invalid input')
    game = Othello_class.Othello_Gamestate(row,col,first,arrangement)
    
    while not game._gameover:
        print_piece_count(game)
        game.print_board()
        if not game.more_moves(game._turn):
            game.switch_turn()
        print_turn(game)
        Othello_move(game)
        
    print_piece_count(game)
    game.print_board()
    print("WINNER: " + winner(game_win,game.count()))
    
    
