#======================================================================================
#引入==================================================================================

from sys import argv
#取得檔案位置、刪除檔案
from os import getcwd, remove, system
#檔案是否重複
from os.path import isfile
#webdirvar
from selenium import webdriver
#開啟外部程式
from subprocess import check_output
#等待
from time import sleep

#====================================================================================
#瀏覽器(下載)設定======================================================================

#自定值
options = webdriver.ChromeOptions()
pre = {"profile.default_content_settings.popups":0, "download.default_directory":getcwd()}
#引入自定值
options.add_experimental_option("prefs", pre)
#開啟使用自訂值瀏覽器
driver = webdriver.Chrome(chrome_options = options)

#======================================================================================
#自動登入==============================================================================
def Login():
    print("\n========自動登入========\n")
    print("開啟網頁...",end="")
    driver.get("http://sso.nutc.edu.tw")
    print("完成")
    stu, pw = argv[1], argv[2]
    #填學號
    driver.find_element_by_name("ctl00$ContentPlaceHolder1$Account").send_keys(stu)
    #驗證碼錯誤，密碼、驗證碼重填
    while(1):
        print("填入資料...",end="")
        #填密碼
        driver.find_element_by_name("ctl00$ContentPlaceHolder1$Password").send_keys(pw)
        print("完成")
        #驗證碼清空
        driver.find_element_by_name("ctl00$ContentPlaceHolder1$ValidationCode").clear()
        #確認驗證碼圖檔是否重複
        if(isfile("VCode.jpg")):
            remove("VCode.jpg")
        #下載圖檔
        driver.get("https://sso.nutc.edu.tw/ePortal/Validation_Code.aspx")
        #開啟外部，破解驗證碼程式，回傳值編碼utf-8
        print("破解驗證碼...\n")
        txt = check_output("crack_captcha.exe").decode("utf-8")
        #填驗證碼
        driver.find_element_by_name("ctl00$ContentPlaceHolder1$ValidationCode").send_keys(txt)
        #按下登入
        driver.find_element_by_name("ctl00$ContentPlaceHolder1$Login").click()
        try:
            #驗證碼警告視窗，確定
            driver.switch_to.alert.accept()
            print("\n重新破解...")
        except:
            print("\n========登入成功========\n")
            break
    return 0

#======================================================================================
#自動評量===============================================================================
def Tch_qa():
    print("\n========自動評量========\n")
    print("開啟教學評量...",end="")
    #學生管理系統
    driver.find_element_by_link_text("學生管理系統").click()
    #轉移控制網頁
    driver.switch_to_window(driver.window_handles[1])
    #主選單
    try:
        driver.find_element_by_id("showLeftPush").click()
    except:
        #清除通知(重開)
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_link_text("學生管理系統").click()
        driver.switch_to_window(driver.window_handles[1])
        driver.find_element_by_id("showLeftPush").click()
    #等待選單開啟
    sleep(1)
    #點入評鑑
    driver.find_element_by_xpath('//a[@href="/student/courses/my_week_time.aspx	"]').click()
    try:
        #期末評鑑
        driver.find_element_by_xpath('//a[@href="/student/tch_qa/assess_list.aspx"]').click()
    except:
        #期中評鑑
        driver.find_element_by_xpath('//a[@href="/student/tch_qa/assess_list_fm.aspx"]').click()
    print("完成")
    #進行評量
    while(1):
        try:
            #打開評量
            driver.find_element_by_xpath('//a[@data-hasqtip="1"]').click()
            print("填寫評鑑...",end="")
            #計算題數
            checkbox = driver.find_elements_by_xpath('//input[@type="checkbox"]')
            radio = driver.find_elements_by_xpath('//input[@type="radio"]')
            checkbox_num = len(checkbox) // 4
            radio_num = len(radio) // 5
            #填寫評量
            for i in range(1, checkbox_num + radio_num + 1):
                driver.find_element_by_name("ans" + str(i)).click()
            print("送出")
            driver.find_element_by_xpath('//a[@onclick="submit_data();"]').click()
            #等待方塊跳出
            sleep(1)
            driver.switch_to.alert.accept()
        except:
            print("\n========評鑑完成========")
            break
    return 0
#======================================================================================
#主程式=================================================================================
system("echo START")
Login()
Tch_qa()
driver.close()
driver.switch_to_window(driver.window_handles[0])
driver.close()