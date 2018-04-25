#Calvin Lui 84152100 & Nicholas sprague 49389270 lab section
import connectfour
import connectfour_tools
import net_tools

#todo: make server do moves, change console version to have help menu in the move inputting

def check_input(connection:"list of socket info",test:str)->None:
    try:
        assert net_tools.receive_input(connection) == test
    except:
        net_tools.close_connection(connection)
        
def server_move(game:"GameState",connection:"list of socket info")->"GameState":
    """Takes move from server and interprets it"""
    
    inp = net_tools.receive_input(connection).split()
    if inp[0] == 'DROP':
        game = connectfour.drop(game,int(inp[1])-1)
    elif inp[0] == "POP":
        game = connectfour.pop(game,int(inp[1])-1)
    else:
        net_tools.close_connection(connection)
    return game

def user_input(connection:"list of socket info")->str:
    """asks user's input and sends to server, returns move"""
    move = ""
    while not connectfour_tools.valid_input(move):
        move = input('input move (type help for info): ')
        if move.lower() == 'help':
            print("type d to drop a piece or p to pop a piece from the bottom of a column\nfollowed by a space and a column number")
    if move[0] == 'd':
        net_tools.send_output(connection,"DROP %s"%move[2:])
    else:
        net_tools.send_output(connection,"POP %s"%move[2:])
    return move

def user_move(game:"GameState",move:str)->"GameState":
    """updates local game board"""
    if move[0] == 'd':
        game = connectfour.drop(game,int(move[2:])-1)
    else:
        game = connectfour.pop(game,int(move[2:])-1)
    return game

def main():
    connection = net_tools.connect()
    user = input("please input a username: ")
    net_tools.send_output(connection,"I32CFSP_HELLO " + user)
    check_input(connection,"WELCOME " + user)
    net_tools.send_output(connection,"AI_GAME")
    #check_input(connection,"READY")

    game = connectfour.new_game()
    while True:
        response = net_tools.receive_input(connection)
        if response == "READY":
            move = user_input(connection)
            response = net_tools.receive_input(connection)
            if response == "OKAY":
                game = user_move(game,move)
                connectfour_tools.print_game(game)
                game = server_move(game,connection)
                connectfour_tools.print_game(game)
            elif response == "INVALID":
                print("Invalid move")
            elif response == "WINNER_RED":
                break
            else:
                print('Sorry! something went wrong with the server.')
                net_tools.close_connection(connection)
        elif response == "WINNER_YELLOW":
            break
        else:
            print('Sorry! something went wrong with the server.')
            net_tools.close_connection(connection)
    print(response)
    connectfour_tools.print_game(game)
    net_tools.close_connection(connection)

if __name__ == "__main__":
    main()
    
