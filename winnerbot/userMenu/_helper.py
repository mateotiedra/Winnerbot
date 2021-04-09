#in this file all the function that can be useful everywhere
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

__name__ = "helper"

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


def logDriver(pathToDriver, implicitWait, headless):
  """Log the chrome driver with the path given"""
  chrome_options = Options()
  chrome_options.add_argument("--lang=en")
  if headless:
    chrome_options.add_argument("--headless")
  driver = webdriver.Chrome(pathToDriver, options=chrome_options)
  if implicitWait :
    driver.implicitly_wait(10)
  print("\033c")
  return driver

def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    pass

  try:
    import unicodedata
    unicodedata.numeric(s)
    return True
  except (TypeError, ValueError):
    pass
  
  return False

def choose_between( *options ):
  for i in range(0, len(options)):
    print("["+str(i+1)+"] "+options[i])

  choice = input("\n>> ")

  if is_number(choice) and int(choice)<=len(options):
    return int(choice)

  print("\033c")
  return choose_between( *options )

def confirm_choice(optTrue, optFalse):
  choice = choose_between(optTrue, optFalse)
  if choice == 1:
    return True
  elif choice == 2:
    return False
  else:
    return confirm_choice(optTrue, optFalse)

def choose_ID(listFakeIDs, extra_param=False, waited_param=""):
  """Make the user choose a FakeID and return his choice"""
  print("\033c")
  print("Choisir une fake ID pour effectuer cette action:")

  for i in range(0, len(listFakeIDs)):
    extra_info=""
    if extra_param and extra_param in listFakeIDs[i]:
      extra_info = " (extra_param => "+listFakeIDs[i][extra_param]+")"

      if len(waited_param)>0:
        if listFakeIDs[i][extra_param]==waited_param:
          extra_info = bcolors.OKGREEN+extra_info+bcolors.ENDC
        else:
          extra_info = bcolors.FAIL+extra_info+bcolors.ENDC

    print("["+str(i+1)+"] "+listFakeIDs[i]['name']+" "+listFakeIDs[i]['lastname']+extra_info)
  choice = input("\n>> ")

  if len(choice)<1 or int(choice)>len(listFakeIDs):
    return choose_ID(listFakeIDs)
  else:
    clear_term()
    choice = int(choice)
    fakeID = listFakeIDs[choice-1]
    for key,value in fakeID.items():
      print(key + " => " + str(value))

    print("")
    if confirm_choice("Confirmer", "Choisir une autre ID"):
      return fakeID
    else:
      return choose_ID(listFakeIDs)

def clear_term():
  print("\033c")
