#Calvin Lui 84152100 & Nicholas sprague 49389270 lab section
import connectfour
import connectfour_tools


def input_move(game:"GameState")->"GameState":
    if game.turn == connectfour.RED:
        turn = "RED"
    else:
        turn = "YELLOW"
    while True:
        while True:
            move = input("{}'s turn, input move (type help for info): ".format(turn))
            if connectfour_tools.valid_input(move):
                break
            elif move.lower()=='help':
                print("type d to drop a piece or p to pop a piece from the bottom of a column\nfollowed by a space and a column number")
            else:
                print("invalid input")
        try:
            if move[0] == 'd':
                return connectfour.drop(game, int(move[2:])-1)
            else:
                return connectfour.pop(game, int(move[2:])-1)
        except:
            print("Invalid move, go somewhere else.")

def main():
    game = connectfour.new_game()
    while True:
        game = input_move(game)
        connectfour_tools.print_game(game)
        if connectfour.winner(game) == connectfour.RED:
            print("RED wins! Congratulations!")
            break
        elif connectfour.winner(game) == connectfour.YELLOW:
            print("YELLOW wins! Congratulations!")
            break

if __name__ == "__main__":
    main()
