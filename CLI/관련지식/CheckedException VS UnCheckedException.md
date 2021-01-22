# CheckedException VS UnCheckedException



**CheckedException** : 컴파일 시점에 명시적으로 예외상황을 처리해야하는 예외 기법. 자바 CLASS 중 Exception 을 상속받아 만들 수 있다.

명시적으로 예외를 처리한다 함은, 자바 언어 기준으로, try~catch 구문을 사용하는것을 의미. 명시적인 예외를 처리하지 않는다면 컴파일이 되지 않아, 코드 에디터에서 빨간 줄이 생김.

**UnCheckedException** : 런타임 시점에 예외상황을 처리하는 예외 기법. 자바 CLASS 중 RuntimeException 을 상속받아 만들 수 있다.

> 런타임 시점이란, 컴파일이 된 후 프로그램이 실행될 때, 어느 특정 상황을 의미.

위에서 살펴본 **CheckedException** 예외와는 다르게, 명시적으로 처리할 필요가 없다. 개발자가 필요시에 try~catch 구문을 이용하여 처리한다.



## CheckedException의 특징

------

**CheckedException**은 사실 현대적인 언어에서는 제공하지 않는 경우가 많다.

사실상 필요없다는 의견도 많을 뿐더러, 프로그래밍에 있어서 큰 단점을 가지고 있기 때문이다. 하지만 장점도 가지고 있는데요, 해당 내용을 알아봅시다.

**CheckedException** 의 최고 장점은 아무래도 안정적인 소프트웨어를 만들 수 있는 길을 제시해준다.

**CheckedException** 을 제공하는 개발자는 빈번하게 발생할 수 있는 예외 케이스 를 제공해줌으로써, 해당 메서드를 사용하는 개발자로 하여금 UnHappyPath 에 대해 생각할 수 있는 여지를 제공해준다.

> *UnCheckedException도 예외케이스를 제공해주지만 명시적인 작성에 대한 안정성이 있다.*

단점은 항상 명시적으로 작성해야 한다.

예를들어, FileInputStream("파일이름") 객체를 만든다고 가정하면, 해당 객체는 FileNotFoundException 이라는 **CheckedException** 처리를 해야한다.

해당 파일이름으로 된 파일이 없는 경우를 대비하라는 의미이다.

만약, 해당 파일이 항상 존재한다고 가정할 수 있는 경우, 해당 경우에는 불필요한 try~catch 구문이 들어가, 코드 가독성을 해치게 된다.

또한 해당 파일이 항상 존재한다는 상황의 표현도 되지 않는것도 큰 문제라 볼수 있다.

프로그래밍이란 것은 아무래도 흐름을 통해 특정 상황을 만드는 일이 빈번하다 보니,

**CheckedException**은 프로그래밍에 있어서 비효율적인 상황으로 다가오는 경우가 많다.

## UnChecekdException의 특징

------

**UnCheckedException** 은 **CheckedException** 의 명확한 단점을 극복할 수 있는 장점이 있지만, 반대로 단점은 명시적으로 예외를 정의할수 있게 유도하지 못한다는 점이다.

하지만 이는 예외상황은 특정 메서드를 사용할 때는 메서드를 탐색하면 어떤 예외가 있는지 확인할 수 있기 때문에 프로그래머가 신경써야 한다는 점에 있어서 큰 단점이 되지 않는다.

그 결과, 현대적인 언어에서는 예외처리를 **UnCheckedException** 으로 제공하는 경우가 많다.

## 마무리

주로 ***숙련된 프로그래머***는 **CheckedException** 의 단점이, ***초보 프로그래머***에게는 **CheckedException**의 장점이 더 부각되는 상황이 될거 같다.

프로그래밍을 많이 할수록 예외 처리는 RuntimeException 을 상속받아 처리하는 부분으로 빈번하게 처리된다.

출처: [blog](https://mommoo.tistory.com/)