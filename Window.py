from Ant import *
from Board import *
from tkinter import *

class Window(Frame):
    def __init__(self, win, ant, tab, **kwargs):
        Frame.__init__(self, win, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.num_iteration = 0
        self.button_is_go = True
        self.after_id = 0
        self.ant = ant
        self.tab = tab
        self.label = Label(self, text="Iteration: {}".format(self.num_iteration))
        self.label.pack()
        self.grid = Frame(self, width=768, heigh=576)
        self.grid_list = self.create_grid(self.tab, self.grid)
        self.grid.pack()
        self.exit_button = Button(self, text="Exit", width=2*self.tab.get_size()[0], command=self.quit)
        self.exit_button.pack(side="right")
        self.go_button = Button(self, text="Go!", width=self.tab.get_size()[0], command=self.goo)
        self.go_button.pack(side="left")
        self.put_ant(self.ant)

    def create_grid(self, tab, grid):
        rows = tab.get_size()[1]
        cols = tab.get_size()[0]
        mygrid = []
        for row in range(rows):
            line = []
            for col in range(cols):
                color = tab.get_case_color([col, row])
                if color == "W":
                    color = "white"
                else:
                    color = "black"
                frame = Frame(grid, width=30, height=30, bg=color, borderwidth=1, highlightthickness=1, highlightbackground="gray")
                frame.bind("<Button-1>", self.change_color)
                tmp = list(range(rows))
                tmp = tmp[-(row+1)]
                frame.grid(row=tmp, column=col)
                line.append(frame)
            mygrid.append(line)
        return mygrid
    
    def put_ant(self, ant):
        frame = ant.get_position()
        frame = self.grid_list[frame[1]][frame[0]]
        canvas = Canvas(frame, width=25, height=25, bg=frame["bg"], highlightthickness=0)
        canvas.pack()
        size = 23
        direction = ant.get_orientation()
        self.create_triangle(canvas, size, direction, ant.get_color())

    def create_triangle(self, canvas, size, direction, color):
        x_center = size / 2
        y_center = size / 2
        if direction == "N":
            points = [x_center, 0, size, size, 0, size]
        elif direction == "E":
            points = [0, 0, 0, size, size, y_center]
        elif direction == "S":
            points = [0, 0, size, 0, x_center, size]
        elif direction == "W":
            points = [0, y_center, size, 0, size, size]
        else:
            raise ValueError("Invalid direction")
        canvas.create_polygon(points, fill=color)

    def move(self, ant, grid):
        pos = ant.get_position()
        cas = grid.get_case_color(pos)
        if cas == "W":
            ant.move_right()
        else:
            ant.move_left()
        newpos = ant.get_position()
        gridsize = grid.get_size()
        frame = self.grid_list[pos[1]][pos[0]]
        if (newpos[0]>=gridsize[0]) or (newpos[0]<0) or (newpos[1]>=gridsize[1]) or (newpos[1]<0):
            ant.set_position(pos)
            frame.winfo_children()[0].destroy()
        else:
            grid.change_case_color(pos)
            frame.winfo_children()[0].destroy()
            if frame["bg"] == "white":
                frame["bg"] = "black"
            else:
                frame["bg"] = "white"

    def go(self):
        self.num_iteration += 1
        self.label["text"] = "Iteration: {}".format(self.num_iteration)
        self.move(self.ant, self.tab)
        self.put_ant(self.ant)
        self.after_id = self.after(300, self.go)

    def goo(self):
        if self.button_is_go == True:
            self.button_is_go = False
            self.go_button["text"] = "Stop!"
            self.go()
        else:
            self.button_is_go = True
            self.go_button["text"] = "Go!"
            self.after_cancel(self.after_id)

    def change_color(self, event):
        obj = event.widget
        pos = []
        for elt in self.grid_list:
            if obj in elt:
                pos.append(elt.index(obj))
                pos.append(self.grid_list.index(elt))
        col = self.tab.get_case_color(pos)
        self.tab.change_case_color(pos)
        if col == 'W':
            self.grid_list[pos[1]][pos[0]]["bg"] = "black"
        else:
            self.grid_list[pos[1]][pos[0]]["bg"] = "white"

