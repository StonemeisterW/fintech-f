#!/usr/bin/env python3


from view.base_view import BaseView


class MainView(BaseView):

	def show_main_menu(self, profile):
		choice = 0
		
		self.clear()
		if profile == 'admin':
			self.show_admin_menu()
		if profile == 'manager':
			self.show_manager_menu()
		if profile == 'client':
			self.show_client_menu()
			
		try:
			print('Your option:')
			choice = int(input())
		except Exception:
			print('Invalid option. Press ENTER to continue...') 
			input()
		
		return choice	
	
	def show_admin_menu(self):
		print(34 * '#')
		print('# {0:<30} #'.format('Choose an option:'))
		print('# {0:<30} #'.format('100 - Create Branch'))
		print('# {0:<30} #'.format('101 - View Branch List'))
		print('# {0:<30} #'.format('102 - Create Manager'))
		print('# {0:<30} #'.format('103 - View Manager List'))
		print('# {0:<30} #'.format('0 - Exit'))
		print(34 * '#')
		print()

	def show_manager_menu(self):
		print(34 * '#')
		print('# {0:<30} #'.format('Choose an option:'))
		print('# {0:<30} #'.format('200 - Create Account'))
		print('# {0:<30} #'.format('201 - View Account List'))
		print('# {0:<30} #'.format('0 - Exit'))
		print(34 * '#')
		print()

	
	def show_client_menu(self):
		print(34 * '#')
		print('# {0:<30} #'.format('Choose an option:'))
		print('# {0:<30} #'.format('1 - Deposit'))
		print('# {0:<30} #'.format('2 - Withdrawal'))
		print('# {0:<30} #'.format('3 - Account Balance'))
		print('# {0:<30} #'.format('4 - Transaction History'))
		print('# {0:<30} #'.format('0 - Exit'))
		print(34 * '#')
		print()









