from random import randint 
import numpy
import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Dice Simulator')


black = (0,0,0)

one = pygame.image.load("dice1.png")
two = pygame.image.load("dice2.png")
three = pygame.image.load("dice3.png")
four = pygame.image.load("dice4.png")
five = pygame.image.load("dice5.png")
six = pygame.image.load("dice6.png") 




no_of_dice = raw_input("Select number of dice (1-4) --->")

def roll(n):
	if int(n) == 1:
		num1 = randint(1,6)
		num2 = 0
		num3 = 0
		num4 = 0
		return num1, num2, num3, num4
	elif int(n) == 2:
		num1 = randint(1,6)
		num2 = randint(1,6)
		num3 = 0
		num4 = 0
		return num1, num2, num3, num4
	elif int(n) == 3:
		num1 = randint(1,6)
		num2 = randint(1,6)
		num3 = randint(1,6)
		num4 = 0
		return num1, num2, num3, num4
	elif int(n) == 4:
		num1 = randint(1,6)
		num2 = randint(1,6)
		num3 = randint(1,6)
		num4 = randint(1,6)
		return num1, num2, num3, num4
	

num = roll(no_of_dice)


while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			num = roll(no_of_dice)

	


	if num[0] == 1:
		dice1 = one
	elif num[0] == 2:
		dice1 = two
	elif num[0] == 3:
		dice1 = three
	elif num[0] == 4:
		dice1 = four
	elif num[0] == 5:
		dice1 = five
	elif num[0] == 6:
		dice1 = six

	if num[1] == 1:
		dice2 = one
	elif num[1] == 2:
		dice2 = two
	elif num[1] == 3:
		dice2 = three
	elif num[1] == 4:
		dice2 = four
	elif num[1] == 5:
		dice2 = five
	elif num[1] == 6:
		dice2 = six
	else:
		dice2 = None

	if num[2] == 1:
		dice3 = one
	elif num[2] == 2:
		dice3 = two
	elif num[2] == 3:
		dice3 = three
	elif num[2] == 4:
		dice3 = four
	elif num[2] == 5:
		dice3 = five
	elif num[2] == 6:
		dice3 = six
	else:
		dice3 = None

	if num[3] == 1:
		dice4 = one
	elif num[3] == 2:
		dice4 = two
	elif num[3] == 3:
		dice4 = three
	elif num[3] == 4:
		dice4 = four
	elif num[3] == 5:
		dice4 = five
	elif num[3] == 6:
		dice4 = six
	else:
		dice4 = None


	screen.fill(black)
	screen.blit(dice1, (0,0))
	if dice2 != None:
		screen.blit(dice2, (250,0))
	if dice3 != None:
		screen.blit(dice3, (0,250))
	if dice4 != None:
		screen.blit(dice4, (250,250))
	pygame.display.flip()

























