# Using selenium Automated router with different IP

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

# Google seraching
def google_search(driver):
  print('hi')
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

# routing IP
options = webdriver.FirefoxOptions()
options.add_argument("start-maximized")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(chrome_options=options, executable_path="./drivers/geckodriver")
print('Enter the url')
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://sslproxies.org/")
driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//th[contains(., 'IP Address')]"))))
ips = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//tbody//tr[@role='row']/td[position() = 1]")))]
ports = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//tbody//tr[@role='row']/td[position() = 2]")))]
driver.quit()
proxies = []
for i in range(0, len(ips)):
    proxies.append(ips[i]+':'+ports[i])
print(proxies)
for i in range(0, len(proxies)):
  try:
    print("Proxy selected: {}".format(proxies[i]))
    options = webdriver.FirefoxOptions()
    options.add_argument('--proxy-server={}'.format(proxies[i]))
    driver = webdriver.Chrome(chrome_options=options, executable_path="./drivers/geckodriver")
    google_search(driver)
    print('call function')
    if "Proxy Type" in WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.card-text"))):
      print('inside condition')
      break
  except Exception:
      driver.quit()
   
print("Proxy Invoked")

