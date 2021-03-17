# Data Class& Enum Class

#### Date Class

데이터를 다루는 데에 최적화된 class로, '5가지 기능'을 내부적으로 자동으로 생성해줌.

1) 내용의 동일성을 판단하는 equals()의 자동구현

2) 객체의 내용에서 고유한 코드를 생성하는 hashcode()의 자동구현

3) 포함된 속성을 보기쉽게 나타내는 toString()의 자동구현

4) 객체를 복사하여 똑같은 내용의 새 객체를 만드는 copy()의 자동구현

여기서 copy()함수를 통해 새 객체를 생성할 때는,

아무 패러미터가 없으면 똑같은 내용으로 생성함

``` kotlin
val a = Data("A", 7)
val b = a.copy()
```

패러미터가 있으면 해당 패러미터를 교체하여 생성함

```kotlin
val a = Data("A",7)
val b = a.copy("B") //*b는 Data("B",7)으로 생성됨
```

5) 속성을 순서대로 반환하는 componentX()의 자동구현

```kotlin
Data("A",7)
//"A" = component1() / 7 = component2()
```

이 함수는 사용자가 직접 호출하기 위한 함수가 아닌

```kotlin
listOf(Data("A",7),Data("B",1))
```

이내용을 자동으로 꺼내 쓸 수 있는 기능을 지원하기 위한 함수들.

```kotlin
fun main(){
    
}
```

