class Ant:

    number_of_ants = 0
    def __init__(self, position=[0,0], orientation="N", color="black"):
        self.color = color
        self.position = position
        if orientation not in ["N", "S", "E", "W"]:
            self.orientation = 'N'
        else:
            self.orientation = orientation
        Ant.number_of_ants += 1
    
    def move_right(self):
        if self.orientation == "N":
            self.position = [self.position[0]+1, self.position[1]]
            self.orientation = "E"
        elif self.orientation == "E":
            self.position = [self.position[0], self.position[1]-1]
            self.orientation = "S"
        elif self.orientation == "S":
            self.position = [self.position[0]-1, self.position[1]]
            self.orientation = "W"
        elif self.orientation == "W":
            self.position = [self.position[0], self.position[1]+1]
            self.orientation = "N"

    def move_left(self):
        if self.orientation == "N":
            self.position = [self.position[0]-1, self.position[1]]
            self.orientation = "W"
        elif self.orientation == "W":
            self.position = [self.position[0], self.position[1]-1]
            self.orientation = "S"
        elif self.orientation == "S":
            self.position = [self.position[0]+1, self.position[1]]
            self.orientation = "E"
        elif self.orientation == "E":
            self.position = [self.position[0], self.position[1]+1]
            self.orientation = "N"


    def __repr__(self):
        return "Position: {}  |  Orientation: {}  |  Color: {}".format(self.position, self.orientation, self.color)

    # Getters
    def get_color(self):
        return self.color

    def get_position(self):
        return self.position

    def get_orientation(self):
        return self.orientation

    # Setters
    def set_color(self, color):
        self.color = color

    def set_position(self, position):
        self.position = position
    
    def set_orientation(self, orientation):
        self.orientation = orientation

