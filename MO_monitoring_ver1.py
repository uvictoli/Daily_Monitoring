# -*- coding: UTF-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests
from bs4 import BeautifulSoup as bs

mobile_emulation = { "deviceName": "iPhone X" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

main_driver = webdriver.Chrome(options=chrome_options)
checking_driver = webdriver.Chrome(options=chrome_options)


# 네이버 
naver_keywords = ['닥터릴리스', '인산가', '롯데스위트몰', '쉐푸드몰', '유라이크제모기', '롯데오토리스', '아모리스', '헤일로탑', '설화수', '유엔난민기구', ' 웰촌', ' 듀잇', '레페리', '찰스앤키스', '슈레피', '레오제이팩', '비너스', '솔브']

for keyword in naver_keywords:
  print(keyword)

  keyword_url = "https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query=" + keyword
  main_driver.get(keyword_url)
  page = requests.get(keyword_url).text
  html = bs(page, "html.parser")


  href = html.find("section", "sc sp_brand ad_light_mode").find_all('a')
  for i in href:
    link = i.get('href')
    checking_driver.get(link)
    time.sleep(0.5)



# 다음
daum_keywords = ['인산가', '설화수']

for keyword in daum_keywords:
  links = []

  keyword_url = "https://m.search.daum.net/search?w=tot&nil_mtopsearch=btn&DA=YZR&q=" + keyword
  main_driver.get(keyword_url)
  page = requests.get(keyword_url).text
  html = bs(page, "html.parser")



  href = html.find("div", id = "speBColl").find_all('a')
  for i in href:
    link = i.get('href')
    checking_driver.get(link)
    time.sleep(0.5)

main_driver.close()
checking_driver.close()
