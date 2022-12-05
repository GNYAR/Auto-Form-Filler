from os import getcwd
from time import sleep
from selenium import webdriver

# driver setup
options = webdriver.EdgeOptions()
pre = {
  "profile.default_content_settings.popups": 0,
  "download.default_directory": getcwd()
}
options.add_experimental_option("prefs", pre)
driver = webdriver.Edge(options = options)

url = "https://ais.ntou.edu.tw/"

print("Open website.")
driver.get(url)
sleep(10)
print("Done.\n")
