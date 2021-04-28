from selenium import webdriver

options = webdriver.ChromeOptions()
options.headers =True
options.add_argument("window-size=1920x1000")

browser = webdriver.Chrome(options=options)
browser.maximize_window() 

# 페이지 이동
# url = "http://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scroollTo(0, 1080)") # 1920 x 1080
# browser.execute_script("window.scroollTo(0, 2080)") # 1920 x 1080

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scroollTo(0, document.body.scrolHeight)") # 1920 x 1080

import time
interval =  2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scroollTo(0, document.body.scrolHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 스크롤을 가장 아래로 내림
    curr_height = browser.execute_script("window.scroollTo(0, document.body.scrolHeight)")
    if curr_height == prev_height:
        break

    prev_height = curr_height
    
print("스크롤 완료")


import requests
from bs4 import BeautifulSoup

# url = "http://play.google.com/store/movies/top"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit",
#     "Accept-Language":"ko-KR,ko"
#     }

# res = requests.get(url)
# res.raise_for_status()
soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

#with open("movie.html", "w",encoding="utf-8") as f:
    # f.write(res.text)
 #   f.write(soup.prettify()) # html 문서를 예쁘게 출력

 for movie in movies:
     title = movie.find("div", attrs={"class":"WsMGlc nnK0zc"}).get_text()
     print(title)

    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        print(title, " <할인되지 않은 영화 제외>")
        continue

    # 할인 된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"})

    # 링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    # 올바른 링크 : https://play.google.com + link

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print(f"링크 : ", "https://play.google.com" + link)
    print("-" * 120)

browser.quit()
