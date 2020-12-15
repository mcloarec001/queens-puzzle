import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

from Grid import Grid

GRID_SIZE = 8
NB_MAX_TRIES = 10000
NB_HPT = 4


def find_one_solution(grid_size: int, nb_max_tries: int):
    """Finds one solution and displays it

    Args:
        grid_size (int): grid size, x*x
        nb_max_tries (int): maximal attemps to find a solution
    """

    grid = Grid(grid_size)
    grid.draw()

    nb_tries = 0
    while nb_tries < nb_max_tries and grid.nb_conflicts > 0:
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
    grid_size: int,
    nb_max_tries: int,
    proba_random_queen: float,
    proba_random_movement: float,
    drawing: bool = True,
):
    """Simulate the maximal attemps, to find the maximal different possible solutions

    Args:
        grid_size (int): grid size
        nb_max_tries (int): number of maximal attemps
        proba_random_queen (float): probability to move random queens
        proba_random_movement (float): probability to make random moves
        drawing (bool, optional): set to True to print solutions found, otherwise set to False. Defaults to True.

    Returns:
        [str]: the string grid of distinct solutions
    """

    # Make all the intent and keep distinct solutions found
    grid = Grid(grid_size, proba_random_queen, proba_random_movement)
    solutions = []
    for i in range(nb_max_tries):
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


def hyper_parameter_tuning(grid_size: int, nb_max_tries: int, nb_hpt: int):
    """Get the maximal distrinct solutions for different values of parameters

    Args:
        grid_size (int): grid size
        nb_max_tries (int): number of maximal attemps
        nb_hpt (int): number of each parameters to test
    """
    # Define parameters
    proba_queens = np.linspace(0.0, 1.0, nb_hpt)
    proba_movements = np.linspace(0.0, 1.0, nb_hpt)

    # Run simulations
    nb_solutions = [
        [
            find_many_solutions(
                grid_size=grid_size,
                nb_max_tries=nb_max_tries,
                proba_random_queen=proba_queens[i],
                proba_random_movement=proba_movements[j],
                drawing=False,
            )
            for i in tqdm(range(nb_hpt))
        ]
        for j in tqdm(range(nb_hpt))
    ]

    # Display results
    print(nb_solutions)
    plt.figure()
    for i in range(nb_hpt):
        plt.plot(
            proba_queens,
            nb_solutions[i],
            label=f"proba_movement = {proba_movements[i]}",
        )
    plt.title(
        f"Number of solutions found for different values of proba_random_queen and proba_random_movement \n grid_size : {grid_size} \n number of tries : {nb_max_tries} "
    )
    plt.xlabel("proba_random_queen")
    plt.ylabel("Nb of dictinct solutions")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # find_one_solution(GRID_SIZE, NB_MAX_TRIES)
    # find_many_solutions(GRID_SIZE,0.4, 0.4)
    hyper_parameter_tuning(GRID_SIZE, NB_MAX_TRIES, NB_HPT)
