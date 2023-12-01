''' Extension of the Problem class used to describe the search problem in the NAO moves space '''

from support.search import *
from functools import reduce
import random
import constants
from NAOmove import *

COOLDOWN_TURNS = 2
MOVES_STEP_RATIO = 3
MIN_ACTIONS_NUMBER = 5

class NAOproblem(Problem):
	def __init__(self, initial, goals, time, moves):
		self.initial = initial
		self.goal = goals
		self.moves = moves
		self.MOVES_PER_STEP = len(moves) // MOVES_STEP_RATIO
		# subtract early the time left using thd duration times of the mandatory positions
		time_left = time - initial.duration - sum([move.duration for move in goals])
		# (prev_pos, next_pos_index, cooldown_moves=(move, cooldown_turns [max 2]), time_left, actions_left, ?overall_penalty?)
		self.initial = (initial, 0, (), time_left, MIN_ACTIONS_NUMBER, 0)
		super().__init__(self.initial, self.goal)

	def actions(self, state):
		_, next_pos_index, _, time_left, _, _ = state
		if next_pos_index == len(self.goal) and time_left > 3:
			# invalid state
			return []
		
		result = []
		moves = [move for move in self.moves]
		random.shuffle(moves)
		result += [(move1, move2, move3) for move1 in moves for move2 in moves for move3 in moves \
if move1.name > move2.name and move2.name > move3.name][:3]

		random.shuffle(moves)
		result += [(move1, move2) for move1 in self.moves for move2 in self.moves if move1 != move2][:3]

		# here we should just generate the entire search space for the current state
		# we will update the state accordingly in the result function 
		random.shuffle(moves)
		result += [(move, ) for move in self.moves][:3]
		
		return result

	def result(self, state, action):
		print(f'State for action {str(action)} is {str(state)}')

		prev_pos, next_pos_index, cooldown_moves, time_left, actions_left, penalty = state
		next_pos = self.goal[next_pos_index]

		action = action if action != (None, ) else ()

		# compute the penalty for repeating actions in cooldown
		moves_names = [move.name for move in action]
		repetition_penalty = sum([cooldown for name, cooldown in cooldown_moves if name in moves_names])

		# reduce action cooldown for actions performed in the previous steps
		# or reduce the cooldown for non-chosen actions
		new_cooldown_moves = []
		for cooldown_move in cooldown_moves:
			indexed_move = next(((i, name) for i, name in enumerate(moves_names) if name == cooldown_move[0]), None)
			if indexed_move != None:
				i, name = indexed_move
				# a move that was in cooldown has just been used
				# reset the cooldown to its maximum value
				new_cooldown_moves.append((name, COOLDOWN_TURNS))
				moves_names.pop(i)
			else:
				# a move that was in cooldown has NOT been used
				# decrease the cooldown by 1 and remove and avoid adding it to the new cooldown moves array
				# if cooldown turns value reaches 0
				if cooldown_move[1] > 1:
					new_cooldown_moves.append((cooldown_move[0], cooldown_move[1] - 1))
		
		# add all the actions which were not in cooldown before to the cooldown array
		for move_name in moves_names:
			new_cooldown_moves.append((move_name, COOLDOWN_TURNS))

		# update the number of actions which still needs to be done (should be at least 5)
		actions_left = actions_left - len(action)
		# update the time left based on the actions performed
		time_left -= reduce(lambda acc, curr: curr.duration + acc, action, 0)

		# update prev and next position
		prev_pos = next_pos
		next_pos_index += 1

		return (prev_pos, next_pos_index, tuple(new_cooldown_moves), time_left, actions_left, repetition_penalty)

	def goal_test(self, state):
		prev_pos, next_pos_index, cooldown_moves, time_left, actions_left, penalty = state
		is_goal = next_pos_index == len(self.goal) and actions_left <= 0 and time_left < 5
		return is_goal

	def path_cost(self, c, state1, action, state2):
		# compute the cost to reach this step
		_, _, _, time_left, actions_left, penalty = state2
		return c + penalty**2

	def h(self, node):
		_, _, cooldown_moves, time_left, actions_left, penalty = node.state
		result = sum([turns for _, turns in cooldown_moves])
		result += 2 * penalty
		result += abs(time_left)
		return result
