import pygame, sys


pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

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
					mainloop = False
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

	def hello_world():
		print 'Hello World!'

	screen = pygame.display.set_mode((640, 480), 0, 32)

	menu_items = ('Start', 'Quit')
	funcs = {'Start' : hello_world, 'Quit' : sys.exit}

	pygame.display.set_caption('Test Menu')
	tm = Testmenu(screen, funcs.keys(), funcs)
	tm.run()
