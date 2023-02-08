class NonogramSolver:
    def __init__(self, ROWS_VALUES=[[]], COLS_VALUES=[[]]) -> None:
        self.ROWS_VALUES = ROWS_VALUES
        self.no_of_rows = len(ROWS_VALUES)

        self.COLS_VALUES = COLS_VALUES
        self.no_of_cols = len(COLS_VALUES)

        self.EMPTY_CELL = 0
        self.FILLED_CELL = 1
        self.ELIMINATED_CELL = -1

        self.board = [
            [self.EMPTY_CELL for c in range(self.no_of_cols)]
            for r in range(self.no_of_rows)
        ]

    def fill_trivial_lines(self, line_vals) -> list:
        line = []

        for v in line_vals:
            line.extend([self.FILLED_CELL for i in range(v)])
            line.append(self.ELIMINATED_CELL)
        return line[:-1]

    def fill_overlapping_cells(self, line_vals: list[int], line_len: int) -> list:
        spare = line_len - sum(line_vals) - (len(line_vals) - 1)

        # if spare < 0, then this is not a valid nonogram.
        # TODO raise error if < 0

        if spare == 0:
            return self.fill_trivial_lines(line_vals=line_vals)
        else:
            line = [self.EMPTY_CELL for i in range(line_len)]
            for i, val in enumerate(line_vals):
                if val > spare:
                    start_range = sum(line_vals[:i]) + len(line_vals[:i]) + spare
                    end_range = start_range + (val - spare)
                    for j in range(start_range, end_range):
                        line[j] = self.FILLED_CELL
            return line


# print(NonogramSolver().fill_overlapping_cells([5,2], 12))
print(NonogramSolver().fill_trivial_lines([5, 2]))
