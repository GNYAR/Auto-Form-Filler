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
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Edge(options = options)

# functions
def courseEvaluationSurvey():
  chageMainFrame("Application/CET/CET20/CET2010_.aspx?progcd=CET2010")
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

def courseSelectionDrawing():
  chageMainFrame("Application/TKE/TKE20/TKE2020_.aspx?progcd=STU1020")
  sleep(3) # wait for alert
  driver.switch_to.alert.accept()
  driver.switch_to.frame("mainFrame")

  # show all rows
  total = driver.find_element(By.ID, "PC_TotalRow").text
  driver.find_element(By.ID, "PC_PageSize").send_keys(total)
  driver.find_element(By.ID, "PC_ShowRows").click()

  sleep(3) # wait for change

  reorderColumn = "籤號"
  count = len(driver.find_elements(By.XPATH, "//td[text()='尚未抽籤']"))
  for _ in range(count):
    # reorder
    driver.find_element(By.PARTIAL_LINK_TEXT, reorderColumn).click()
    driver.find_element(By.PARTIAL_LINK_TEXT, reorderColumn).click()
    # select course
    driver.find_element(By.LINK_TEXT, "詳").click() 
    sleep(10) # wait for change
    # do lot
    driver.find_element(By.ID, "DoLot_BTN").click()
    sleep(10) # wait for change

def chageMainFrame(href):
  mainFrame = driver.find_element(By.NAME, "mainFrame")
  driver.execute_script("arguments[0].src='{0}'".format(href), mainFrame)

def printFuncMenu(funcs):
  printHeader("Function Menu")
  for i in funcs:
    print(str(i["id"]) + ".  " + i["text"])
  print("\n0.  Exit")
  return int(input("\nWhich to do? (Enter the number)"))

def printHeader(str):
  n = 32
  l = int((n - 2 - len(str)) / 2)
  r = n - 2 - l - len(str)
  print()
  print("=" * n)
  print("=", " " * l, str, " " * r, "=", sep="")
  print("=" * n)

# variables
url = "https://ais.ntou.edu.tw"

# open website
driver.get(url)

# login
printHeader("Login")
fields = {
  "M_PORTAL_LOGIN_ACNT": "",
  "M_PW": "",
  "M_PW2": ""
}
while(True):
  fields["M_PORTAL_LOGIN_ACNT"] = input("Account: ")
  fields["M_PW"] = getpass()
  fields["M_PW2"] = input("Captcha: ")
  for i in fields:
    driver.find_element(By.NAME, i).clear()
    driver.find_element(By.NAME, i).send_keys(fields[i])
  print("\nLogin...", end="\r")
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
  },
  {
    "id": 2,
    "text": "Course Selection Drawing",
    "func": courseSelectionDrawing
  }
]
selected = printFuncMenu(funcs)
while(selected != 0):
  filtered = [x for x in funcs if x["id"] == selected][0]
  if len(filtered):
    printHeader(filtered["text"])
    filtered["func"]()
    print("\nDone! Please check.\n")
    printFuncMenu(funcs)
  else:
    print("\nBad input.\n")
    printFuncMenu(funcs)
