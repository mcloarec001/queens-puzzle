import random

from Queen import Queen


class Grid:
    _queens = []
    solved = False

    def __init__(self, grid_size: int):
        self._grid_size = grid_size

        # Select distinct random positions
        random_positions = []
        while len(random_positions) < self._grid_size:
            new_position = [
                random.randint(0, self._grid_size - 1),
                random.randint(0, self._grid_size - 1),
            ]
            if new_position not in random_positions:
                random_positions.append(new_position)

        # Put the queens on the positions
        for pos in random_positions:
            self._queens.append(Queen(new_line=pos[0], new_column=pos[1]))
        self._update_conflict()

    def _update_conflict(self):
        for main_queen in self._queens:
            main_queen_conflicts = 0
            for second_queen in self._queens:
                if main_queen != second_queen and (
                    main_queen.line == second_queen.line
                    or main_queen.column == second_queen.column
                ):
                    main_queen_conflicts += 1
            main_queen.set_conflicts(nb_conflicts=main_queen_conflicts)

    def get_conflict(self):
        nb_conflicts = 0
        for queen in self._queens:
            nb_conflicts += queen.nb_conflicts
        return nb_conflicts

    def _get_possible_movement(self, queen: Queen):
        neighbour_position = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        # Dealing with borders
        if queen.line == 0:
            neighbour_position.remove([-1, 0])
        if queen.line == self._grid_size - 1:
            neighbour_position.remove([1, 0])
        if queen.column == 0:
            neighbour_position.remove([0, -1])
        if queen.column == self._grid_size - 1:
            neighbour_position.remove([0, 1])
        # Dealing with other queens
        for other_queen in self._queens:
            for pos in neighbour_position:
                if (
                    queen.line + pos[0] == other_queen.line
                    and queen.column + pos[1] == other_queen.column
                ):
                    neighbour_position.remove(pos)
        return neighbour_position

    def one_turn(self):
        # Select the queen which has the most conflict
        queen_moving = self._queens[0]
        for queen in self._queens:
            if queen_moving.nb_conflicts < queen.nb_conflicts:
                queen_moving = queen

        # Move it
        positions = self._get_possible_movement(queen=queen_moving)
        new_pos = random.choice(positions)
        queen_moving.set_position(
            new_line=queen_moving.line + new_pos[0],
            new_column=queen_moving.column + new_pos[1],
        )

        # Deal with conflict
        self._update_conflict()
        if self.get_conflict() == 0:
            self.solved = True

    def draw(self):
        # for i in range(len(self._queens)):
        #     print(f"          -- Queen {i} --")
        #     self._queens[i].draw()
        # print()

        for line in range(self._grid_size):
            line_text = "             "
            for column in range(self._grid_size):
                column_text = "/ "
                for queen in self._queens:
                    if line == queen.line and column == queen.column:
                        column_text = "O "
                line_text += column_text
            print(line_text)
        print("")
        print(f" Number of conflicts : {self.get_conflict()}")
        print("      ==================== ")
        print("")
