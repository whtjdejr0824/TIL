import requests
from bs4 import BeautifulSoup
# [오늘의 날씨]
# 흐림, 어제보다 OO 높아요
# 현재 OOC (최저 OO / 최고 OO)
# 오전 강수확률 OO% / 오후 강수확률 OO%

# 미세먼지 OO좋음
# 초미세먼지 OO 좋음

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    # 흐림, 어제보다 00 높아요.
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()
    # 현재 OOC (최저 OO / 최고 OO)
    curr_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨", "")
    min_temp = None
    max_temp = None

if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기
