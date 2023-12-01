''' Execute the search on the NAO problem using the provided information '''

from support.search import *
from support.reporting import *
from functools import reduce

def search(problem):
    soln = astar_search(problem)
    # soln = breadth_first_graph_search(problem)

    actions = path_actions(soln)
    action_names = list(map(lambda action: list(map(lambda move: move.name, action)), actions))
    # action_names = [move[0] for move in [action for action in actions]]

    states = path_states(soln)
    states_names = list(map(lambda state: state[0].name, states))

    return (action_names, states_names)


if __name__ == '__main__':
    search()
