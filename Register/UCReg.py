from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import selenium
# REQUIRES username.py containing your 6+3 username for UC
# REQUIRES password.py containing your password for your 6+3 username
# REQUIRES searchNumbers.py containing the call numbers you want added in an array; ["123467","654765",...]
# REQUIRES term.py containing the term name found when drop clicking to select which term you want to register for.
# e.g. Spring 2015-16, Fall 2015-16,...

# IF THE CALL NUMBER IS WRONG, IT WILL NOT ADD ANY CLASSES DUE TO A BAD CALL NUMBER

import username as un 
import password as pw
import searchNumber as sN
import term as term


def getNumbs():
	howMany = int(raw_input("How many classes are you adding? "))
	if(howMany > 14):
		while(howMany > 14):
			print("You cannot add more than 14 classes. ")
			howMany = int(raw_input("How many classes are you adding? "))
	numbs = [None] * howMany
	for i in range(0,howMany):
		numbs[i] = raw_input("Enter a course call number. (If call number is invalid no courses will be added) ")
	return numbs
	
def main():
	username = raw_input("Enter your 6+3 username: ")
	password = raw_input("Enter your 6+3 password: ")
	searchNumbers = getNumbs()
	term = raw_input("Enter the term you wish to add classes to. (e.g. Spring 2015-16) ")
	# searchNumbers = sN.searchNumbers
	# term = term.term
	# Opens firefox
	driver = webdriver.Firefox()
	driver.get('https://ixpress-server2.uc.edu/Registration/Register.asp')
	# Finds username/password text boxes
	time.sleep(3)
	user = driver.find_element_by_name("Username")
	passw = driver.find_element_by_name("Password")
	# user.send_keys(un.username)
	# passw.send_keys(pw.password)
	user.send_keys(username)
	passw.send_keys(password)
	# Clicks log in
	log = driver.find_element_by_xpath("//input[@value='Log In']").click()
	# Hits register
	time.sleep(1)
	regbut = driver.find_element_by_xpath("//input[@value='Register']").click()
	# Finds drop down
	time.sleep(1)
	termcode = driver.find_element_by_name("TermCode")
	selection = Select(termcode.find_element_by_xpath("//select[@name='TermCode']"))
	# Clicks semester
	selection.select_by_visible_text(term)
	conbut = driver.find_element_by_xpath("//input[@value='Continue']").click()
	# Writes number into first box 
	# count = 6 - 19, 14 times.
	count = 6
	for i in searchNumbers:
		inp = '//input[@name=\''
		callnumb = 'CallNumber'
		endBrack = '\']'
		call= inp+callnumb+(str(count))+endBrack
		numb1 = driver.find_element_by_xpath(call)
		numb1.send_keys(i)
		count += 1

	time.sleep(3)
	sub = driver.find_element_by_xpath("//input[@value='Submit']").click()
	
if __name__ == "__main__":
	main()
	# Whatever is in the text box after hitting submit. (if worked, nothing. If didn't work, same number)
	# theone = new.get_attribute('value')
	# while(theone == searchNumber):
			# time.sleep(15)
			# submi = driver.find_element_by_xpath("//input[@value='Submit']").click()
			# new = driver.find_element_by_xpath("//input[@name='CallNumber6']")
			# theone = new.get_attribute('value')
