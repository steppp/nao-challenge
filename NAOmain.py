''' Runs all the algorithm steps to find the best choreography and executes it '''

from NAOsearch import search
from NAOproblem import NAOproblem
from NAOperform import play_choreography
import constants

def find_choreography():
    problem = NAOproblem(constants.INITIAL_POS, constants.MANDATORY_MOVES, constants.SONG_DURATION, constants.AVAILABLE_MOVES)
    return search(problem)

def merge_actions_states(actions, states):
    result = []
    i = 0
    while i < len(states):
        result.append(states[i])
        if i < len(actions):
            for action in actions[i]:
                result.append(action)
        i += 1

    return result

def save_results(moves):
    with open(constants.FILE_PATH, 'w') as file_out:
        for move in moves:
            file_out.write(move + '\n')

def main():
    # compute the choreography
    actions, states = find_choreography()

    # get the sequence of moves
    result = merge_actions_states(actions, states)

    # save results to disk
    save_results(result)

    # send moves to NAO which will perform them
    play_choreography(result, play_song=True)


if __name__ == '__main__':
    main()
