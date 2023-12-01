''' Run the animations in the provided file using the provided connection parameters '''

import constants
import os
import time
import subprocess

def play_choreography(moves, play_song=False):
    if play_song:
        song_command = f'python2 NAOsong.py {constants.NAO_IP} {constants.NAO_PORT}'
        process = subprocess.run(song_command.split(), stdout=subprocess.PIPE)

    for move in moves:
        move_command = f'python2 ./positions/{move}.py {constants.NAO_IP} {constants.NAO_PORT}'
        print(f'Executing move {move}', end='', flush=True)

        start_time = time.time()
        process = subprocess.run(move_command.split(), stdout=subprocess.PIPE)
        end_time = time.time()

        print(f'({str(round(end_time - start_time, 2))})', flush=True)


if __name__ == '__main__':
    moves = None

    if os.path.exists(constants.FILE_PATH):
        with open(constants.FILE_PATH, 'r') as file_in:
            # Read lines and create a list
            moves = [line.strip() for line in file_in]
    else:
        print(f'The specified file does not exist. Edit the FILE_PATH item in the constants.py file.')

    play_choreography(moves)

