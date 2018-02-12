# Given a tic-tac-toe grid with each player's markers, determine which player won.
import numpy as np

def winner(grid, player1, player2):

	grid[grid == player1] = np.int_(1)
	grid[grid == player2] = np.int_(0)
	grid = grid.astype(np.int)
	grid_ad = np.fliplr(grid)

	if np.int(0) in np.sum(grid, axis = 0) or np.int(0) in np.sum(grid, axis = 1) or np.trace(grid) == 0 or np.trace(grid_ad) == 0:
		return "player 2"
	elif 3 in np.sum(grid, axis = 0) or 3 in np.sum(grid, axis = 1) or np.trace(grid) == 3 or np.trace(grid_ad) == 3:
		return "player 1"
	else:
		return "draw"


grid = np.array([["X","O","X"],["X","X","O"],["O","X","X"]])

winner = winner(grid, 'X','O')
print(winner)