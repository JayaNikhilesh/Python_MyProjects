from selenium import webdriver

username = bin
password = 2004nikhil

url =

driver = webdriver.chrome()

driver.get(url)

driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)