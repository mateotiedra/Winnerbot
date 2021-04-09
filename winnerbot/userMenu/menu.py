import os

from ._helper import *
from .. browser import Browser
from .. listIDs import ListIDs
from ._add_IDs import get_new_ID_data

class Menu(object):
  def __init__(self, originPath, absolutePathToDriver, relativePathToData):
    self.originPath = originPath
    self.pathToDriver = absolutePathToDriver
    self.pathToData = relativePathToData
    self.browser = Browser(self.pathToDriver, 10)
    self.list_IDs = ListIDs(os.path.join(originPath, self.pathToData))
    self.list_IDs.load_data()

  #importe modules
  
  def open(self):
    while True:
      clear_term()
      task = choose_between("Add emails", "Check the emails state", "New insta", "Quit")

      if task==1:
        self.add_IDs_menu()
      elif task == 2:
        self.check_IDs_menu()
      else:
        break
    print("Menu closed")

  def add_IDs_menu(self):
    clear_term()
    mustContinue = choose_between("New ID", "Existing ID", "Quit")
    clear_term()

    if mustContinue==1:
      #New ID
      print("Actives/change the vpn")
      if confirm_choice("Done", "Cancel"):
        clear_term()
        self.list_IDs.create_new(self.browser)
        input("\n>> ")

    elif mustContinue==2:
      #Existing ID
      new_ID = get_new_ID_data()
      self.list_IDs.add_existing(new_ID["name"], new_ID["lastname"], new_ID["email"], new_ID["emailPassword"])

    if mustContinue!=3:
      self.add_IDs_menu()

  def check_IDs_menu(self):
    clear_term()
    mustContinue = choose_between("Check one email state", "Quit")
    clear_term()

    if mustContinue==1:
      checked_ID = choose_ID(self.list_IDs.data_IDs, "emailState", "ok")
      clear_term()
      email_state = self.list_IDs.check_email(checked_ID["email"], self.browser)
      clear_term()
      if email_state == "ok" :
        print(checked_ID["email"]+" => \033[92mFonctionne correctement \033[0m\U0001F92A")
        input("\n>> ")
      else:
        if email_state == "ban":
          print(checked_ID["email"]+" => \033[91mBan par microsoft :(\033[0m")
        elif email_state == "wrongPassword":
          print(checked_ID["email"]+" => \033[91mMauvais mot de passe\033[0m")
        elif email_state == "wrongEmail":
          print(checked_ID["email"]+" => \033[91mMauvaise adresse email\033[0m")
        elif email_state == "proofNeeded":
          print(checked_ID["email"]+" => \033[91mA besoin de preuves\033[0m"+"\n")
        else:
          print(checked_ID["email"]+" => \033[91mProblème inconnu.\033[0m Url : " + email_state)

        if confirm_choice("Remove this ID", "Keep this ID") and confirm_choice("Confirm", "Cancel"):
          clear_term()
          print("The ID has been removed !")

    if mustContinue!=2:
      self.check_IDs_menu()