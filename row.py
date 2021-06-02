class Row:
    def __init__(self, data):
        self.DATA = data
        self.pivot_pos = None
        self.all_zero = False

    def update_pivot_pos(self):
        """ update and return pivot position """
        # find the first nonzero value in row
        i = 0
        while i < len(self.DATA) and self.DATA[i] == 0:
            i += 1

        # if i is less than len(data) there is a pivot; otherwise, the row is all zero
        if i < len(self.DATA):
            self.pivot_pos = i
        else:
            self.pivot_pos = None
            self.all_zero = True

        return self.pivot_pos

    def reduce(self):
        """ scale row so the leading coefficient is 1 """
        # update pivot pos
        self.update_pivot_pos()
        # divide each entry by the pivot value
        if not self.pivot_pos == None:
            piv_value = self.DATA[self.pivot_pos] # get value at pivot position
            # self.DATA = [0 if x == 0 else x/self.DATA[self.pivot_pos] for x in self.DATA]
            self.DATA = [0 if x == 0 else x/piv_value for x in self.DATA]

        return

    def print_row(self):
        for v in self.DATA:
            if (v < 0 and v > -10) or (v >= 10):
                print("{:0.2f}".format(v), end="   ")
            elif v <= -10:
                print("{:0.1f}".format(v), end="   ")
            elif v >= 0 and v < 10:
                print("{:0.3f}".format(v), end="   ")
        print()

    
    #* GETTERS
    def get_pivot_pos(self):
        return self.pivot_pos
    def get_all_zero(self):
        return self.all_zero
    def get_length(self):
        return len(self.DATA)
    def get_data(self):
        return self.DATA
    def get_value(self, index):
        return self.DATA[index]

    #* SETTERS
    def set_value(self, index, value):
        self.DATA[index] = value
        return
