from tabulate import tabulate
import calendar

class Calender(object):

	def __init__(self):
		print('\nWelcome to the Calender App: Calender Initialized\n')
		'''
		self.calender = {'Jan':range(1, 32),
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
		                 'Dec':range(1, 32)}'''
		yy = 2016
		mm = 11
		print(calendar.month(yy, mm))

		self.display_events = list()
		self.options()

	def add_event(self):
		events = list()
		event_name = raw_input('What is the event about?: \n')
		event_month = raw_input('Enter month: \n')
		event_date = input('Enter date: \n')
		events.append(event_name)
		events.append(event_month)
		events.append(event_date)
		self.display_events.append(events)
		self.options()

	def view_list(self):
		print tabulate(self.display_events, headers=['Event Name', 'Month', 'Date'], tablefmt="grid")
		return self.options()

	def view_last_event(self):
		last_view = list()
		last_view.append(self.display_events[len(self.display_events) - 1])
		print tabulate(last_view, headers=['Event Name', 'Month', 'Date'], tablefmt="grid")

		return self.options()


	def options(self):
		option = input('\nWhat would you like to do?\n1. Create an event \n2. View list of events\n3. View last event\n')

		if option == 1:
			return self.add_event()
		elif option == 2:
			return self.view_list()
		elif option == 3:
			return self.view_last_event()



c = Calender()