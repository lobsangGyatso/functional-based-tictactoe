import pygame
# 


# board=["-","-","-","-","-","-","-","-","-"]
# game_still_going=True
# winner=None

# current_player="X"


# def drawboard():
# 	print(board[0]+"|"+board[1]+"|"+ board[2])
# 	print(board[3] +"|"+board[4]+"|"+board[5])
# 	print(board[6]+"|"+board[7]+"|"+board[8])


# def gameplay():
# 	drawboard()
	
# 	while game_still_going:
# 		handle_turn(current_player)
# 		check_if_game_over()
# 		flip_player()
# 	if winner=="X" or winner=="0":
# 		print("winner is:",winner)
# 	elif winner==None:
# 		print("tie")
# def handle_turn(player):
# 	print("its "+player+"turns")
# 	position=input("enter the number fornm 1-9:")

# 	position=int(position)-1
# 	board[position]=player
# 	drawboard()		

# def check_if_game_over():
# 	check_for_winner()
# 	check_if_tie()

# def check_for_winner():
# 	global winner
# 	# check row
# 	row_winner=check_row()
# 	# check column
# 	column_winner=check_column()
# 	# check diagonal
# 	diagonal_winner=check_diagonal()
# 	if row_winner:
# 		winner=row_winner
# 	elif column_winner:
# 		winner=column_winner
# 	elif diagonal_winner:
# 		winner=diagonal_winner
# 	else:
# 		winner=None

# 	pass
# def check_row():
# 	# 	global variable
# 	global game_still_going

# 	row1= board[0] ==board[1]==board[2] !="-"
# 	row2= board[3] ==board[4]==board[5] !="-"
# 	row3= board[6] ==board[7]==board[8] !="-"

# 	if row1 or row2 or row3:
# 		game_still_going=False

# 	if row1:
# 		return board[0]
# 	if row2:
# 		return board[3]
# 	if row3:
# 		return board[6]

# def check_column():
# 	global game_still_going

# 	col1= board[0] ==board[3]==board[6] !="-"
# 	col2= board[1] ==board[4]==board[7] !="-"
# 	col3= board[2] ==board[5]==board[8] !="-"

# 	if col1 or col2 or col3:
# 		game_still_going=False

# 	if col1:
# 		return board[0]
# 	if col2:
# 		return board[1]
# 	if col3:
# 		return board[2]

# def check_diagonal():
# 	global game_still_going

# 	diagonal1= board[0] ==board[4]==board[8] !="-"
# 	diagonal2= board[6] ==board[4]==board[2] !="-"
	

# 	if diagonal1 or diagonal2:
# 		game_still_going=False

# 	if diagonal1:
# 		return board[0]
# 	if diagonal2:
# 		return board[6]
	
# def check_if_tie():
# 	global game_still_going
# 	if "-" not in board:
# 		game_still_going=False

# def flip_player():
# 	global current_player
# 	if current_player =="X":
# 		current_player ="0"
# 	elif current_player =="0":
# 		current_player="X"
# gameplay()


# class tictactoe:

# 	def __init__(self):
# 		pass


	


class playerX:
	def __init__(self,player):
		self.player=player
	def returnplayer(self):
		return self.player


class player0:
	def __init__(self,player):
		self.player=player
	def returnplayer(self):
		return self.player

class game:
	p1=playerX("X")
	l1=p1.returnplayer()
	p2=player0("0")
	l2=p2.returnplayer()
	player=l1
	def __init__(self,play):
		self.play=play
		self.board=["-","-","-","-","-","-","-","-","-"]
	def drawboard(self):
		print(self.board[0]+"|"+self.board[1]+"|"+ self.board[2])
		print(self.board[3] +"|"+self.board[4]+"|"+self.board[5])
		print(self.board[6]+"|"+self.board[7]+"|"+self.board[8])

	def gameplay(self):
		self.drawboard()
		while self.play:
			self.checkplayer(self.player)
			self.check_if_game_over()
			self.flip_player()
	def checkplayer(self,player):
		print("player is :",player)
		position=input("enter the number from 1-9  :")
		position=int(position)-1
		self.board[position]=player
		self.drawboard()	

	def check_if_game_over(self):
		pass
	def flip_player(self):
		global player
		if self.player == self.l1:
			self.player = self.l2
		elif self.player ==self.l2:
			self.player =self.l1

g=game("True")
g.gameplay()

