import pygame, sys
from random import randint 


pygame.init()

myfont = pygame.font.SysFont(None, 30)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
speed = [2, 2]
size = width, height = 320, 240

one = pygame.image.load("dice1.png")
two = pygame.image.load("dice2.png")
three = pygame.image.load("dice3.png")
four = pygame.image.load("dice4.png")
five = pygame.image.load("dice5.png")
six = pygame.image.load("dice6.png") 

class MenuItem(pygame.font.Font):
    def __init__(self, text, font=None, font_size=30,
                 font_color=white, (pos_x, pos_y)=(0, 0)):
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def is_mouse_selection(self, (posx, posy)):
	    if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
	        (posy >= self.pos_y and posy <= self.pos_y + self.height):
	            return True
	    return False

    def set_font_color(self, rgb_tuple):
	 	self.font_color = rgb_tuple
	 	self.label = self.render(self.text, 1, self.font_color)

    

class Testmenu():
	def __init__(self, screen, items, funcs, bg_colour= black, font =None, font_size = 30, font_color = white):
		self.screen = screen
		self.scr_width = self.screen.get_rect().width
		self.scr_height = self.screen.get_rect().height
		self.bg_colour = bg_colour
		self.font = pygame.font.SysFont(font, font_size)
		self.font_color = font_color

		self.items = []
		for index, item in enumerate(items):
			menu_item = MenuItem(item)

			total_h = len(items) + menu_item.height
			pos_x = (self.scr_width/2) - (menu_item.width/2)
			pos_y = (self.scr_height/2) - (total_h/2) + ((index * 2) + index * menu_item.height)

			menu_item.set_position(pos_x, pos_y)
			self.items.append(menu_item)

		
		self.clock = pygame.time.Clock()
		self.mouse_is_visible = True
		self.cur_item = None
		self.funcs = funcs

	def set_mouse_selection(self, item, mpos):
		if item.is_mouse_selection(mpos):
			item.set_font_color(red)
		else:
			item.set_font_color(white)

	def set_keyboard_selection(self, key):
		for item in self.items:
			item.set_font_color(white)

		if self.cur_item is None:
			self.cur_item = 0
		else:
			if key == pygame.K_UP and self.cur_item > 0:
				self.cur_item -= 1
			elif key == pygame.K_UP and self.cur_item == 0:
				self.cur_item = len(self.items) - 1
			elif key == pygame.K_DOWN and self.cur_item < len(self.items) - 1:
				self.cur_item += 1
			elif key == pygame.K_DOWN and self.cur_item == len(self.items) - 1:
				self.cur_item = 0

		self.items[self.cur_item].set_font_color(red)

	def set_mouse_visibility(self):
		if self.mouse_is_visible:
			pygame.mouse.set_visible(True)
		else:
			pygame.mouse.set_visible(False)


	def run(self):
		mainloop = True
		while mainloop == True:
			self.clock.tick(60)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					self.mouse_is_visible = False
					self.set_keyboard_selection(event.key)
					if event.key == pygame.K_RETURN:
						text = self.items[self.cur_item].text
						mainloop = False
						self.funcs[text]()
				if event.type == pygame.MOUSEBUTTONDOWN:
					mpos = pygame.mouse.get_pos()
					for item in self.items:
						if item.is_mouse_selection(mpos):
							mainloop = False
							self.funcs[item.text]()

			if pygame.mouse.get_rel() != (0,0):
				self.mouse_is_visible = True

			self.set_mouse_visibility()
			self.screen.fill(self.bg_colour)

			for item in self.items:
				if self.mouse_is_visible:
					mpos = pygame.mouse.get_pos()
					self.set_mouse_selection(item, mpos)
				self.screen.blit(item.label, item.position)
			pygame.display.flip()



if __name__ == '__main__':
	
	def die():
		num = randint(1,6)
		

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					num = randint(1,6)
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
					num = randint(1,6)
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
					tm.run()
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					sys.exit()

			
			if num == 1:
				dice1 = one
			elif num == 2:
				dice1 = two
			elif num == 3:
				dice1 = three
			elif num == 4:
				dice1 = four
			elif num == 5:
				dice1 = five
			elif num == 6:
				dice1 = six

			note = "Reroll : click/return    Menu : backspace    Quit : escape"
			label = myfont.render(note,1,white)
			
			screen.fill(black)
			screen.blit(dice1, (0,0))
			screen.blit(label, (50, 550))

			pygame.display.flip()
	
	def dice_2():
		def roll():
			num1 = randint(1,6)
			num2 = randint(1,6)
			return num1, num2

		num = roll()

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					num = roll()
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
					num = roll()
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
					tm.run()
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					sys.exit()

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

			note = "Reroll : click/return    Menu : backspace    Quit : escape"
			label = myfont.render(note,1,white)

			screen.fill(black)
			screen.blit(dice1, (0,0))
			if dice2 != None:
				screen.blit(dice2, (250,0))
			screen.blit(label, (50, 550))
			pygame.display.flip()


	def dice_3():
		def roll():
			num1 = randint(1,6)
			num2 = randint(1,6)
			num3 = randint(1,6)
			return num1, num2, num3

		num = roll()

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					num = roll()
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
					num = roll()
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
					tm.run()
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					sys.exit()

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

			note = "Reroll : click/return    Menu : backspace    Quit : escape"
			label = myfont.render(note,1,white)

			screen.fill(black)
			screen.blit(dice1, (0,0))
			if dice2 != None:
				screen.blit(dice2, (250,0))
			if dice3 != None:
				screen.blit(dice3, (0,250))
			screen.blit(label, (50, 550))
			pygame.display.flip()

	def dice_4():
		def roll():
			num1 = randint(1,6)
			num2 = randint(1,6)
			num3 = randint(1,6)
			num4 = randint(1,6)
			return num1, num2, num3, num4

		num = roll()

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					num = roll()
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
					num = roll()
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
					tm.run()
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					sys.exit()

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

			note = "Reroll : click/return    Menu : backspace    Quit : escape"
			label = myfont.render(note,1,white)

			screen.fill(black)
			screen.blit(dice1, (0,0))
			if dice2 != None:
				screen.blit(dice2, (250,0))
			if dice3 != None:
				screen.blit(dice3, (0,250))
			if dice4 != None:
				screen.blit(dice4, (250,250))
			screen.blit(label, (50, 550))
			pygame.display.flip()

	screen = pygame.display.set_mode((640, 640), 0, 32)

	menu_items = ('One', 'Two', 'Three', 'Four', 'Quit')
	funcs = {'One' : die, 'Two' : dice_2, 'Three' : dice_3, 'Four' : dice_4, 'Quit' : sys.exit}

	pygame.display.set_caption('Dice Simulator')
	tm = Testmenu(screen, menu_items, funcs)
	tm.run()
