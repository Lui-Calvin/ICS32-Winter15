

NONE = 0
WHITE = 1
BLACK = 2

class Othello_Gamestate:
    def __init__(self,row:int,col:int,turn:int,Arrangement:int,win_cond:str):
        """assigns all the variables"""
        self._NUM_ROW = row
        self._NUM_COL = col
        self._BOARD = []
        self._turn = turn
        self._win_cond = win_cond
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
        self._BOARD[int(self._NUM_ROW/2)-1][int(self._NUM_COL/2)-1] = first_pos
        self._BOARD[int(self._NUM_ROW/2)][int(self._NUM_COL/2)] = first_pos
        self._BOARD[int(self._NUM_ROW/2)][int(self._NUM_COL/2)-1] = second_pos
        self._BOARD[int(self._NUM_ROW/2)-1][int(self._NUM_COL/2)] = second_pos

    def print_board(self)->None:
        '''prints out readable board onto the console'''
        for col in self._BOARD:
            for row in col:
                item = "."
                if row == BLACK:
                    item = 'B'
                elif row == WHITE:
                    item = 'W'
                print(item,end = " ")
            print()

    def switch_turn(self):
        '''switches turns'''
        if self._turn == WHITE:
            self._turn = BLACK
        else:
            self._turn = WHITE

    def within_board(self,row:int,col:int)->bool:
        '''checks to see if a point is within the board'''
        if row < self._NUM_ROW and row >= 0 and col < self._NUM_COL and col >= 0:
            return True
        return False

    def check_line(self,color:int,row:int,col:int,direction:tuple)->bool:
        '''takes a point and checks the adjacent point in the specified direction
           and recursively calls this function to see if there is a matching game piece
           that can make this a valid line in othello'''        
        adjacent_row = row + direction[0]
        adjacent_col = col + direction[1]
        if not self.within_board(adjacent_row,adjacent_col) or(self.within_board(adjacent_row,adjacent_col) and self._BOARD[adjacent_row][adjacent_col] == NONE):
            return False
        if self._BOARD[adjacent_row][adjacent_col] == color:
            return True
        return self.check_line(color,adjacent_row,adjacent_col,direction)
            
    
    def is_valid_move(self,color:int,row:int,col:int)->bool:
        '''checks the pieces around a point to see if there is a possible
           othello line flip from the origin'''
        if self.within_board(row,col) and self._BOARD[row][col] == NONE:
            for r in range(row-1,row+2):
                for c in range(col-1,col+2):
                    if self.within_board(r,c):
                        if self._BOARD[r][c] != color and (row != r or col != c):
                            if self.check_line(color,row,col,(r-row,c-col)):
                                return True
        return False
    
    def color_line(self,color,row:int,col:int,direction:tuple)->None:
        '''assumes there that the given point is a complete othello line and flips
           the pieces bounded between a color'''
        row += direction[0]
        col += direction[1]
        while self._BOARD[row][col] != color:
            self._BOARD[row][col] = color
            row += direction[0]
            col += direction[1]
            
    def place_piece(self,color:int,row:int,col:int)->None:
        '''assumes that the move is already valid and places a piece down. flips over
           all lines that are completed by another same color piece'''
        for r in range(row-1,row+2):
            for c in range(col-1,col+2):
                if self._BOARD[row][col] != color and self.check_line(color,row,col,(r-row,c-col)):
                    self.color_line(color,row,col,(r-row,c-col))
        self._BOARD[row][col] = color
        
    def more_moves(self,color:int)->bool:
        """returns true if a move can still be made"""
        for r in range(self._NUM_ROW):
            for c in range(self._NUM_COL):
                if self._BOARD[r][c] == NONE and self.is_valid_move(color,r,c):
                    return True
        return False

    def count(self)->tuple:
        '''returns the count of the black and white pieces on the board in a tuple'''
        bc = 0
        wc = 0
        for r in self._BOARD:
            for c in r:
                if c == WHITE:
                    wc += 1
                elif c == BLACK:
                    bc += 1
        return (bc,wc)
           
    def Make_move(self,row:int,col:int):
        """places current player's piece at a specified point"""
        if self._gameover:
            pass
        elif not self._gameover and (self.more_moves(BLACK) or self.more_moves(WHITE)):
            move = BLACK
            if self._turn == WHITE:
                move = WHITE
            if self.more_moves(move):
                if self.is_valid_move(move,row,col): 
                    self.place_piece(move,row,col)
                    self.switch_turn()
                    if not self.more_moves(BLACK) and not self.more_moves(WHITE):
                        self._gameover = True
            else:
                self.switch_turn()
                
    def winner(self)-> str:
        '''picks winner based on the winning condition set'''
        count = self.count()
        if self._win_cond == '>':
            if count[0] > count[1]:
                return 'B'
            elif count[0] < count[1]:
                return 'W'
        elif self._win_cond == '<':
            if count[0] < count[1]:
                return 'B'
            elif count[0] > count[1]:
                return 'W'
        return 'NONE'

class GameOverError(Exception):
    '''exception that is thrown when moves are attempted after the game
       has ended'''
    pass

class InvalidMoveError(Exception):
    '''exception thrown when an invalid move is attempted'''
    pass
