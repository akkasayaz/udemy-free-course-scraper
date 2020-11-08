from selenium.webdriver.common.keys import Keys

class Udemy():
	
	def __init__(self, mail, password):
		self.mail = mail
		self.password = password


	def login(self, element_1, element_2):
		element_1.send_keys(self.mail)
		element_2.send_keys(self.password)
		element_2.send_keys(Keys.RETURN)




if __name__ == '__main__':
	print("Please run main.py")