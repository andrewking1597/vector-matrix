from row import Row

class CoefficientMatrix:
    def __init__(self, data):
        self.ROWS = [Row(d) for d in data]
        self.NUM_ROWS = len(data)
        self.NUM_COLS = len(data[0]) # assuming all rows same length (todo exception handling)

    def ref(self):
        self._sort_rows()

        current_row = 0
        while current_row < self.NUM_ROWS - 1 and self.ROWS[current_row].update_pivot_pos() < self.NUM_COLS:
            self._zeros_below(current_row)
            self._sort_rows()
            current_row += 1
        return

    def _zeros_below(self, row_num):
        # get the relevant pivot position and pivot value
        pivot_pos = self.ROWS[row_num].get_pivot_pos()

        pivot_value = self.ROWS[row_num].get_value(pivot_pos)
        
        # loop through the rows BELOW row_num
        for i in range(row_num+1, self.NUM_ROWS):
            # calculate the appropriate scalar
            current_scalar = -1 * self.ROWS[i].get_value(pivot_pos) / pivot_value
            # scale and replace scalar, row_num, i
            self._scale_and_replace(current_scalar, row_num, i)
            
        return True

    def _scale_and_replace(self, scalar, row_a, row_b):
        """ (scalar)(row_a) + row_b --> row_b """
        for i in range(self.NUM_COLS):
            # self.ROWS[row_b][i] = scalar * self.ROWS[row_a][i] + self.ROWS[row_b][i]
            v = scalar * self.ROWS[row_a].get_value(i) + self.ROWS[row_b].get_value(i)
            self.ROWS[row_b].set_value(i, v)

        return

    def _sort_rows(self):
        """
        sort rows by pivot_pos
        note: pivot_pos can be in range 0-->self.NUM_COLS (inclusive)
        """

        # first, update pivot_pos for each row
        for row in self.ROWS:
            row.update_pivot_pos()

        # insertion sort
        #todo use more efficient sorting algorithm (counting sort?)
        for i in range(1, self.NUM_ROWS):
            current_row = self.ROWS[i]
            current_row_pivot_pos = current_row.get_pivot_pos()
            j = i - 1
            while j >= 0 and self.ROWS[j].get_pivot_pos() > current_row_pivot_pos:
                self.ROWS[j+1] = self.ROWS[j]
                j -= 1
            self.ROWS[j+1] = current_row

        return

    def print_matrix(self):
        for r in self.ROWS:
            r.print_row()
        print()


    #* GETTERS
    def get_num_rows(self):
        return self.NUM_ROWS
    def get_num_cols(self):
        return self.NUM_COLS
    def get_rows(self):
        return self.ROWS
    def get_row(self, r):
        return self.ROWS[r] #todo move this into a try block
