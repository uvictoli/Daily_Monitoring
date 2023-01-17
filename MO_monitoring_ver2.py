import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

import multiprocessing


def set_chrome_driver():
    mobile_emulation = { "deviceName": "iPhone X" }
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def naver_get_links(keyword):
    print("get links from ", keyword)
    keyword_url = "https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query=" + keyword
    page = requests.get(keyword_url).text
    html = bs(page, "html.parser")
    href = html.find("section", "sc sp_brand ad_light_mode").find_all('a')

    links_list = []
    for i in href:
        link = i.get('href')
        links_list.append(link)
    return keyword_url, links_list

def daum_get_links(keyword):
    print("get links from ", keyword)
    keyword_url = "https://m.search.daum.net/search?w=tot&nil_mtopsearch=btn&DA=YZR&q=" + keyword
    page = requests.get(keyword_url).text
    html = bs(page, "html.parser")
    href = html.find("div", id = "speBColl").find_all('a')
        
    links_list = []
    for i in href:
        link = i.get('href')
        links_list.append(link)
    return keyword_url, links_list

def naver_monitoring(brand):
    try:
        main_url, links = naver_get_links(brand)
        main = set_chrome_driver()
        main.get(main_url)

        driver = set_chrome_driver()
        for url in links:
            driver.get(url)
            time.sleep(0.3)
        driver.close()
        main.close()
        print(brand, " check")
    except AttributeError:
        pass
        

def daum_monitoring(brand):
    main_url, links = daum_get_links(brand)
    main = set_chrome_driver()
    main.get(main_url)

    driver = set_chrome_driver()
    for url in links:
        driver.get(url)
        time.sleep(0.3)
    driver.close()
    main.close()
    print(brand, " check")


# main
if __name__ == "__main__":
    start_time = time.time()
    naver_keywords = ['닥터릴리스', '인산가', '롯데스위트몰', '쉐푸드', '유라이크제모기', '롯데오토리스', '아모리스', '헤일로탑', '설화수', '유엔난민기구', '웰촌', '듀잇', '레페리', '찰스앤키스', '슈레피', '레오제이팩', '비너스', '솔브']
    daum_keywords = ['인산가', '설화수']
        
    cpu_count = multiprocessing.cpu_count() 
    
    for i in range(0, len(naver_keywords), cpu_count):
        pool = multiprocessing.Pool(processes = cpu_count)
        brand = naver_keywords[i:i + cpu_count]
        pool.map(naver_monitoring, brand)
        pool.close()
        pool.join()
    

    for i in range(0, len(daum_keywords), cpu_count):
        pool = multiprocessing.Pool(processes = cpu_count)
        brand = daum_keywords[i:i + cpu_count]
        pool.map(daum_monitoring, brand)
        pool.close()
        pool.join()

    print(f"--- {time.time() - start_time} seconds ---")
# --- 843.3965482711792 seconds ---
