import names

import random
import datetime

def add_existing(self, name, lastname, email, emailPassword):
  """Add a new ID to the list and save it"""
  self.data.append({})
  self.data[-1]["name"] = name
  self.data[-1]["lastname"] = lastname
  self.data[-1]["email"] = email

  if self.data[-1]["email"] != self.data[-1]["email"].replace('@hotmail.com', ''):
    self.data[-1]["emailBox"] = "hotmail"
  elif self.data[-1]["email"] != self.data[-1]["email"].replace('@outlook.com', ''):
    self.data[-1]["emailBox"] = "outlook"
  elif self.data[-1]["email"] != self.data[-1]["email"].replace('@gmail.com', ''):
    self.data[-1]["emailBox"] = "gmail"
  else :
    self.data[-1]["emailBox"] = "other"

  self.data[-1]["emailPassword"] = emailPassword

  self.save_data()

def create_new(self, browser):
  name = names.get_first_name()
  lastName = names.get_last_name()
  birthYear =  datetime.datetime.today().year - random.randint(18,30)

  new_ID = browser.outlook_sign_up(name, lastName, birthYear)
  if new_ID:
    add_existing(self, new_ID["name"], new_ID["lastname"], new_ID["email"], new_ID["emailPassword"])
  #browser.close()