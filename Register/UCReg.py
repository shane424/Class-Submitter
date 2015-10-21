from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import username as un 
import password as pw
import searchNumber as sN
# from selenium.webdriver.common.actions
searchNumber = sN.searchNumber
driver = webdriver.Firefox()
driver.get('https://ixpress-server2.uc.edu/Registration/Register.asp')
user = driver.find_element_by_name("Username")
passw = driver.find_element_by_name("Password")
user.send_keys(un.username)
passw.send_keys(pw.password)
log = driver.find_element_by_xpath("//input[@value='Log In']").click()
# log.send_keys("Keys.RETURN")
# log.submit()
# time.sleep(5)
regbut = driver.find_element_by_xpath("//input[@value='Register']").click()
termcode = driver.find_element_by_name("TermCode")
selection = Select(termcode.find_element_by_xpath("//select[@name='TermCode']"))
selection.select_by_visible_text('Spring 2015-16')
conbut = driver.find_element_by_xpath("//input[@value='Continue']").click()
# time.sleep(5)
numb1 = driver.find_element_by_xpath("//input[@name='CallNumber6']")
numb1.send_keys(searchNumber)
sub = driver.find_element_by_xpath("//input[@value='Submit']").click()
# for i in driver.find_element_by_xpath("//input[@name='CallNumber6']"):
	# print i.get_attribute('value')
new = driver.find_element_by_xpath("//input[@name='CallNumber6']")
theone = new.get_attribute('value')
while(theone == searchNumber):
# if(new.get_attribute('value') == '604278'):
		time.sleep(15)
		submi = driver.find_element_by_xpath("//input[@value='Submit']").click()
		new = driver.find_element_by_xpath("//input[@name='CallNumber6']")
		theone = new.get_attribute('value')

	
	
# if(numb1.get_attribute('value') == '604278'):
	# print "yo"
# while(driver.find_ele)
# numb1.submit()
# send_keys("Keys.ARROW_DOWN")
