from Grid import Grid

GRID_SIZE = 10


# TODO : gérer les cas où la dame ne peut pas être bougée
# TODO : bouger les dames dans des cases avec un minimum de conflit ?


def main():
    grid = Grid(GRID_SIZE)
    grid.draw()
    nb_max_tries = 1000
    nb_tries = 0
    while nb_tries < nb_max_tries and grid.solved == False:
        grid.one_turn()
        grid.draw()
        nb_tries += 1
    if grid.solved:
        print("THE AI HAS FOUND A SOLUTION !!!")
        print(f"Number of tries : {nb_tries}")
    else:
        print("THE AI COULD NOT FIND A SOLUTION...")


if __name__ == "__main__":
    main()
