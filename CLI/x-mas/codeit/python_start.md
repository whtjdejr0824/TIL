# 파이썬 시작하기

## 1. 우리가 사용할 도구들

python ineterpreter :python 코드를 MachineCode로 번역해서 Computer로 전달해 주는 프로그램

PyCharm : 통합 개발 환경(IDE : Integrated Development Enviroment)



## 02. 파이썬& 파이참 설치하기

### Window

- webBrowser에서 'python' 검색<p>
        -> www.Python.org로 이동<p>
​        -> Downloads<p>
​        -> Download the latest version for Windows<p>
​        -> Install launcher for all users(checked)<p>
​        -> Add Python 3.8 to PATH(checked)<p>
​        -> Installed Now(Click)

- webBrowser에서 'Pycharm' 검색<p>
        -> www.jetbrains.com로 이동<p>
        -> '다운로드'클릭<p>
        -> 'Community'다운<p>
        -> 모든 체크박스 체크<p>

### Mac

- webBrowser에서 'python' 검색<p>
        -> www.Python.org로 이동<p>
​        -> Downloads<p>
​        -> Download the latest version for Mac OS X<p>

- webBrowser에서 'Pycharm' 검색<p>
        ->www.jetbrains.com로 이동<p>
        ->'다운로드'클릭<p>
        ->'Community'다운<p>
        ->PyCharm CE를 Applications폴더로 이동<p>

## 03. 프로그래밍이란?
계산할 수식들을 컴퓨터에게 알려주는 것
자료형(DATA TYPE)<p> 
정수(integer) : -1,0,1<p>
소수(flouting Point) : 0.1, 2.0<p>
문자열(String) : "Hello", "2"<p>
부울린(Boolean) : True, False<p>

## 04. 추상화개요
추상화(Abstraction) : 복잡한 내용은 **숨기고**, **주요** 기능에만 신경쓰자!

변수(Variable) : 값을 저장하는 것

함수(Function) : 명령을 저장하는 것

객체(Object) : <p>
``` python
object
    buger_price = 4900
    fries_price = 1490
    drink_price = 1250

    print(buger_price)
    print(buger_price*2)
    print(buger_price + fries_price)
    print(buger_price * 3 + fries_price * 2 + drink_price * 5)

fuction
    def hello():
        print("Hello!")
        print("Welcome to Codeit!")

    hello()
    hello()
    hello()

Parameter : 매개변수(함수를 정의할 때 쓰개 되는 변수)
    def hello(name):
        print("Hello!")
        print(name)
        print("Welcome to Codeit!")

    hello("Chris")

    def print_sum(num1, num2, num3):
        print(num1+num2+num3)
    
    print_sum(7, 3, 2)

return : 돌려준다.
    def get_square(x):
        return x * x

    y = get_square(3)
    print(y) // 3*3 = 9
    print(get_square(3)+get_square(4)) // 3*3+4*4=25
```

