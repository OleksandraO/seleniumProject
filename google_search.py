from selenium import webdriver  # class that helps you open browser
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# created object for chromedriver that talks to Chrome Browser
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
# # driver = webdriver.Firefox()
print('maximizing the browser window')
driver.maximize_window()

driver.get('http://www.google.com/')
time.sleep(5)

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('selenium')
search_box.send_keys(Keys.ENTER)
time.sleep(5)

result = driver.find_element(By.ID, 'result-stats')
print(f'Search is done and result text is: {result.text}')

print('closing the browser after test')
driver.quit()
print('Test completed')