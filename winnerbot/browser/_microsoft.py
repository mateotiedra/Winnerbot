import random
from time import sleep
from .browser import *

def outlook_sign_up(self, name, last_name, birth_year):
  new_ID = {
    "name": name,
    "lastname":last_name,
    "birthYear":birth_year,
    "emailBox": random.choice(["hotmail", "outlook"]),
    "emailPassword": "Jeb0tttt_",
  }
  user_name = new_ID["name"].lower()+"."+new_ID["lastname"].lower()+str(new_ID["birthYear"])

  #go to the signup page
  sign_up_webscript = WebScript()
  self.log_driver("https://outlook.live.com/")
  self.run_web_script(sign_up_webscript.new_steps([
    ["xpath", "//*[text()='Create free account']", "click"],
    ["id", "LiveDomainBoxList", "select", new_ID["emailBox"]+".com"],
    ["id", "MemberName", "fill", user_name, True],
  ]))

  while not ("has-error" in self.get_webelement_class("id", "MemberName")) and not self.find_webelement("id", "PasswordInput", 0):
    sleep(0.5)

  if "has-error" in self.get_webelement_class("id", "MemberName"):
    self.run_web_script(sign_up_webscript.new_steps([["id", "suggLink", "click"]]))
    new_ID["email"] = self.get_webelement_value("xpath", "//*[@id='Suggestions']/div[1]/a")
    self.run_web_script(sign_up_webscript.new_steps([
      ["xpath", "//*[@id='Suggestions']/div[1]/a", "click"],
      ["id", "iSignupAction", "click"],
    ]))
  else :
    new_ID["email"] = user_name+"@"+new_ID["emailBox"]+".com"
  
  #script from the password to the kaptcha
  self.run_web_script(sign_up_webscript.new_steps([
    ["id", "PasswordInput", "fill", new_ID["emailPassword"], True],
    ["id", "FirstName", "fill", new_ID["name"], True],
    ["id", "LastName", "fill", new_ID["lastname"], True],
    ["id", "Country", "select", "Switzerland"],
    ["id", "BirthMonth", "select", random.randint(0, 11)],
    ["id", "BirthDay", "select", random.randint(0, 27)],
    ["id", "BirthYear", "fill", new_ID["birthYear"], False],
    ["id", "iSignupAction", "click"],
  ]))

  self.wait_page("inbox", sign_up_webscript)
  self.close_outlook_inbox_alerts()
  
  if sign_up_webscript.running:
    return new_ID
  return False
  
def close_outlook_inbox_alerts(self):
  if self.driver.current_url != "https://outlook.live.com/mail/0/inbox":
    self.driver.get("https://outlook.live.com/mail/0/inbox")
  
  self.run_web_script(WebScript(10).new_steps([["xpath", "/html/body/div[7]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/span[3]/button", "click"]]))
  self.run_web_script(WebScript(1).new_steps([["xpath", "/html/body/div[5]/div/div/div/div[3]/div/div[2]/button", "click"]]))

def outlook_sign_in(self, email, email_password):
  """Sign in the given email with the given password and return the state of this email"""
  sign_in_webscript = WebScript()
  self.log_driver("https://outlook.live.com/")
  self.run_web_script(sign_in_webscript.new_steps([
    ["xpath", "/html/body/header/div/asIDe/div/nav/ul/li[2]/a", "click"],
    ["xpath", "//input[@placeholder='Email, phone, or Skype']", "fill", email, True],
    ["xpath", "//input[@placeholder='Password']", "fill", email_password, True],
  ]))

  print("Checking state...")
  current_url = self.driver.current_url

  if "Abuse" in current_url :
    return "ban"
  elif "ppsecure" in current_url :
    return "wrongPassword"
  elif "proofs" in current_url :
    return "proofNeeded"
  elif "mail" in current_url:
    return "ok"
  else:
    return current_url