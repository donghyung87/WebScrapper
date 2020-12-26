from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import re
from bs4 import BeautifulSoup
import csv
import time

browser = webdriver.Chrome("D:/python_practice/wbscraping_basic/chromedriver.exe")

url="https://play.watcha.net/sign_in"
browser.get(url)
########여기에 ID랑 Password만 입력해서 python 돌릴수 있는 tool에서 돌리면 됨
browser.find_element_by_name("email").send_keys("Your email")
browser.find_element_by_name("password").send_keys("Your password")
##################라이브러리 설치 필요
browser.find_element_by_xpath('//*[@id="root"]/div[1]/main/div/main/div/form/div[3]/button').click()
time.sleep(3)
browser.find_element_by_xpath("//*[@id='root']/div[1]/main/div/section/ul/li[1]/button").click()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="root"]/div[1]/nav/ul[1]/li[2]/div/div/div/a').click()

#time.sleep(3)
#browser.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()
#

interval=2
#현재문서 높이를 가져와서 저장
prev_height=browser.execute_script("return document.body.scrollHeight")

#
# 반복
while True:
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(interval)
    current_height=browser.execute_script("return document.body.scrollHeight")
    if current_height==prev_height:
        break
    else:
        prev_height=current_height

print("스크롤 끝")
time.sleep(2)
soup=BeautifulSoup(browser.page_source,"lxml")
movies=soup.find_all("li",attrs={'class':"css-1aw5v0q-RowItem e17mfvby2"})
#del movies[0]
print(len(movies))
#print(movies[0])
filename='watcha_original.txt'
f=open(filename,"w", encoding="utf8")
for movie in movies:
    
    title=movie.find('div',attrs={'css-1cplejl-Text el11hez1'}).get_text()
    if title:
        print(title)
        f.write(str(title))
        f.write('\n')
    else:
        continue