class Calender(object):

	def __init__(self):
		print('\nWelcome to the Calender App: Calender Initialized\n')
		self.calender = {'Jan':[range(1, 32)],       #Calculate fo leap year
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

		self.options()

	def add_event(self):
		event_name = raw_input('What is the event about?')
		event_month = raw_input('Enter month: ')
		event_date = input('Enter date: ')
		events = {event_name: [event_month, event_date]}

		print events
		self.options()

	def view_list(self):
		pass

	def view_last_event(self):
		pass

	def options(self):
		self.options = input('What would you like to do?\n1. View list of events\n2. Create an event\n3. View last event')

		if self.options == 1:
			return self.add_event()
		elif self.options == 2:
			return self.view_list()
		elif self.options == 3:
			return self.view_last_event()



c = Calender()
