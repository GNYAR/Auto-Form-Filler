# Auto-Form-Filler

## Environment

- Python
- Selenium
- Webdriver
  ( [Edge](https://developer.microsoft.com/zh-tw/microsoft-edge/tools/webdriver/) |
  [Chrome](https://chromedriver.chromium.org/downloads) )

| Program Name   | Python | Selenium | Browser |
| -------------- | ------ | -------- | ------- |
| ePortal (NUTC) | 3.7    | ?        | Chrome  |
| ais (NTOU)     | 3.11   | 4.7.2    | Edge    |

## Build

Check the program can be executed as expected first.

```
> pip install pyinstaller
> pyinstaller -F <PROGRAM.py> -i <IMG.ico>
```

# ais - NTOU

## Execute

1. Put the [Edge webdriver](https://developer.microsoft.com/zh-tw/microsoft-edge/tools/webdriver/) in the same directory as the program
2. `python <PROGRAM.py>`

> **IMPORTANT** | Need to input the login fields form the terminal.

# ePortal - NUTC

## Coding

Old version (used in `ePortal.py`)

```
# Import
from selensium import webdriver

# Webdriver setup
driver = webdriver.Chrome(chrome_options = options)

# Open website
driver.get("URL")

# Find element
driver.find_element_by_HTML屬性("屬性值").方法()

find_element_by_id() #用id屬性尋找
find_element_by_name() #用name屬性尋找
find_element_by_xpath() #用xpath語法尋找區塊
find_element_by_link_text() #尋找超連結文字區塊
find_element_by_partial_link_text() #和上面類似，比較少用
find_element_by_tag_name() #以標籤名稱尋找區塊(table、div)
find_element_by_class_name() #用class屬性尋找
find_element_by_css_selector() #用css語法尋找區塊

# Actions
.click() #點擊
.send_keys("字串") #填入文字
.clear() #清除文字

# Alert
driver.switch_to.alert.accept() #確定

# Switch tab
driver.switch_to_window(driver.window_handles[註標值]) #註標值從0開始
```

---

## References

- [社團上課講義](https://hackmd.io/@5Tx96k0MTs6LBwHSE3bmHQ/SkmpHiwDr)
- [Selenium Webdriver](https://www.selenium.dev/documentation/webdriver/)
