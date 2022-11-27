from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
import time

HOST = "https://demoqa.com/automation-practice-form"

# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
print('maximizing the browser window')
driver.maximize_window()
# This sets a sticky timeout to implicitly wait for an element to be found, or a command to complete.
driver.implicitly_wait(20)

try:
    print("Starting test with various locator to use in find_element() method.")
    driver.get(HOST)
    # time.sleep(5)
    # enter first_name ='john', enter last_name = 'doe', enter email = 'jdoe@gmail.com'
    # select radio button Gender = Male
    # mobile_number = 9876543210
    # enter date_of_birth = 27 Nov 2000
    # enter subjects = "selenium forms testing"
    # select checkboxes, select Sports, Reading
    # (optional) upload picture
    # enter message in text_area = '2906 Shell Road, 12224'
    # check is City List is enabled
    # select state=NCR
    # select city=Delhi
    # check if Male gender is selected
    # check if Sports Hobbies is selected
    # check is City List is enabled
    # click submit
    # verify the message="Thanks for submitting the form"


except Exception as err:
    print("Python Exception: test failed with following exception.")
    print(err)
except (NoSuchElementException, TimeoutException) as err:
    print("Selenium Exception: test failed with following exception.")
    print(err)
finally:
    # close all tabs:
    driver.quit()
    # pass