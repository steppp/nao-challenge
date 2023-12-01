''' File containing all the constants and base data structures needed for the project '''

from NAOmove import *
import random

INITIAL_POS = NAOmove('StandInit', 1.68)

# moves which must be executed by the robot, at some point
# the array is shuffled because a specific order is not required
MANDATORY_MOVES = [
    NAOmove('WipeForehead', 8.2),
    NAOmove('Stand', 24),
    NAOmove('Hello', 8.4),
    NAOmove('Sit', 9.84),
    NAOmove('SitRelax', 31),
    NAOmove('StandZero',5.6)
]
random.shuffle(MANDATORY_MOVES)
MANDATORY_MOVES.append(NAOmove('Crouch', 1.32))

# list of possible intermediate moves that the robot can perform
AVAILABLE_MOVES = [
    NAOmove('Rotation_handgun_object', 6.9,),
    NAOmove('Double_movement', 12.3,),
    NAOmove('Right_arm', 18.4,),
    NAOmove('Arms_opening', 14.5),
    NAOmove('Union_arms', 10.8),
    NAOmove('Move_forward', 5),
    NAOmove('Move_backward', 5),
    NAOmove('Diagonal_left', 7.3),
    NAOmove('Diagonal_right', 7.3),
    NAOmove('Rotation_foot_LLeg', 9.2),
    NAOmove('Rotation_foot_RLeg', 9.2),
]

# minimum number of non-mandatory intermediate positions
MIN_INTERMEDIATE_POS = 5

# duration of the song in seconds
SONG_DURATION = 125

FILE_PATH = 'choreography.txt'

NAO_IP = '192.168.178.112'
NAO_PORT = 9559
