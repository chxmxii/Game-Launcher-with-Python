import numpy as np
import pygame
import sys
import math
from threading import Timer
import time 
import pygame as pg
import datetime 
import os
from sys import exit


temps=time.strftime("%Y-%m-%d")
H=datetime.datetime.now().strftime(" %H:%M:%S")


BLUE = ( 250, 218, 221)
BLACK = (0,0,0)
RED = ( 52, 45, 128)
YELLOW = (255, 204, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
	board = np.zeros((ROW_COUNT,COLUMN_COUNT))
	return board

def drop_piece(board, row, col, piece):
	board[row][col] = piece

def is_valid_location(board, col):
	return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			return r

def print_board(board):
	print(np.flip(board, 0))

def winning_move(board, piece):
	# Check horizontal locations for win
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Check positively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

def draw_board(board):
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):		
			if board[r][c] == 1:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 2: 
				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()

board = create_board()
print_board(board)
game_over = False
turn = 0

filepath= os.path.join(r"C:\Users\User\Desktop\Game Launcher v 1.0.0\ConnectDATA",'Connectlog-' + temps + '.txt')
if not os.path.exists(r"C:\Users\User\Desktop\Game Launcher v 1.0.0\ConnectDATA"):
    os.makedirs(r"C:\Users\User\Desktop\Game Launcher v 1.0.0\ConnectDATA")
f = open(filepath, "a")



pygame.init()
pygame.font.init()



SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)



while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		#if event.type == timer:  # checks for timer event
		#	if timer_sec > 0:
		#		timer_sec -= 1
		#		timer_text = timer_font.render("00:%02d" % timer_sec, True, (255, 255, 255))
		#	else:
		#		pygame.time.set_timer(timer, 0)  # turns off timer event


		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			posx = event.pos[0]
			if turn == 0:
				pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
			else: 
				pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			#print(event.pos)
			# Ask for Player 1 Input
			if turn == 0:
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, 1)

					if winning_move(board, 1):
						label = myfont.render("Player 1 won ", 1, RED)
						screen.blit(label, (40,10))
						f.write("Last played game for today was at : " + H + "\n"+ "Winner is : Player 1"+"\n")
						f.close()
						game_over = True


			# # Ask for Player 2 Input
			else:				
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, 2)

					if winning_move(board, 2):
						label = myfont.render("Player 2 won ", 1, YELLOW)
						screen.blit(label, (40,10))
						f.write("Last played game for today was at : " + H + "\n"+ "Winner is : Player 2"+"\n")
						f.close()
						game_over = True

			print_board(board)
			draw_board(board)

			turn += 1
			turn = turn % 2

	#if timer_sec == 0:
	#	box = messagebox.showinfo("time is up","TIME IS UP!!!!!")
	#	f.write(H + "-no winner\n")
	#	f.close()
	#	sys.exit()

	if game_over:
				pygame.time.wait(10)
				time.sleep(5)
				pygame.quit()

def endgame():
        f.write("Last played game for today was at : " + H + "\n"+ "Winner is : Both players lost and the game shut down"+"\n")
        f.close()
        sys.exit()
        
 
  
def main():
    
    
    screen = pg.display.set_mode((740, 390))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(70, 160, 120, 32)
    color_inactive = pg.Color('White')
    color_active = pg.Color('Red')
    color = color_inactive
    active = False
    text = 'Thanks for playing,you will be redirected to the game menu'
    done = False
    pipe=os.popen("Glauncher.py")


    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
      
        screen.fill((35, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)
        pg.display.flip()
        clock.tick(5)
        
      
if __name__ == '__main__':
    pg.init()
    main()
    pg.time.wait(10)
    pg.quit()
    
t = Timer(3.0, main)
t.start() # after 2 seconds, function "main" will run


tt=Timer (120.0,endgame)
tt.start()



