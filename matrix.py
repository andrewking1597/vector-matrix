from row import Row

class Matrix:
    def __init__(self, num_rows, num_cols, is_augmented=False):
        self.NUM_ROWS = num_rows
        self.NUM_COLS = num_cols
        self.IS_AUGMENTED = is_augmented
        self.ROWS = []

    def rref(self):
        self.ref()

        # for each row, starting with the last row and ending with the second row
        for i in range(self.NUM_ROWS-1, 0, -1):
            # reduce the row so the pivot value is 1
            self.ROWS[i].reduce()
            # zeros above
            self._zeros_above(i)
            self._sort_rows()

        # reduce row 0
        self.ROWS[0].reduce()

    def ref(self):
        self._sort_rows()
        for i in range(self.NUM_ROWS - 1):
            self._zeros_below(i)
            self._sort_rows()
        return

    def _zeros_above(self, row_num):
        # get the relevant pivot position and pivot value
        pivot_pos = self.ROWS[row_num].get_pivot_pos()
        pivot_value = self.ROWS[row_num].get_value(pivot_pos)

        # loop through the rows ABOVE row_num
        for i in range(row_num-1, -1, -1):
            # calculate the appropriate scalar
            current_scalar = -1 * self.ROWS[i].get_value(pivot_pos) / pivot_value
            # scale and replace scalar, row_num, i
            self._scale_and_replace(current_scalar, row_num, i)

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

        return

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

    def add_row(self, row_list):
        """ create a new row and append it to the matrix """

        # use row_list to make a Row object
        row = Row(row_list)

        if row.get_length() == self.NUM_COLS and len(self.ROWS) < self.NUM_ROWS:
            self.ROWS.append(row)
            return 1 # success
        elif len(self.ROWS) >= self.NUM_ROWS:
            print("Error: matrix full")
            return 0 # error
        elif row.get_length() != self.NUM_COLS:
            print("Error: rows must have a length of {}.".format(self.NUM_COLS))
            return 0 # error

    def add_rows(self, rows):
        """ take a list of lists and add each as a row """
        for row in rows:
            self.add_row(row)

    def print_matrix(self):
        for r in self.ROWS:
            r.print_row()
        print()


    #* GETTERS
    def get_num_rows(self):
        return self.NUM_ROWS
    def get_num_cols(self):
        return self.NUM_COLS
    def get_is_augmented(self):
        return self.IS_AUGMENTED
    def get_rows(self):
        return self.ROWS
    def get_row(self, r):
        return self.ROWS[r] #todo move this into a try block
