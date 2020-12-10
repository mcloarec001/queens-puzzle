from Grid import Grid
from tqdm import tqdm
import numpy as np
import copy
import matplotlib.pyplot as plt

GRID_SIZE = 20
NB_MAX_TRIES = 50000
NB_HPT = 4


def find_one_solution():
    grid = Grid(GRID_SIZE)
    grid.draw()

    nb_tries = 0
    while nb_tries < NB_MAX_TRIES and grid.nb_conflicts > 0:
        grid.one_turn()
        # grid.draw()
        nb_tries += 1
    grid.draw()
    if grid.nb_conflicts == 0:
        print("THE AI HAS FOUND A SOLUTION !!!")
        print(f"Number of tries : {nb_tries}")
    else:
        print("THE AI COULD NOT FIND A SOLUTION...")


def find_many_solutions(
    proba_random_queen: float, proba_random_movement: float, drawing: bool = True
):

    # Make all the intent and keep all solutions found
    grid = Grid(GRID_SIZE, proba_random_queen, proba_random_movement)
    solutions = []
    for i in range(NB_MAX_TRIES):
        grid.one_turn()
        if grid.nb_conflicts == 0:
            solution = grid.draw(drawing=False)
            if solution not in solutions:
                solutions.append(solution)

    if drawing:
        print(f"{len(solutions)} distinct solutions found")
        for solution in solutions:
            print("------------------   \n")
            print(solution)

    return len(solutions)


def hyper_parameter_tuning(nb_hpt: int):
    proba_queens = np.linspace(0.1, 0.7, nb_hpt)
    proba_movements = np.linspace(0.0, 0.4, nb_hpt)

    nb_solutions = [
        [
            find_many_solutions(proba_queens[i], proba_movements[j], drawing=False)
            for i in tqdm(range(nb_hpt))
        ]
        for j in tqdm(range(nb_hpt))
    ]

    print(nb_solutions)
    fig = plt.figure()
    for i in range(nb_hpt):
        plt.plot(
            proba_queens,
            nb_solutions[i],
            label=f"proba_movement = {proba_movements[i]}",
        )
    plt.title(
        f"Number of solutions found for different values of proba_random_queen and proba_random_movement \n grid_size : {GRID_SIZE} \n number of tries : {NB_MAX_TRIES} "
    )
    plt.xlabel("proba_random_queen")
    plt.ylabel("Nb of dictinct solutions")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # find_one_solution()
    # find_many_solutions(0.4, 0.4)
    hyper_parameter_tuning(NB_HPT)