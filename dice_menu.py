import pygame, sys
from random import randint 


pygame.init()
pygame.mixer.init()
myfont = pygame.font.SysFont(None, 30)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
speed = [2, 2]
size = width, height = 320, 240
pics = []
for n in range(1,21):
	 pics.append(pygame.image.load("test/num%s.jpg" % n))

noise = pygame.mixer.Sound("ShakeNRoll.wav")
class MenuItem(pygame.font.Font):
    def __init__(self, text, font=None, font_size=30, font_color=white, (pos_x, pos_y)=(0, 0)):
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
	def __init__(self, screen, items, funcs, header, bg_colour= black, font =None, font_size = 30, font_color = white):
		self.screen = screen
		self.scr_width = self.screen.get_rect().width
		self.scr_height = self.screen.get_rect().height
		self.bg_colour = bg_colour
		self.font = pygame.font.SysFont(font, font_size)
		self.font_color = font_color
		self.header = header

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
		#backimg = pygame.image.load("mountains.jpg").convert()
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
			#self.screen.blit(backimg, (0,0))
			title = myfont.render(self.header,1,white)
			self.screen.blit(title, (200,50))

			for item in self.items:
				if self.mouse_is_visible:
					mpos = pygame.mouse.get_pos()
					self.set_mouse_selection(item, mpos)
				self.screen.blit(item.label, item.position)
			pygame.display.flip()



if __name__ == '__main__':


	def dice(i,n):
				def roll():
					num1 = randint(1,n)
					num2 = randint(1,n)
					num3 = randint(1,n)
					num4 = randint(1,n)
					return num1, num2, num3, num4
				num = roll()
				thing = 1
				while thing == 1:
					for event in pygame.event.get():
						if event.type == pygame.QUIT: 
							sys.exit()
						elif event.type == pygame.MOUSEBUTTONDOWN:
							num = roll()
						elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
							num = roll()
						elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
							thing = 0
						elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
							sys.exit()
					dice1 = None
					dice2 = None
					dice3 = None
					dice4 = None
					dice1 = pics[num[0]-1]
					if i > 1:
						dice2 = pics[num[1]-1]
					if i >2:
						dice3 = pics[num[2]-1]
					if i >3:
						dice4 = pics[num[3]-1]

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

	def d4():
		def d_1():
			dice(1,4)
		def d_2():
			dice(2,4)
		def d_3():
			dice(3,4)
		def d_4():
			dice(4,4)
		theitems =  ('One', 'Two', 'Three', 'Four', 'Quit')
		thefuncs = {'One' : d_1, 'Two' : d_2, 'Three' : d_3, 'Four' : d_4, 'Quit' : sys.exit}
		theheader = 'Select Number of Dice'
		the = Testmenu(screen, theitems, thefuncs, theheader)
		the.run()
		tm.run()	
	def d6():
		def d_1():
			dice(1,6)
		def d_2():
			dice(2,6)
		def d_3():
			dice(3,6)
		def d_4():
			dice(4,6)
		theitems =  ('One', 'Two', 'Three', 'Four', 'Quit')
		thefuncs = {'One' : d_1, 'Two' : d_2, 'Three' : d_3, 'Four' : d_4, 'Quit' : sys.exit}
		theheader = 'Select Number of Dice'
		the = Testmenu(screen, theitems, thefuncs, theheader)
		the.run()
		tm.run()	
	def d8():
		def d_1():
			dice(1,8)
		def d_2():
			dice(2,8)
		def d_3():
			dice(3,8)
		def d_4():
			dice(4,8)
		theitems =  ('One', 'Two', 'Three', 'Four', 'Quit')
		thefuncs = {'One' : d_1, 'Two' : d_2, 'Three' : d_3, 'Four' : d_4, 'Quit' : sys.exit}
		theheader = 'Select Number of Dice'
		the = Testmenu(screen, theitems, thefuncs, theheader)
		the.run()
		tm.run()
	def d10():
		def d_1():
			dice(1,10)
		def d_2():
			dice(2,10)
		def d_3():
			dice(3,10)
		def d_4():
			dice(4,10)
		theitems =  ('One', 'Two', 'Three', 'Four', 'Quit')
		thefuncs = {'One' : d_1, 'Two' : d_2, 'Three' : d_3, 'Four' : d_4, 'Quit' : sys.exit}
		theheader = 'Select Number of Dice'
		the = Testmenu(screen, theitems, thefuncs, theheader)
		the.run()
		tm.run()
	def d12():
		def d_1():
			dice(1,12)
		def d_2():
			dice(2,12)
		def d_3():
			dice(3,12)
		def d_4():
			dice(4,12)
		theitems =  ('One', 'Two', 'Three', 'Four', 'Quit')
		thefuncs = {'One' : d_1, 'Two' : d_2, 'Three' : d_3, 'Four' : d_4, 'Quit' : sys.exit}
		theheader = 'Select Number of Dice'
		the = Testmenu(screen, theitems, thefuncs, theheader)
		the.run()
		tm.run()
	def d20():
		def d_1():
			dice(1,20)
		def d_2():
			dice(2,20)
		def d_3():
			dice(3,20)
		def d_4():
			dice(4,20)
		theitems =  ('One', 'Two', 'Three', 'Four', 'Quit')
		thefuncs = {'One' : d_1, 'Two' : d_2, 'Three' : d_3, 'Four' : d_4, 'Quit' : sys.exit}
		theheader = 'Select Number of Dice'
		the = Testmenu(screen, theitems, thefuncs, theheader)
		the.run()
		tm.run()

	screen = pygame.display.set_mode((640, 640), 0, 32)

	menu_items = ('d4','d6', 'd8', 'd10', 'd12', 'd20', 'Quit')
	funcs = {'d4' : d4, 'd6' : d6, 'd8' : d8, 'd10' : d10, 'd12' : d12, 'd20' : d20, 'Quit':sys.exit}
	header = 'Select Dice Type'
	pygame.display.set_caption('Dice Simulator')
	tm = Testmenu(screen, menu_items, funcs, header)
	tm.run()
