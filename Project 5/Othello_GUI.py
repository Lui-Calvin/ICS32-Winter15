#Calvin Lui 84152100
import tkinter
import Othello_class

FONT = ('Comic Sans MS', 14)

class window:
    '''pop up window that asks for all the settings of the game'''
    def __init__(self):
        self._dialog_window = tkinter.Toplevel()
        self._ROW = 0
        self._COL = 0
        self._FIRST = ''
        self._ARRANGEMENT = ''
        self._win_cond = ''
        self._ok_clicked = False

        settings_label = tkinter.Label(
            master = self._dialog_window, text = "GAME SETTINGS",
            font = FONT)
        settings_label.grid(
            row = 0,column = 0,padx = 10, pady = 10,
            sticky = tkinter.W)

        
        row_label = tkinter.Label(
            master = self._dialog_window, text = "Row(4 - 16)",
            font = FONT)   
        row_label.grid(
            row = 1, column = 0,padx = 10,pady = 10,
            sticky = tkinter.W)

        
        self._row_entry = tkinter.Entry(
            master = self._dialog_window,width = 20,font = FONT)
        self._row_entry.grid(
            row = 1,column = 1,padx = 10,pady = 10,
            sticky = tkinter.W + tkinter.E)


        col_label = tkinter.Label(
            master = self._dialog_window,text = "Column(4 - 16)",
            font = FONT)
        col_label.grid(
            row = 2,column = 0,padx = 10,pady = 10,
            sticky = tkinter.W)


        self._col_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = FONT)
        self._col_entry.grid(
            row = 2,column = 1,padx = 10,pady = 10,
            sticky = tkinter.W + tkinter.E)
        

        first_label = tkinter.Label(
            master = self._dialog_window,text = "First Turn( B or W )",
            font = FONT)          
        first_label.grid(
            row = 3,column = 0,padx = 10,pady = 10,
            sticky = tkinter.W)
        

        self._turn_entry = tkinter.Entry(
            master = self._dialog_window, width = 20,font= FONT)
        self._turn_entry.grid(
            row = 3,column = 1,padx = 10,pady = 10,
            sticky = tkinter.W + tkinter.E)
        

        arr_label = tkinter.Label(
            master = self._dialog_window,text = "Arrangement( B or W )",font = FONT)
        arr_label.grid(
            row = 4,column = 0,padx = 10,pady = 10,
            sticky = tkinter.W)
        

        self._arr = tkinter.Entry(
            master = self._dialog_window,width = 20,font = FONT)
        self._arr.grid(
            row = 4,column = 1,padx = 10,pady = 10,
            sticky = tkinter.W +tkinter.E)

        win_condition_label = tkinter.Label(
            master = self._dialog_window,text = "Win Condition( > or < )",font = FONT)
        win_condition_label.grid(
            row = 5,column = 0,padx = 10,pady = 10,
            sticky = tkinter.W)
        
        self._win_type = tkinter.Entry(
            master = self._dialog_window,width = 20,font = FONT)
        self._win_type.grid(
            row = 5,column = 1,padx = 10,pady = 10,
            sticky = tkinter.W +tkinter.E)

        

        button_frame = tkinter.Frame(master = self._dialog_window)
        button_frame.grid(
            row = 6,column = 1, columnspan = 2,padx = 10,pady = 10,
            sticky = tkinter.E + tkinter.S)
        
        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = FONT,
            command = self._ok_button_clicked)
        ok_button.grid(row = 0,column = 0,padx = 10,pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = FONT,
            command = self._cancel_button_clicked)
        cancel_button.grid(row = 0,column = 1,padx = 10,pady = 10)

        self._dialog_window.rowconfigure(5,weight = 1)
        self._dialog_window.columnconfigure(1,weight = 1)
        
    def display(self)->None:
        '''call that brings a modal window'''
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def _ok_button_clicked(self)->None:
        """sets all the variables when ok is clicked"""
        row = int(self._row_entry.get())
        col = int(self._col_entry.get())
        first = self._turn_entry.get()
        arr = self._arr.get()
        win = self._win_type.get()
        if self.valid_inputs(row,col,first,arr,win):
            self._ok_clicked = True
            self._ROW = row
            self._COL = col
            self._FIRST = first
            self._ARRANGEMENT = arr
            self._win_cond = win
            self._dialog_window.destroy()
        
    def _cancel_button_clicked(self)->None:
        '''kills settings window if cancel is clicked'''
        self._dialog_window.destroy()

    def valid_inputs(self,row:int,col:int,first:str,Arrangement:str,win_cond:str)->bool:
        nums = [4,6,8,10,12,14,16]
        colors = ['B','W']
        wins = ['<','>']
        return row in nums and col in nums and first in colors and Arrangement in colors and win_cond in wins
        
    def get_info(self)->(int,int,int,int):
        '''returns the information set by the pop up window'''
        return(self._ROW, self._COL, self.BW_to_int(self._FIRST), self.BW_to_int(self._ARRANGEMENT),self._win_cond)
    
    def BW_to_int(self,color:str)->int:
        '''converts the string into the black white integer representation'''
        if color.upper() == 'B':
            return 2
        elif color.upper() == 'W':
            return 1
        
