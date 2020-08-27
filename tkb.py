from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from http import cookiejar
from urllib import request
import datetime , time
from PIL import ImageGrab

def choosesubject():
    subject=['線性代數','計算機組織','離散數學','資料結構','作業系統','演算法']
    classnum = -1
    while(classnum<1 or classnum>6):
        choice = input("請問你要選哪一堂課\n1.線性代數\n2.計算機組織\n3.離散數學\n4.資料結構\n5.作業系統\n6.演算法\n")
        if choice.isdigit() and 0<int(choice)<7:
            classnum = int(choice)
            print("課程為:"+subject[classnum-1])
        else:
            print("Error")
    return '//*[@id="class_selector"]/option['+str(int(classnum)+1)+']'
def choosedate():
    learnday = -1
    while(learnday<1 or learnday>7):
        for i in range(7):
            print(str(i+1)+". "+str(datetime.date.today() + datetime.timedelta(days=i)))
        choice = input("請輸入1~7: ")
        if choice.isdigit() and 0<int(choice)<8:
            learnday=int(choice)
            print("預定時間為:"+str(datetime.date.today() + datetime.timedelta(days=learnday-1)))
        else:
            print("Error")
    return '//*[@id="date_selector"]/option['+str(learnday+1)+']'
def chooseplace():
    place=['中壢數位學堂','中央數位學堂','高大數位學堂']
    learnplace=-1
    while(learnplace<1 or learnplace>3):
        choice = input("請問要選哪個教室\n"+'1.中壢數位學堂\n2.中央數位學堂\n3.高大數位學堂\n')
        if choice.isdigit() and 0<int(choice)<4:
            learnplace = int(choice)
            print("教室為:"+place[learnplace-1])
        else:
            print("Error")
    return place[learnplace-1]
def screenshot():
    im = ImageGrab.grab()
    im.save('screenshot.png')
def autoreserved(subject , date , classroom):
    url = "https://bookseat.tkblearning.com.tw/book-seat/student/login"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element_by_name("id").send_keys("S124925420")
    driver.find_element_by_name("pwd").send_keys("Tony2468@")
    driver.find_element_by_class_name("login_btn").submit()
    driver.switch_to_alert().accept()
    time.sleep(5)
    driver.find_element_by_xpath(subject).click()
    driver.find_element_by_xpath(date).click()
    Select(driver.find_element_by_id("branch_selector")).select_by_visible_text(classroom)
    sleep(10)
    #Select(driver.find_element_by_id("class_selector")).select_by_visible_text("線性代數(黃子嘉)-->2078/分鐘   有效日期:2019-12-31")

#driver.find_element_by_xpath(classchoice).click()
#Select(driver.find_element_by_id("date_selector")).select_by_index(6)
#Select(driver.find_element_by_id("branch_selector")).select_by_visible_text("中壢數位學堂")
#driver.find_element_by_xpath('//input[@value="2"]').click()
#driver.find_element_by_xpath('//input[@value="3"]').click()
#driver.find_element_by_class_name("btn").click()
#driver.switch_to_alert().accept()
#driver.switch_to_alert().dismiss()
#sleep(50)

if __name__ == '__main__':
    subject_xpath= choosesubject()
    date_xpath = choosedate()
    classroom = chooseplace()
    autoreserved(subject_xpath , date_xpath , classroom)