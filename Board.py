class Board:
    def __init__(self, absciss_size=11, ordinate_size=11):
        self.size = [absciss_size, ordinate_size]
        self.tab = []
        if absciss_size <= 0 :
            absciss_size = 1
        if ordinate_size <= 0:
            ordinate_size = 1
        for i in range(ordinate_size):
            line = []
            for j in range(absciss_size):
                line.append("W")
            self.tab.append(line)
    
    def __repr__(self):
        tab_string = ""
        for i in reversed(self.tab):
            for j in i:
                tab_string += j + " "
            tab_string += "\n"
        return tab_string


    def change_case_color(self, case):
        if self.tab[case[1]][case[0]] == "W":
            self.set_black_cases(case)
        else:
            self.set_white_cases(case)

    # Getters
    def get_tab(self):
        return self.tab
    
    def get_case_color(self, case):
        return self.tab[case[1]][case[0]]
    
    def get_size(self):
        return self.size

    # Setters
    def set_black_cases(self, *cases):
        for case in cases:
            self.tab[case[1]][case[0]] = "B"

    def set_white_cases(self, *cases):
        for case in cases:
            self.tab[case[1]][case[0]] = "W"