class Othello_gui:
    def __init__(self):
        '''sets up the starting window'''
        self._root_window = tkinter.Tk()
        
        self._canvas = tkinter.Canvas(
            master = self._root_window,width = 500,height = 500,
            background = '#006000')
        self._canvas.grid(
            row = 1, column = 0, columnspan = 2, padx = 20, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._canvas.create_text(250,250,text = "please click to start game",font = ("Comic Sans MS",30))     
        
        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>',self._on_canvas_clicked)
        self._game = None
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)
        
        

    def start(self):
        '''starts the tkinter event based loop'''
        self._root_window.mainloop()

    def _on_canvas_clicked(self, event:tkinter.Event)->None:
        '''when canvas is clicked and game has not been instantiated yet,
           open pop up window and get parameters for a new othello game object'''
        if self._game == None:
            win = window()
            win.display()
            if win._ok_clicked:
                info = win.get_info()
                self._game = Othello_class.Othello_Gamestate(
                    info[0],info[1],info[2],info[3],info[4])
                self._canvas.delete(tkinter.ALL)
                self.draw_lines()
                self.draw_circles()
                self.Display_info()
        else:
            self.Othello_move(event.x,event.y)
            self.draw_lines()
            self.draw_circles()
        
    def Display_info(self)->None:
        self._Bcount = tkinter.StringVar()
        self._Wcount = tkinter.StringVar()
        self._turn = tkinter.StringVar()
        self._winner = tkinter.StringVar()

        Full_label = tkinter.Label(master = self._root_window,text = "OTHELLO FULL",font =FONT)
        Full_label.grid(
            row = 0,column = 0,columnspan = 2,padx = 10,pady = 10,sticky = tkinter.N)

        self._Bcount.set("B: {}".format(self._game.count()[0]))
        Black_count = tkinter.Label(
            master = self._root_window, textvariable = self._Bcount,font = FONT)
        Black_count.grid(
            row = 2,column = 0,padx = 10,pady= 10,sticky = tkinter.W)

        self._Wcount.set("W: {}".format(self._game.count()[1]))
        White_count = tkinter.Label(
            master = self._root_window,textvariable = self._Wcount,font = FONT)
        White_count.grid(
            row = 2, column = 1, padx = 10, pady = 10,sticky = tkinter.W)

        self._turn.set("")
        Winner_label = tkinter.Label(
            master = self._root_window,textvariable = self._winner,font = FONT)
        Winner_label.grid(
            row = 3,column = 1,padx = 10,pady = 10,sticky = tkinter.E)
        
        self._turn.set("TURN: {}".format(self.int_to_BW(self._game._turn)))
        Turn_display = tkinter.Label(
            master = self._root_window,textvariable = self._turn,font = FONT)
        Turn_display.grid(
            row = 2,column = 1,padx = 10,pady = 10,sticky = tkinter.E)
        
            
    def _on_canvas_resized(self,event:tkinter.Event)->None:
        '''when resized, if game hasn't been instantiated yet,
           resize starting text. when game has started, resize
           the lines and circles on the game board'''
        self._canvas.delete(tkinter.ALL)
        if self._game == None:
            self._canvas.create_text(int(self._canvas.winfo_width()/2),
                                     int(self._canvas.winfo_height()/2),
                                     text = "please click to start game!",font = ("Comic Sans MS",30))
        else:
            self.draw_lines()
            self.draw_circles()
            
    def draw_lines(self)->None:
        '''draws all the black lines in the grid'''
        col_space = self._canvas.winfo_width()/float(self._game._NUM_COL)
        row_space = self._canvas.winfo_height()/float(self._game._NUM_ROW)
        c = 0
        r = 0
        for col in range(self._game._NUM_COL):
            self._canvas.create_line(c,0,c,self._canvas.winfo_height())
            c += col_space
        for row in range(self._game._NUM_ROW):
            self._canvas.create_line(0,r,self._canvas.winfo_width(),r)
            r += row_space

    def draw_circles(self)->None:
        '''draws all the othello game pieces'''
        x_space = self._canvas.winfo_width()/float(self._game._NUM_COL)
        y_space = self._canvas.winfo_height()/float(self._game._NUM_ROW)
        y = 0
        for row in range(self._game._NUM_ROW):
            x = 0
            for col in range(self._game._NUM_COL):
                if self._game._BOARD[row][col] == 2:
                    self._canvas.create_oval(x,y,x+x_space,y+y_space,fill = 'black')
                elif self._game._BOARD[row][col] == 1:
                    self._canvas.create_oval(x,y,x+x_space,y+y_space,fill = 'white')
                x += x_space      
            y += y_space

    def Othello_move(self,x:int,y:int)->None:
        '''gets a set of coordinates and makes a move in othello according
           to which box the mouse x and mouse y were in'''
        if not self._game._gameover:
            row_col = self.xy_to_row_col(x,y)
            self._game.Make_move(row_col[0],row_col[1])
            self._Bcount.set("B: {}".format(self._game.count()[0]))
            self._Wcount.set("W: {}".format(self._game.count()[1]))
            self._turn.set("TURN: {}".format(self.int_to_BW(self._game._turn)))
            if self._game._gameover:
                self._winner.set("WINNER: {}".format(self._game.winner()))
            
    def xy_to_row_col(self,x:int,y:int)->(int,int):
        '''calculates which row and column a mouse click is in'''
        x_space = self._canvas.winfo_width()/float(self._game._NUM_COL)
        y_space = self._canvas.winfo_height()/float(self._game._NUM_ROW)
        row = int(y/y_space)
        col = int(x/x_space)
        return (row,col)

    def int_to_BW(self,color:int)->str:
        '''converts the int representation of black or white and converts it into a string'''
        if color == 2:
            return "B"
        elif color == 1:
            return "W"



if __name__ == '__main__':
    game = Othello_gui()
    game.start()
    
        
        
