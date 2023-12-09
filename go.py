from Ant import *
from Board import *

def move(ant, grid):
    pos = ant.get_position()
    cas = grid.get_case_color(pos)
    if cas == "W":
        ant.move_right()
    else:
        ant.move_left()
    newpos = ant.get_position()
    gridsize = grid.get_size()
    if (newpos[0]>=gridsize[0]) or (newpos[0]<0) or (newpos[1]>=gridsize[1]) or (newpos[1]<0):
        ant.set_position(pos)
    else:
        grid.change_case_color(pos)

grid = Board()
#grid.set_black_cases([4,4],[4,5],[4,6],[5,6],[6,6],[6,5],[6,4],[5,4])
ant = Ant([5,5])
print(grid, ant, sep="")
n = input("Enter the number of the ant's moves: ")

while True:
    try:
        n = int(n)
    except ValueError:
        n = input("Enter an interger: ")
    else:
        if n <= 0:
            n = input("A strictly positive integer: ")
        else:
            break
        
for i in range(n):
    move(ant, grid)
    print(grid, ant, sep="")
