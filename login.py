from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="./drivers/geckodriver")
driver.get('https://adminportal.ccfutures.org/')


driver.find_element_by_name("username").send_keys("pramodray0215@gmail.com")
driver.find_element_by_name ('password').send_keys('Admin@1122')
driver.find_element_by_tag_name('button').click()
# Fill user's email ID
# email = browser.find_element_by_name('password')
# slow_typing(email, 'Admin@1122')

