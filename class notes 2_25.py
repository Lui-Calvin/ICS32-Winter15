import tkinter

class RingsApp:
    def __init__(self):
        self._root_window = tkinter.Tk()
        self._canvas = tkinter.Canvas(
            master = self._root_window,width = 700,height = 600,
            background = '#bedebe')

        self._canvas.grid(row = 0,column = 0)
        self._root_window.rowconfigure(0,weight = 1)
        self._root_window.colconfigure(0,weight = 1)


    def start(self):
        self._root_window.mainloop()

if __name__ == '__main__':
    app = RingsApp()
    app.start()
    
