import requests
import json
import re
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import datetime , time
import threading as td
import os

flag = False
def post(s , access_token):
    global flag
    date = str(datetime.date.today() + datetime.timedelta(days=6))
    payload ={'class_data': 'V5<6>K:;<=>?A=BF@EKCI' , 'date': date ,'branch_no': 'UA', 'access_token': access_token, 'session_time[]': ['2', '3']}
    while(True):
        content=s.post("https://bookseat.tkblearning.com.tw/book-seat/student/bookSeat/book",data=payload)
        if('預約成功' not in content.text):
            print("try")
            continue
        else:
            flag = True
            print(content.text)
            break

if __name__=='__main__':
    s = requests.Session()
    content = s.get('https://bookseat.tkblearning.com.tw/book-seat/student/bookSeat/index')
    cookie = {'JSESSIONID': content.cookies.get('JSESSIONID')}
    pos = content.text.find("name='access_token' type='hidden' value='")
    access_token = content.text[pos+41:pos+73]
    payload = {'access_token': access_token, 'toURL': '/student/bookSeat/index', 'id': '自行輸入自己的身分證', 'pwd': '自行輸入自己的密碼'}
    print(access_token)
    s.post('https://bookseat.tkblearning.com.tw/book-seat/student/login/login', data=payload, cookies=cookie)
    cookie={'JSESSIONID' : s.cookies.get('JSESSIONID')}
    content = s.get('https://bookseat.tkblearning.com.tw/book-seat/student/bookSeat/index')
    pos = content.text.find('type="hidden" id="access_token_id" value="')
    access_token = content.text[pos+42:pos+78]
    print(access_token)

    date = str(datetime.date.today() + datetime.timedelta(days=7))
    payload={'effectiveDate': '2019-12-31','class_data': 'V5<6>KLM;<=>@B=BF@EJCI','class_status': 'T'}
    s.post("https://bookseat.tkblearning.com.tw/book-seat/student/bookSeat/canBookseatDate",data=payload)
    payload={'date': date , 'branch_no': 'UA'}
    s.post("https://bookseat.tkblearning.com.tw/book-seat/student/bookSeat/sessionTime",data=payload)


    class_data_name=["線性代數","計組與計結","離散數學","資料結構","作業系統","演算法"]
    class_data=['V5<6:TJ:;<=>?A=BF@EHCI','V5<6>KLM;<=>@B=BF@EJCI','V5<6>KM:;<=>?A=BF@EGCI','V5<6>KM];<=>?A=BF@EICI','V5<6>K:;<=>?A=BF@EKCI','V5<77KL;<=>?B=BF@ELCI']
    driver = webdriver.Chrome()
    driver.get('https://www.timeanddate.com/worldclock/taiwan/taipei')
    while(True):
        if(driver.find_element_by_id('ct').text=='11:59:30'):
            break
    print("next way")
    thread = []
    for i in range(0, 5):
        thread.append(td.Thread(target=post,args=(s, access_token)))
    [p.start() for p in thread]
    while(flag == False):
        continue
    os._exit(1)