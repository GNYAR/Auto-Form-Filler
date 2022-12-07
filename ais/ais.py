from getpass import getpass
from os import getcwd, system
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# driver setup
options = webdriver.EdgeOptions()
pre = {
  "profile.default_content_settings.popups": 0,
  "download.default_directory": getcwd()
}
options.add_experimental_option("prefs", pre)
driver = webdriver.Edge(options = options)

# functions
def courseEvaluationSurvey():
  goToNode(["Menu_TreeViewt1", "Menu_TreeViewt28", "Menu_TreeViewt39"])
  # loop
  while(True):
    try:
      # select a form
      driver.switch_to.frame("mainFrame")
      driver.find_element(By.XPATH, "//td[@onclick]//a[@href='#this']").click()
      driver.switch_to.default_content()

      sleep(3) # wait for page change

      # auto filler
      driver.switch_to.frame("viewFrame")
      radio = driver.find_elements(By.XPATH, "//input[@type='radio']")
      for i in range(len(radio) // 5): # 5 options for each question
        radio[i * 5 + 2].click() # select the middle one
      driver.find_element(By.NAME, "SAVE_BTN2").click()
      sleep(1) # wait for alert
      driver.switch_to.alert.accept()
      sleep(1) # wait for alert
      driver.switch_to.alert.accept()
      driver.switch_to.default_content()
    except:
      break

def funcMenu(funcs):
  print("Function Menu")
  for i in funcs:
    print(str(i["id"]) + ".  " + i["text"])
  print("\n0.  Exit")
  return int(input("Enter the number: "))

def goToNode(path):
  driver.switch_to.frame("menuFrame")
  for i in path:
    driver.find_element(By.ID, i).click()
    sleep(1) # wait for animation
  driver.switch_to.default_content()

# variables
url = "https://ais.ntou.edu.tw"

# open website
driver.get(url)

# login
print("Login")
fields = {
  "M_PORTAL_LOGIN_ACNT": "",
  "M_PW": "",
  "M_PW2": ""
}
while(True):
  fields["M_PORTAL_LOGIN_ACNT"] = input("Account: ")
  fields["M_PW"] = getpass()
  fields["M_PW2"] = input("Check: ")
  for i in fields:
    driver.find_element(By.NAME, i).clear()
    driver.find_element(By.NAME, i).send_keys(fields[i])
  driver.find_element(By.NAME, "LGOIN_BTN").click()
  try:
    driver.switch_to.alert.accept()
    print("Wrong user input. Please retry\n")
  except:
    break
print("Login successfully.\n")

# function menu
funcs = [
  {
    "id": 1,
    "text": "Course Evaluation Survey",
    "func": courseEvaluationSurvey
  }
]
selected = funcMenu(funcs)
while(selected != 0):
  filtered = [x for x in funcs if x["id"] == selected]
  if len(filtered):
    print("\nStart the function.")
    filtered[0]["func"]()
    print("Done! Please check.")
    break
  else:
    print("Bad input.\n")
    funcMenu(funcs)

system("pause")
