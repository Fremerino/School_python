import os
import sys

import numpy as np


class SudokuSolver:
    def __init__(self):
        self.field = np.zeros([9, 9], dtype=int)

    def load(self, file_path:str) -> None:

        # list of lists (rows)
        loaded_rows : list[list[int]] = [] 

        argument = file_path
        with open(argument,encoding="UTF-8") as f:
            for file in f:
              line = file.strip().split(";")
              line = [int(cell) for cell in line]
              loaded_rows.append(line)

      
        self.field = np.array(loaded_rows)



    def check_sequence(self, sequence:np.ndarray) -> bool:
        encounter = 0
        for i in sequence:
            for x in sequence:
                if i==x and i!=0:
                    encounter = encounter+1
                if encounter==2:
                    return False
            encounter = 0
        return True


    def check_row(self, row_index:int) -> bool:
        return self.check_sequence(self.field[row_index])

    def check_column(self, column_index:int) -> bool:
        return self.check_sequence(self.field[:,column_index])

    def check_block(self, row_index:int, column_index:int) -> bool:
        row_start = row_index-row_index%3
        collumn_start = column_index-column_index%3
        return self.check_sequence(self.field[row_start:row_start+3,collumn_start:collumn_start+3].flatten())


    def check_one_cell(self, row_index:int , column_index:int) -> bool:
        if self.check_row(row_index) and self.check_block(row_index, column_index) and self.check_column(column_index):
            return True
        return False
    def get_empty_cell(self) -> tuple[int, int] | None:
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if self.field[i,j] == 0:
                    return i,j
        return None

    def solve(self) -> bool:
        empty = self.get_empty_cell()
        if empty is None:
            return True
        i, j = empty
        for num in range(1,10):
            self.field[i,j] = num
            if not self.check_one_cell(i,j):
                continue
            solved = self.solve()
            if solved:
                return True
        self.field[i,j] = 0
        return False 





def main() -> None:

    sudoku_solver = SudokuSolver()
    sudoku_solver.load("sudoku.csv")
    sudoku_solver.solve()
    print(sudoku_solver.field)

if __name__ == "__main__":

    
    main()

