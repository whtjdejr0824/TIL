#Quiz) 부동산 매물(송파 헬라오시티) 정보를 스크래핑 하는 프로그램을 만드시오

#[조회 조선]
# 1. http://daum.net 접속
# 2. '송파 헬리오시티'검색
# 3. 다음 부동산 부분에 나오는 결과 정보

# [출력 결과]
# ===== 매물 1 =======
# 거래 : 매매
# 면적 : 84/59 (공급/전용)
# 가격 : 165,000 (만원)
# 동 : 214동
# 총 : 고/23

# ========= 매물 2 =========
#       ....

# [주의 사항]
# - 실습하는 시점에 위 매물이 없다면 다른 곳으로 대체 가능

import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%EC%EC+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

with open("quiz.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())
