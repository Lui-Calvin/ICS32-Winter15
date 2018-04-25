#Calvin Lui 84152100

NONE = 0
WHITE = 1
BLACK = 2
#NOTE the coordinate system is down the number of columns and left the number of rows

class Othello_Gamestate:
    def __init__(self,col:int,row:int,turn:int,Arrangement:int):
        """assigns all the variables"""
        self._NUM_ROW = row
        self._NUM_COL = col
        self._BOARD = []
        self._turn = turn
        self._gameover = False
        for row in range(self._NUM_ROW):
            row = []
            for col in range(self._NUM_COL):
                row.append(NONE)
            self._BOARD.append(row)
        self.Board_arrange(Arrangement)

    def Board_arrange(self,Arrangement:int)-> None:
        """puts the specified color(BLACK = 1, WHITE = 2) in the top-left position in the middle
        of the board, and sets it up accordingly"""
        first_pos = WHITE
        second_pos = BLACK
        if Arrangement == BLACK:
            first_pos = BLACK
            second_pos = WHITE
        self._BOARD[int(self._NUM_COL/2-1)][int(self._NUM_ROW/2-1)] = first_pos
        self._BOARD[int(self._NUM_COL/2)][int(self._NUM_ROW/2)] = first_pos
        self._BOARD[int(self._NUM_COL/2)][int(self._NUM_ROW/2-1)] = second_pos
        self._BOARD[int(self._NUM_COL/2-1)][int(self._NUM_ROW/2)] = second_pos

    def print_board(self)->None:
        '''prints out readable board onto the console'''
        for col in self._BOARD:
            for row in col:
                item = "."
                if row == BLACK:
                    item = 'B'
                elif row == WHITE:
                    item = 'W'
                elif row == HIGHLIGHT:
                    item = "*"
                print(item,end = " ")
            print()

    def switch_turn(self):
        '''switches turns'''
        if self._turn == WHITE:
            self._turn = BLACK
        else:
            self._turn = WHITE

    def within_board(self,col:int,row:int)->bool:
        '''checks to see if a point is within the board'''
        if row < self._NUM_ROW and row >= 0 and col < self._NUM_COL and col >= 0:
            return True
        return False

    def check_line(self,color:int,col:int,row:int,direction:tuple)->bool:
        '''takes a point and checks the adjacent point in the specified direction
           and recursively calls this function to see if there is a matching game piece
           that can make this a valid line in othello'''        
        adjacent_col = col + direction[0]
        adjacent_row = row + direction[1]
        if not self.within_board(adjacent_col,adjacent_row) or(self.within_board(adjacent_col,adjacent_row) and self._BOARD[adjacent_col][adjacent_row] == NONE):
            return False
        if self._BOARD[adjacent_col][adjacent_row] == color:
            return True
        return self.check_line(color,adjacent_col,adjacent_row,direction)
            
    
    def is_valid_move(self,color:int,col:int,row:int)->bool:
        '''checks the pieces around a point to see if there is a possible
           othello line flip from the origin'''
        if self.within_board(col,row) and self._BOARD[col][row] == NONE:
            for c in range(col-1,col+2):
                for r in range(row-1,row+2):
                    if self.within_board(c,r) and self._BOARD[c][r] != color and (row != r or col != c):
                        if self.check_line(color,col,row,(c-col,r-row)):
                            return True
        return False
    
    def color_line(self,color,col:int,row:int,direction:tuple)->None:
        '''assumes there that the given point is a complete othello line and flips
           the pieces bounded between a color'''
        col += direction[0]
        row += direction[1]
        while self._BOARD[col][row] != color:
            self._BOARD[col][row] = color
            col += direction[0]
            row += direction[1]
            
    def place_piece(self,color:int,col:int,row:int)->None:
        '''assumes that the move is already valid and places a piece down. flips over
           all lines that are completed by another same color piece'''
        for c in range(col-1,col+2):
            for r in range(row-1,row+2):
                if self._BOARD[col][row] != color and self.check_line(color,col,row,(c-col,r-row)):
                    self.color_line(color,col,row,(c-col,r-row))
        self._BOARD[col][row] = color
    def more_moves(self,color:int)->bool:
        """returns true if a move can still be made"""
        for c in self._BOARD:
            for r in c:
                if self._BOARD[c][r] == None and self.is_valid_move(color,c,r):
                    return True
        return False

    def count(self)->tuple:
        """returns the count of the pieces on the board"""
        wc = 0
        bc = 0
        for c in self._BOARD:
            for r in self._BOARD:
                if self._BOARD[c][r] == WHITE:
                    wc += 1
                elif self._BOARD[c][r] == BLACK:
                    bc += 1
        return (wc,bc)
    
    def Make_move(self,col:int,row:int):
        """places current player's piece at a specified point"""
        if not self._gameover and (self.more_moves(BLACK) or self.more_moves(WHITE)):
            move = BLACK
            if self._turn == WHITE:
                move = WHITE
            if self.more_moves(move):
                if self.is_valid_move(move,col,row):
                    self.place_piece(move,col,row)
                    self.switch_turn()
                else:
                    print('sorry invalid move')
            else:
                self.switch_turn()
        else:
            self._gameover = True
            

        

if __name__ == '__main__':
    game = Othello_Gamestate(8,8,BLACK,WHITE)
    game.print_board()
    print('TURN: ',game._turn)
    while True:
        col = int(input("col pls: "))
        row = int(input("row pls: "))
        game.Make_move(col,row)
        game.print_board()
    

                
