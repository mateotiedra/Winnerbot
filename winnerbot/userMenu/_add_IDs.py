from ._helper import *

def get_new_ID_data():
  new_ID = {
    "name": input("Name : ").lower().capitalize(),
    "lastname": input("Lastname : ").lower().capitalize(),
    "email": input("Email : ").lower(),
    "emailPassword": input("Mot de passe de l'email : ")
  }

  if new_ID["email"] != new_ID["email"].replace('@hotmail.com', ''):
    new_ID["emailBox"] = "hotmail"
  elif new_ID["email"] != new_ID["email"].replace('@outlook.com', ''):
    new_ID["emailBox"] = "outlook"
  elif new_ID["email"] != new_ID["email"].replace('@gmail.com', ''):
    new_ID["emailBox"] = "gmail"
  else :
    new_ID["emailBox"] = "\033[91mEmail box not found !\033[0m"

  clearTerm()
  for key,value in new_ID.items():
    print(key + " => " + value)
  print("")

  if confirmChoice("Save", "Cancel") :
    clearTerm()
    return new_ID
  else:
    clearTerm()
    return get_new_ID_data()
