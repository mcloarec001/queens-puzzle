import random
import copy
from typing import List
from Queen import Queen
import numpy as np


class Grid:
    def __init__(
        self,
        grid_size: int,
        proba_rand_queen: float = 0.0,
        proba_rand_movement: float = 0.0,
        predisposed_queens: List = [],
    ):
        self._grid_size = grid_size
        self._conflicts = np.zeros((grid_size, grid_size), dtype=int)
        self._proba_ran_queen = proba_rand_queen
        self._proba_rand_movement = proba_rand_movement
        self._queens = []
        self.nb_conflicts = 0

        # Select distinct random positions
        random_positions = []
        while len(random_positions) < self._grid_size:
            new_position = [
                random.randint(0, self._grid_size - 1),
                random.randint(0, self._grid_size - 1),
            ]
            if new_position not in random_positions:
                random_positions.append(new_position)

        # Put the _queens on the positions
        for pos in random_positions:
            self._queens.append(Queen(new_line=pos[0], new_column=pos[1]))

        self._update_conflict()

    def _update_conflict(self):

        # Update the entire table of conflicts
        self._conflicts = np.zeros((self._grid_size, self._grid_size), dtype=int)
        for queen in self._queens:
            for column in range(self._grid_size):
                self._conflicts[queen.line, column] += 1
            for line in range(self._grid_size):
                self._conflicts[line, queen.column] += 1
            # direct diagonal
            dir_diag = queen.line - queen.column
            if dir_diag <= 0:
                for x in range(0, self._grid_size + dir_diag):
                    self._conflicts[x, x - dir_diag] += 1
            else:
                for x in range(0, self._grid_size - dir_diag):
                    self._conflicts[x + dir_diag, x] += 1
            # undirect diagonal
            undir_diag = queen.line + queen.column
            if undir_diag < self._grid_size:
                for x in range(0, undir_diag + 1):
                    self._conflicts[undir_diag - x, x] += 1
            else:
                for x in range(0, 2 * self._grid_size - undir_diag - 1):
                    self._conflicts[
                        self._grid_size - x - 1, undir_diag + 1 - self._grid_size + x
                    ] += 1

        # Update the conflicts of _queens and the number of actual conflicts
        nb_conflicts = 0
        for queen in self._queens:
            nb_queen_conflicts = self._conflicts[queen.line, queen.column] - 4
            queen.set_conflicts(nb_queen_conflicts)
            nb_conflicts += nb_queen_conflicts
        self.nb_conflicts = nb_conflicts // 2

    def _get_one_best_position(self):
        value = 0
        positions = []
        while value < 3 and len(positions) == 0:
            positions = [
                [i, j]
                for i in range(self._grid_size)
                for j in range(self._grid_size)
                if self._conflicts[i, j] == value
            ]
            value += 1

        for queen in self._queens:
            if [queen.line, queen.column] in positions:
                positions.remove([queen.line, queen.column])
        return random.choice(positions)

    def _get_one_random_position(self):
        positions = [
            [i, j] for i in range(self._grid_size) for j in range(self._grid_size)
        ]
        for queen in self._queens:
            positions.remove([queen.line, queen.column])
        pos = random.choice(positions)
        return pos

    def compare(self, second_grid):
        same = True
        for queen in self._queens:
            if queen not in second_grid._queens:
                same = False
        return same

    def one_turn(self):
        # Select the queen which has the most conflict
        proba = random.randint(0, 100) / 100
        queen_moving = random.choice(self._queens)
        if proba > self._proba_ran_queen:
            for queen in self._queens:
                if queen_moving.nb_conflicts < queen.nb_conflicts:
                    queen_moving = queen
        # Move it
        proba = random.randint(0, 100) / 100
        new_position = []
        if proba < self._proba_rand_movement:
            new_position = self._get_one_random_position()
        else:
            new_position = self._get_one_best_position()
        queen_moving.set_position(
            new_line=new_position[0],
            new_column=new_position[1],
        )

        # Deal with conflict
        self._update_conflict()

    def draw(self, drawing: bool = True):
        # for i in range(len(self._queens)):
        #     print(f"          -- Queen {i} --")
        #     self._queens[i].draw()
        # print()

        display = ""
        for line in range(self._grid_size):
            line_text = "     "
            for column in range(self._grid_size):
                column_text = "/ "
                for queen in self._queens:
                    if line == queen.line and column == queen.column:
                        column_text = "O "
                line_text += column_text
            display += line_text + "\n"
        if drawing:
            print(display)
            print("")
            print(f" Number of conflicts : {self.nb_conflicts}")
            print("      ==================== ")
            print("")
        return display
