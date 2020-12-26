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


url="https://www.netflix.com/kr/login"
browser.get(url)
#######여기에 ID랑 Password만 입력해서 python 돌릴수 있는 tool에서 돌리면 됨
browser.find_element_by_id("id_userLoginId").send_keys("Your Email")
browser.find_element_by_id("id_password").send_keys("Your password")
#################라이브러리 설치 필요
browser.find_element_by_xpath("//*[@id='appMountPoint']/div/div[3]/div/div/div[1]/form/button").click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a/div/div').click()
browser.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div/ul/li[4]/a').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()
browser.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div').click()
browser.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/ul/li[4]/a').click()
interval=1
#현재문서 높이를 가져와서 저장
prev_height=browser.execute_script("return document.body.scrollHeight")
time.sleep(1)
#반복
while True:
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(interval)
    current_height=browser.execute_script("return document.body.scrollHeight")
    if current_height==prev_height:
        break
    else:
        prev_height=current_height

print("스크롤 끝")

soup=BeautifulSoup(browser.page_source,"lxml")
movies=soup.find_all("div",attrs={'class':"ptrack-content"})
del movies[0]
print(len(movies))
print(movies[0])
filename='netflixmovietitleg ㅎ~.txt'
f=open(filename,"w", encoding="utf8")
for movie in movies:
    
    title=movie.find('a',attrs={'class':'slider-refocus'})['aria-label']
    if title:
        print(title)
        f.write(str(title))
        f.write('\n')
    else:
        continue