import requests
from bs4 import BeautifulSoup

url = "http://play.google.com/store/movies/top"
headers = {"User-Agent":Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit}

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

with open("movie.html", "w",encoding="utf-8") as f:
    # f.write(res.text)
    f.write(soup.prettify()) # html 문서를 예쁘게 출력
