import json

class ListIDs(object):
  def __init__(self, pathToData):
    self.pathToData = pathToData
    self.data_IDs = []

  from ._add_IDs import add_existing, create_new

  def load_data(self):
    with open(self.pathToData, 'r') as f:
      self.data_IDs = json.loads(f.read())
  
  def save_data(self):
    with open(self.pathToData, 'w') as f:
      f.write(json.dumps(self.data_IDs))
  
  def get_ID_from_email(self, email):
    for ID in self.data_IDs:
      if email==ID["email"]:
        return ID

  def check_email(self, email, browser):
    """Check the state of the given email and save it in the data_IDs"""
    checked_ID = self.get_ID_from_email(email)
    
    checked_ID["emailState"] = browser.outlook_sign_in(checked_ID["email"], checked_ID["emailPassword"])
    browser.driver.quit()
    self.save_data()

    return checked_ID["emailState"]
  
  def delete_email(self, email):
    removed_ID = self.get_ID_from_email(email)
    self.data_IDs.remove(removed_ID)