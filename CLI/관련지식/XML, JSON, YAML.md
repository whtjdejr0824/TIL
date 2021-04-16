# XML, JSON, YAML이 뭔가요?

영상에 나온 XML, JSON, YAML 예제들을
아래에서 보다 자세히 확인하세요!

## XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<shop>
    <name>돌준이네 치킨</name>
    <location>닭볶로 12번길</location>
    <!-- 가게 주인 정보 -->
    <owner>
        <name>장돌준</name>
        <age>44</age>
        <major>컴퓨터공학</major>
        <career>
            <job>앱 개발자</job>
            <job>풀스택 개발자</job>
            <job>SI 개발자</job>
        </career>
    </owner>
    <menus>
        <menu>
            <name>자바치킨</name>
            <price>18000</price>
            <ingredients>
                <ingredient>닭</ingredient>
                <ingredient>튀김가루</ingredient>
                <ingredient>자바소스</ingredient>
            </ingredients>
        </menu>
        <menu>
            <name>깃윙</name>
            <price>6500</price>
            <ingredients>
                <ingredient>닭날개</ingredient>
                <ingredient>문어다리</ingredient>
            </ingredients>
        </menu>
        <menu>
            <name>스프링소다</name>
            <price>2000</price>
            <ingredients>
                <ingredient>물</ingredient>
                <ingredient>사카린</ingredient>
                <ingredient>메탄가스</ingredient>
            </ingredients>
        </menu>   
    </menus>
    <reviews>
        <review>
            <reviewer>
                <name>배다른민족</name>
                <level>Beginner</level>
            </reviewer>
            <rating>5</rating>
            <comment>아니 음료수 뭐냐고</comment>
        </review>
        <review>
            <reviewer>
                <level>VIP</level>
                <name>김밥순</name>
            </reviewer>
            <rating>5</rating>
            <comment>개발팀장님 힘내세요. 많이 시켜먹을게요.</comment>
        </review>
    </reviews>
</shop>
```

----

## JSON

```json
{
  "name": "돌준이네 치킨",
  "location": "닭볶로 12번길",
  "owner": {
      "name": "장돌준",
      "age": 44,
      "major": "컴퓨터공학",
      "career": ["앱 개발자", "풀스택 개발자", "SI 개발자"]
    },  
    "menus": [
        {
      "name": "자바치킨",
      "price": 18000,
      "ingredients": ["닭", "튀김가루", "자바소스"]
        },
        {
          "name": "깃윙",
          "price": 6500,
          "ingredients": ["닭날개", "문어다리"]
        },
        {
          "name": "스프링소다",
          "price": 2000,
          "ingredients": ["물", "설탕", "메탄가스"]
        }
    ],
    "reviews": [
      {
            "reviewer": {
              "name": "배다른민족",
              "level": "Beginner"
       },
          "rating": "1",
          "comment": "아니 음료수 뭐냐고"
          },
          {
          "reviewer": {
              "name": "김밥순",
              "level": "VIP"
          },
          "rating": "5",
          "comment": "개발팀장님 힘내세요. 많이 시켜먹을게요."
        }
    ]
}
```



------



## YAML

```yaml
name: 돌준이네 치킨
location: 닭볶로 12번길
# 가게 주인 정보
owner:
  name: 장돌준
  age: 44
  major: 컴퓨터공학
  career:
    - 앱 개발자
    - 풀스택 개발자
    - SI 개발자
menus:
  - name: 자바치킨
    price: 18000
    ingredients:
      - 닭
      - 튀김가루
      - 자바소스
  - name: 깃윙
    price: 6500
    ingredients:
      - 닭날개
      - 문어다리
  - name: 스프링소다
    price: 2000
    ingredients:
      - 물
      - 설탕
      - 메탄가스
reviews:
  - reviewer: 
      name: 배다른민족
      level: Beginner
    rating: '1'
    comment: 아니 음료수 뭐냐고
  - reviewer:
      name: 김밥순
      level: VIP
    rating: '5'
    comment: 개발팀장님 힘내세요. 많이 시켜먹을게요.
```



[ 얄코 ](https://youtu.be/55FrHTNjTCc)