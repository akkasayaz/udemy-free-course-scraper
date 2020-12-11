from logger import Udemy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time

mail = input("Enter your e-mail")
password = getpass("Enter your Udemy password")

user = Udemy(mail, password)


browser = webdriver.Chrome("chromedriver.exe")

browser.get("https://www.udemy.com/join/login-popup/")
time.sleep(3)

email = browser.find_element_by_name("email")

sifre = browser.find_element_by_name("password")

user.login(email, sifre) 

browser.get('https://www.udemyfreebies.com/course-category/development')

coup_but = browser.find_elements_by_class_name('button-icon')


for course in coup_but:
	course.click()
	time.sleep(1)
	nb = browser.find_element_by_class_name('button-icon')
	nb.click()
	time.sleep(1)
	cart = browser.find_element_by_class_name('udlite-btn udlite-btn-large udlite-btn-brand udlite-heading-md add-to-cart')
	cart.click()
	browser.get('https://www.udemyfreebies.com/course-category/development')
	time.sleep(1)	
user.buy()
