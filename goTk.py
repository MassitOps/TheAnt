from Window import *

win = Tk()
win.title("La fourmi de Langton")

ant = Ant([5,5], "N", "red")
grid = Board(11, 11)

screen = Window(win, ant, grid)
screen.mainloop()

screen.destroy()
