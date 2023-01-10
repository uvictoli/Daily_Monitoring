# -*- coding: UTF-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests
from bs4 import BeautifulSoup as bs
 
main_driver = webdriver.Chrome('./chromedriver.exe')
checking_driver = webdriver.Chrome('./chromedriver.exe')



# 네이버
naver_keywords = ['기프티엘비즈', '인산가', ' 롯데스위트몰', '롯데쉐푸드', '유라이크제모기', '롯데오토리스', '아모리스', '설화수', '유엔난민기구', '웰촌', '듀잇', '레페리', '찰스앤키스', '슈레피', '비너스', '솔브']

for keyword in naver_keywords:
  print(keyword)
  
  keyword_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=" + keyword
  main_driver.get(keyword_url)
  page = requests.get(keyword_url).text
  html = bs(page, "html.parser")


  href = html.find("div", "brand_search section brand_new_ui").find_all('a')
  for i in href:
    link = i.get('href')
    checking_driver.get(link)
    time.sleep(1)



# 다음
daum_keywords = ['인산가', '설화수']

for keyword in daum_keywords:
  links = []

  keyword_url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=" + keyword
  main_driver.get(keyword_url)
  page = requests.get(keyword_url).text
  html = bs(page, "html.parser")



  href = html.find("div", id = "speBrandColl").find_all('a')
  for i in href:
    link = i.get('href')
    checking_driver.get(link)
    time.sleep(1)

main_driver.close()
checking_driver.close()
