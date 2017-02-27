from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#the login page location (lives in an apache server on the local network)
LOGIN_URL = "http://192.168.1.124/login.html"

#username and password
usr = ""
pw = ""

#init webdriver
driver = webdriver.Firefox()

#login
driver.get(LOGIN_URL)
main_handle = driver.current_window_handle
for handle in driver.window_handles:       #gets a handle to the popup
    if handle != main_handle:
        signin_handle = handle
        break
sleep(1)                                   #sleep so popup can load
driver.switch_to.window(signin_handle)     #switch to popup

#do the login
elem = driver.find_element_by_id('email')
elem.send_keys(usr)
elem = driver.find_element_by_id('pass')
elem.send_keys(pw)
elem = driver.find_element_by_id('loginbutton')
elem.click()
sleep(3)

#switch back to main window
driver.switch_to.window(main_handle)
sleep(2)
elem = driver.find_element_by_id('token')
print elem.get_attribute('innerHTML')


#elem = driver.find_element_by_id('token')
#print elem


#using selenium might be a better idea?
