# from selenium import webdriver
# for i in range(0,windows):
#     PROXY = "localhost:8080"

#     # Create a copy of desired capabilities object.
#     desired_capabilities = webdriver.DesiredCapabilities.CHROME.copy()
#     # Change the proxy properties of that copy.
#     desired_capabilities['proxy'] = {
#         "httpProxy":PROXY,
#         "ftpProxy":PROXY,
#         "sslProxy":PROXY,
#         "noProxy":None,
#         "proxyType":"MANUAL",
#         "class":"org.openqa.selenium.Proxy",
#         "autodetect":False
#     }

#     # you have to use remote, otherwise you'll have to code it yourself in python to 
#     # dynamically changing the system proxy preferences
#     driver = webdriver.Chrome(executable_path="drivers/chromedriver",
#              desired_capabilities=desired_capabilities)


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
browser.get('http://www.google.com')

search = browser.find_element_by_name('q')
search.send_keys("google search through python")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results
browser.quit()