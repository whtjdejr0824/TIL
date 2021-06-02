import requests
from bs4 import BeautifulSoup

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    # 흐림, 어제보다 OO 높아요
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()
    # 현재 OOC (최저 OO / 최고 OO)
    curr_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨", "") #현재 온도
    min_temp = soup = soup.find("span", attrs={"class":"min"}).get_text # 최저 온도
    max_temp = soup.find("span", attrs={"class":"max"}).get_text # 최고 온도
    # 오전 강수확률 OO% / 오후 강수확률 OO%
    morning_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip() # 오전 강수확률
    afternoon_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip # 오후 강수확률

    # 미세먼지 OO좋음
    # 초미세먼지 OO 좋음
    dust = soup.find("dl", attrs={"class":"indicator"})
    pm10 = dust.find_all("dd")[0].get_text() # 미세먼지
    pm25 = dust.find_all("dd")[1].get_text() # 초미세먼지

    # 출력
    print(cast)
    print("현재 {} (최저 {} / 최고 {})".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate,afternoon_rain_rate))
    print()
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm10))
    print()

# [헤드라인 뉴스]
# 1. 무슨 무슨 일이...
#  (링크 : https://...)
# 2. 어떤 어떤 일이...
#  (링크 : https://...)
# 3. 이런 저런 일이...
#  (링크 : https://...)

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"headline_article_list"}).find_all("li")
    for index, news in enumerate(news_list):
        title = news.find("a").get_text.strip()
        link = url + news.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print("링크 : {})". format(link))
    print()



if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline_news()
