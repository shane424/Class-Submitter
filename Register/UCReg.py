from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import username as un 
import password as pw
import searchNumber as sN
searchNumber = sN.searchNumber

# Opens firefox
driver = webdriver.Firefox()
driver.get('https://ixpress-server2.uc.edu/Registration/Register.asp')
# Finds username/password text boxes
user = driver.find_element_by_name("Username")
passw = driver.find_element_by_name("Password")
user.send_keys(un.username)
passw.send_keys(pw.password)
# Clicks log in
log = driver.find_element_by_xpath("//input[@value='Log In']").click()
# Hits register
regbut = driver.find_element_by_xpath("//input[@value='Register']").click()
# Finds drop down
termcode = driver.find_element_by_name("TermCode")
selection = Select(termcode.find_element_by_xpath("//select[@name='TermCode']"))
# Clicks semester
selection.select_by_visible_text('Spring 2015-16')
conbut = driver.find_element_by_xpath("//input[@value='Continue']").click()
# Writes number into first box 
numb1 = driver.find_element_by_xpath("//input[@name='CallNumber6']")
numb1.send_keys(searchNumber)
sub = driver.find_element_by_xpath("//input[@value='Submit']").click()

new = driver.find_element_by_xpath("//input[@name='CallNumber6']")
# Whatever is in the text box after hitting submit. (if worked, nothing. If didn't work, same number)
theone = new.get_attribute('value')
while(theone == searchNumber):
		time.sleep(15)
		submi = driver.find_element_by_xpath("//input[@value='Submit']").click()
		new = driver.find_element_by_xpath("//input[@name='CallNumber6']")
		theone = new.get_attribute('value')
