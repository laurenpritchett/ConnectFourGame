def check_for_winner(board):

# Check for four in a row horizontally
	for row in range(6):
		for col in range(3):
			if board[row][col] == board[row][col + 1] == board[row][col + 2] ==\
			board[row][col + 3] and board[row][col] != " ":
				return board[row][col]

# Check for four in a row vertically
	for col in range(6):
		for row in range(3):
			if board[row][col] == board[row + 1][col] == board[row + 2][col] ==\
			board[row + 3][col] and board[row][col] != " ":
				return board[row][col]

# Check for four in a row diagonally (top-left to bottom-right)
	for row in range(3):
		for col in range(4):
			if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] ==\
			board[row + 3][col + 3] and board[row][col] != " ":
				return board[row]

# Check for four in a row diagonally (bottom-left to top-right)

	for row in range(5, 2, -1):
		for col in range(3):
			if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] ==\
			board[row - 3][col + 3] and board[row][col] != " ":
				return board[row][col]

#No winner: return the empty string
	return ""

def player_one_move(board):
	try:
		valid_move = False
		while not valid_move:
			col = int(raw_input("Select a column to insert a checker (1-7): \n"))
			for row in range(6,0,-1):
				if board[row-1][col-1] == " ":
					board[row-1][col-1] = "A"
					valid_move = True
					break
				else:
					pass
	except NameError:
		print "Please input a number."

	except IndexError:
		print "Oops! Please select a column from 1 to 7."


def player_two_move(board):
	try:
		valid_move = False
		while not valid_move:
			col = int(raw_input("Select a column to insert a checker (1-7): \n"))
			for row in range(6,0,-1):
				if board[row-1][col-1] == " ":
					board[row-1][col-1] = "B"
					valid_move = True
					break
				else:
					pass
	except NameError:
		print "Please input a number."

	except IndexError:
		print "Oops! Please input a column from 1 to 7."

	except ValueError:
		print "Please input a number from 1 to 7"


def display_board(board):
	print " | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " | " + board[0][3] + " | " + board[0][4] + " | " + board[0][5] + " | " + board[0][6] + " | "
	print " |---|---|---|---|---|---|---|"
	print " | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " | " + board[1][3] + " | " + board[1][4] + " | " + board[1][5] + " | " + board[1][6] + " | "
	print " |---|---|---|---|---|---|---|"
	print " | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " | " + board[2][3] + " | " + board[2][4] + " | " + board[2][5] + " | " + board[2][6] + " | "
	print " |---|---|---|---|---|---|---|"
	print " | " + board[3][0] + " | " + board[3][1] + " | " + board[3][2] + " | " + board[3][3] + " | " + board[3][4] + " | " + board[3][5] + " | " + board[3][6] + " | "
	print " |---|---|---|---|---|---|---|"
	print " | " + board[4][0] + " | " + board[4][1] + " | " + board[4][2] + " | " + board[4][3] + " | " + board[4][4] + " | " + board[4][5] + " | " + board[4][6] + " | "
	print " |---|---|---|---|---|---|---|"
	print " | " + board[5][0] + " | " + board[5][1] + " | " + board[5][2] + " | " + board[5][3] + " | " + board[5][4] + " | " + board[5][5] + " | " + board[5][6] + " | "
	print "   1   2   3   4   5   6   7"
	print "         CONNECT FOUR       "

def main():
	free_cells = 42
	player_ones_turn = True
	count = 1
	game_board = [ [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "]]

	while not check_for_winner(game_board) and free_cells > 0:
		display_board(game_board)
		if player_ones_turn:
			print "Player One's Turn!"
			player_one_move(game_board)
			player_ones_turn = not player_ones_turn
		else:
			print "Player Two's Turn!"
			player_two_move(game_board)
			player_ones_turn = not player_ones_turn
		free_cells -= 1

	display_board(game_board)
	if check_for_winner(game_board) == "A":
		print "Player One wins!"
		print "\n GAME OVER"
	elif check_for_winner(game_board) == "B":
		print "Player Two wins!"
		print "\n GAME OVER"
	else:
		print "It's a tie!"
		print "Game Over."

if __name__ == '__main__':
	main()