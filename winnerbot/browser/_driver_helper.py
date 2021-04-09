import random
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def log_driver(self, url_to_go=False, implicitWait=False, headless=False):
  """Log the chrome driver with the path given"""
  print("Logging the driver..")
  chrome_options = Options()
  chrome_options.add_argument("--lang=en")
  if headless:
    chrome_options.add_argument("--headless")
  self.driver = webdriver.Chrome(self.path_to_driver, options=chrome_options)
  if implicitWait :
    self.driver.implicitly_wait(10)
  if url_to_go:
    self.driver.get(url_to_go)

def close(self):
  self.driver.quit()

METHODS_CATALOG = {
  "id": By.ID,
  "xpath": By.XPATH,
  "tag": By.TAG_NAME,
}

def find_webelement(self, method, path, waiting_time=-1):
  if waiting_time==-1: waiting_time = self.waiting_time
  try:
    return WebDriverWait(self.driver, waiting_time).until(EC.presence_of_element_located((METHODS_CATALOG[method], path)))
  except TimeoutException:
    return False

def click_on_elem(self, method, path, waiting_time=-1):
  web_element = self.find_webelement(method, path, waiting_time)
  if web_element:
    web_element.click()
    return "success"
  return path + " => \033[91mnot found\033[0m"

def fill_field(self, method, path, text, tapEnter=False, waiting_time=-1):
  web_element = self.find_webelement(method, path, waiting_time)
  if web_element:
    web_element.send_keys(text)
    if tapEnter: web_element.send_keys(Keys.RETURN)
    return "success"
  return path + " => \033[91mnot found\033[0m"

def select_option(self, method, path, option_chosen=-1, waiting_time=-1):
  if waiting_time==-1: waiting_time = self.waiting_time

  web_element = self.find_webelement(method, path, waiting_time)
  if web_element:
    wait = WebDriverWait(self.driver, waiting_time)
    wait.until(EC.presence_of_all_elements_located((METHODS_CATALOG["tag"], "option")))
    web_element = self.find_webelement(method, path, waiting_time)
    options = web_element.find_elements_by_tag_name('option')

    if option_chosen==-1 :
      option_chosen == random.randint(0, len(options)-1)
      pass

    option_chosen_found = False

    for option_id in range(0, len(options)):
      if options[option_id].text == option_chosen or option_id==option_chosen:
        option_chosen_found = True
        while not options[option_id].is_displayed() or not options[option_id].is_enabled():
          sleep(0.5)
        options[option_id].click()
        break

    if option_chosen_found:
      return "success"
    else:
      return path + " => option ["+str(option_chosen)+"] \033[91mnot found\033[0m"
  return path + " => \033[91mnot found\033[0m"

def get_webelement_class(self, method, path):
  web_element = find_webelement(self, method, path, 0)
  if web_element:
    return web_element.get_attribute("class")
  return ""

def get_webelement_value(self, method, path):
  web_element = find_webelement(self, method, path, 0)
  if web_element:
    return web_element.text
  return ""

class WebScript(object):
  def __init__(self, waiting_time=10):
    self.running = True
    self.waiting_time = waiting_time

  def new_steps(self, new_steps):
    if self.running :
      return new_steps, self.waiting_time
    else:
      return [], 0