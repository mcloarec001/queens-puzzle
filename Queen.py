class Queen:
    line = 0
    column = 0
    nb_conflicts = 0

    def __init__(self, new_line: int, new_column: int):
        self.line = new_line
        self.column = new_column

    def set_conflicts(self, nb_conflicts: int):
        self.nb_conflicts = nb_conflicts

    def set_position(self, new_line: int, new_column: int):
        self.line = new_line
        self.column = new_column

    def draw(self):
        print(
            f"Position : [{self.line}, {self.column}]  ; Nombre de conflits : {self.nb_conflicts} "
        )
