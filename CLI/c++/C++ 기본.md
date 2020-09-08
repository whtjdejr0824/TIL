## C++ 기본(1)

#### 1. 프로그램 구조

```c++
// #include : 헤더파일을 포함시키는 기능. / 외부 프로그램 소스를 포함시키는 매크로
// iosteram : 입출력 관련 기본 라이브러리. / std namespace를 정의 
# include <iostream>

using namespace std;

// 실행 과정 : 컴파일 -> 빌드 -> 실행
// 컴파일 : 번역작업.
// Ctrl + Shift + B : 컴파일 및 빌드
// Ctrl + Alt + N : 코드 실행
// Ctrl + F5 : exe프로그램실행

// C++의 시작점은 main함수이므로, 반드시 있어야 한다.
int main() {
  
  // C++ 표준 기능의 대부분은 std 라는 namespace 안에 존재한다. 
  // 이름이 겹치는 것을 방지해주기 위해서 이다.
  // :: : 스코프 연산자(어디에 정의되어 있는지 지정할 때 사용)
  // cout : consolout(콘솔창에 출력해주는 기능. 뒤에 있는 ""(큰따옴표) 안에 있는 문자들을
  // 화면에 출력해준다.)
  // endl : 개행기능(ENTER)
    
  std::cout << "Test Output" << std::endl;
  std::cout << "abcd" << std::endl;
 
  cout << "using namespace std" << endl; //std를 써도 에러 발생하지 않는다.
  return 0;
}

```

#### 

출처 : [어소트락 게임아카데미 유튜브](https://www.youtube.com/watch?v=WZLkdz277DA&lc=z23ddnnabtufupoa204t1aokg1idllo2fqcjxpjosne2bk0h00410)

