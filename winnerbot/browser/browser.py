from time import sleep

from ._driver_helper import WebScript

class Browser:
  def __init__(self, path_to_driver, waiting_time=10):
    self.path_to_driver = path_to_driver
    self.waiting_time = waiting_time
    self.running_scripts = False

  from ._microsoft import outlook_sign_up, outlook_sign_in, close_outlook_inbox_alerts
  from ._driver_helper import log_driver, close, find_webelement, click_on_elem, fill_field, select_option, get_webelement_class, get_webelement_value

  def wait_page(self, word_in_url, web_script=False):
    if not (web_script and not web_script.running):
      while not word_in_url in self.driver.current_url:
        sleep(0.5)
  
  def wait_next_page(self, word_in_url, max_time, web_script=False):
    if not (web_script and not web_script.running):
      print("Waiting next page..")
      time_waited = 0
      while word_in_url in self.driver.current_url and time_waited<max_time:
        sleep(0.1)
        time_waited += 0.1
  
  def run_web_script(self, web_script, waiting_time=-1):
    if type(web_script) == tuple:
      waiting_time = web_script[1]
      web_script = web_script[0]
    
    script_state = "success"

    for web_step in web_script:
      method = web_step[0]
      path = web_step[1]
      action = web_step[2]

      step_state = "action unknown : "+action
      if action == "click":
        step_state = self.click_on_elem(method, path, waiting_time)
      elif action == "fill":
        step_state = self.fill_field(method, path, web_step[3], web_step[4], waiting_time)
      elif action == "select":
        step_state = self.select_option(method, path, web_step[3], waiting_time)
      
      if step_state!="success":
        script_state = step_state
        break

    if script_state == "success":
      print("\033[92mScript well executed \033[0m\U0001F92A")
      return True
    else:
      print("\033[91mScript failed \033[0m:")
      print("\t"+script_state)
      return False
