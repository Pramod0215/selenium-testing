# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# browser = webdriver.Firefox(executable_path="./drivers/geckodriver")
# browser.get('http://www.google.com')
# que=browser.find_element_by_name("q")
# que.send_keys("Software Testing")
# que.send_keys(Keys.RETURN)
# search= browser.find_element_by_name("q")
# search.send_keys("selenium")
# search.send_keys(keys.RETURN)
# sleep(5)
# browser.quit()
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# # create a new Firefox session
# driver = webdriver.Firefox(executable_path="./drivers/geckodriver")
# driver.get('https://shop.techdata.com/searchall?b=1&kw=printer')

# items_count = 1

# while True: 
#     items = driver.find_elements_by_class_name('productResult')
#     for i, item in enumerate( items ):
#         if 'EPSON' in item.text:
#             print(items_count + i)
#     items_count += 25
#     try: 
#         driver.find_element_by_xpath('//div[@class="pageNavigation nextPage"]/a').click()
#     except:
#         break

# # close the browser window
# driver.quit()

# Search on google

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# browser = webdriver.Firefox(executable_path="./drivers/geckodriver")
# found=False
# browser.get('http://www.google.com')
# que=browser.find_element_by_name("q")
# que.send_keys("https://www.tutorialspoint.com/software_testing/")
# que.send_keys(Keys.RETURN)
# while True: 
#     print('entry in while loop')
#     browser.find_element_by_xpath('//h3[@class="LC20lb DKV0Md"]/span').click()
#     # print(items,'items')
#     # print(items)
#     # for i, item in enumerate( items ):
#     #     if 'EPSON' in item:
#     #         print(items_count + i)
#     # items_count += 25
#     # try: 
#     #     browser.find_element_by_xpath('//div[@class="d6cvqb nextPage"]/a').click()
#     # except:
#     #     break

# # close the browser window
# browser.quit()

import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# get the path of ChromeDriverServer

# create a new Chrome session
driver = webdriver.Firefox(executable_path="./drivers/geckodriver")
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("http://www.google.com")

# get the search textbox
search_field = driver.find_element_by_name("q")

search_field.send_keys("Digital marketing company in Ahmdanbad")
search_field.submit()
lists=[]
for i in range(0,10):
   try:
      print(i)
      elem = driver.find_element_by_partial_link_text('Tej SolPro: Digital Marketing Agency in Ahmedabad & New York')
      
      if elem.is_displayed():
         elem.click()
         sleep(10) # this will click the element if it is there
         print("FOUND THE LINK CREATE ACTIVITY! and Clicked it!")
            
         break
      
   except:
      next_Google_Search= driver.find_element_by_xpath("//*[contains(local-name(), 'span') and contains(text(), 'Next')]").click()
      print(next_Google_Search)
      print('check condition')
      sleep(3)
      
      print('not found')
      
   
driver.quit()

# from time import sleep
# from selenium import webdriver
# from parsel import Selector
# from selenium.webdriver.common.keys import Keys

# #path to the chromedriver
# driver = webdriver.Firefox(executable_path="./drivers/geckodriver")

# driver.get('https://www.gooogle.com')

# #locate search form by name
# search_query = driver.find_element_by_name('q')

# #Input search words
# search_query.send_keys('X-Men')

# #Simulate return key
# search_query.send_keys(Keys.RETURN)

# Xmen_urls = driver.find_elements_by_class_name('iUh30')

# for page in range(0,10):
#    #  Xmen_urls = [url.text for url in Xmen_urls]

#    #  #loop to iterate through all links in the google search query
#    #  for Xmen_url in Xmen_urls:
#    #       driver.get(Xmen_url)
#    #       sel = Selector(text = driver.page_source)

#     #Go back to google search
#     driver.get('https://www.gooogle.com') 

#     #locate search form by name
#     search_query = driver.find_element_by_name('q')

#     #Input search words
#     search_query.send_keys('X-Men')

#     #Simulate return key
#     search_query.send_keys(Keys.RETURN)
#    #  driver.switch_to.window(driver.window_handles[0])
#     sel = Selector(text = driver.page_source)
#    #  driver.close()
#    #  driver.switch_to.window(driver.window_handles[0])
    


#     #find next page icon in Google search
    
#    #  counter=0
#    #  for page in range(0,9):
#    #    pages=driver.find_elements_by_xpath("//*[@id='nav']/tbody/tr/td/a")
#    #    print(pages)
#    # driver.execute_script("window.open(X-Men_url, 'new_window')")
      
#     page += 1

# next_Google_Search = driver.find_elements_by_xpath("//*[@id='nav']/table/tbody/tr/td/a")
# print(next_Google_Search)
