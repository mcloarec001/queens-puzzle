class Queen:
    line = 0
    column = 0
    nb_conflicts = 0

    def __init__(self, new_line: int, new_column: int):
        """Initiate a Queen object

        Args:
            new_line (int): value of the line position
            new_column (int): value of the column position
        """
        self.line = new_line
        self.column = new_column

    def set_conflicts(self, nb_conflicts: int):
        """Set the number of conflicts of the queen

        Args:
            nb_conflicts (int): the number of conflicts to set
        """
        self.nb_conflicts = nb_conflicts

    def set_position(self, new_line: int, new_column: int):
        """Set the line and the column of the queen

        Args:
            new_line (int): value of line to set
            new_column (int): value of column to set
        """
        self.line = new_line
        self.column = new_column

    def draw(self):
        """Print the queen's position and number of conflicts"""
        print(
            f"Position : [{self.line}, {self.column}]  ; Nombre de conflits : {self.nb_conflicts} "
        )
