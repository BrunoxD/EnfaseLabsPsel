import numpy as np

"""
0:2
X:1
.:5

SUM(O) == 6 : 0 Winner
SUM(X) == 3 : X Winner
"""

def readBoard():	
	board = []
	[board.append(i) for i in input()]	
	[board.append(i) for i in input()]	
	[board.append(i) for i in input()]	

	for i in range(len(board)):
		if board[i] == 'X':
			board[i] = 1
		elif board[i] == '.':
			board[i] = 5
		else:
			board[i] = 2
	return np.array(board).reshape(3, 3)

def checkWinners(board):
	X = (board == 2).sum()
	O = (board == 1).sum()
	empty = (board == 5).sum()
	O_Winner = False
	X_Winner = False

	# Valid Game?
	if abs(X-O) > 1:
		return "inválido"

	# There is a Winner?

	# Horizontal Check
	H = board.sum(axis = 0) 
	
	if(H[0] == 6 or H[1] == 6 or H[2] == 6):
		O_Winner = True
	if(H[0] == 3 or H[1] == 3 or H[2] == 3):
		X_Winner = True

	# Vertical Check
	V = board.sum(axis = 1) 
	
	if(V[0] == 6 or V[1] == 6 or V[2] == 6):
		O_Winner = True
	if(V[0] == 3 or V[1] == 3 or V[2] == 3):
		X_Winner = True

	# Diagonals Check
	D1 = board.trace()
	if(D1 == 6):
		O_Winner = True
	if(D1 == 3):
		X_Winner = True

	D2 = board[::-1].trace()
	if(D2 == 6):
		O_Winner = True
	if(D2 == 3):
		X_Winner = True

	# Who is the Winner?
	if O_Winner == True and X_Winner == True:
		return "inválido"	
	elif O_Winner == True or X_Winner == True:
		if X == O:
			return "segundo_venceu"
		else:
			return "primeiro_venceu"
	elif not empty:
		return "empate"		
	# Next move?
	elif X == O:
		return "primeiro"
	else:
		return "segundo"

if __name__ == '__main__':
	board = readBoard()		
	print(checkWinners(board))
