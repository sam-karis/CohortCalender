class Calender(object):

	def __init__(self):
		print('\nWelcome to the Calender App: Calender Initialized\n')
		self.calender = {'Jan':range(1, 32),       #Calculate fo leap year
		                 'Feb':range(1, 30),
		                 'Mar':range(1, 32),
		                 'Apr':range(1, 31),
		                 'May':range(1, 32),
		                 'June':range(1, 31),
		                 'July':range(1, 32),
		                 'Aug':range(1, 32),
		                 'Sept':range(1, 31),
		                 'Oct':range(1, 32),
		                 'Nov':range(1, 31),
		                 'Dec':range(1, 32)}

		self.options = input('What would you like to do?\n1. View list of events\n2. Create an event\n3. View last event')

		if self.options == 1:
			self.add_event()
		elif self.options == 2:
			self.view_list()
		elif self.options == 3:
			self.view_last_event()

	def add_event(self):
		pass

	def view_list(self):
		pass

	def view_last_event(self):
		pass


c = Calender()
#print c.calender