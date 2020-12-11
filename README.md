# udemy-free-course-scraper
This bot scrapes free udemy courses (about development for now) and enrolls you automatically.

# Run pip install -r requirements.txt 
Actually only requirement is selenium so you can just do pip install selenium
("pip3 install" for linux)

# You must have chromedriver in the same folder

# If you want to change directory or use another browser do the following
  a) You want to change dir of chromedriver:
    1-) go to main.py
    2-) find the variable decleration of driver
    3-) inside of the parantheses hardcode directory or use os module
  
  b) You want to change browser 
    1-) go to main.py
    2-) find the variable decleration of driver
    3-) change Chrome class to desired browser (check official selenium documentation for more information)
