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
    
    val a = General("보영", 212)
    
    println(a == General("보영", 212)) // false
    println(a.hashCode()) // 681842940
    println(a) //General@28a418fc
    
    val b = Data("루다", 306)
    
    println(b == Data("루다", 306)) // true
    println(b.hashcode()) // 46909878
    println(b) // Data(name = 루다, id = 306)
    
    println(b.copy()) // Data(name = 루다, id = 306)
    println(b.copy("아린")) // Data(name = 아린, id = 306)
    println(b.copy(id = 618)) // Data(name = 아린, id = 618)
}

class General(val name: String, val id: Int)

data class Data(val name: String, val id: Int)
```

```kotlin
fun main(){
    val list = listOf(Data("보영", 212),
                      listOf(Data("루다", 306),
                      listOf(Data("아린", 618))
                             
    for((a, b) in list){ // a = conponent1() / b = conponent2()
        println("${a},${b}")
        // 보영, 212
        // 루다, 306
        // 아린, 618
    }
}

class General(val name: String, val id: Int)

data class Data(val name: String, val id: Int)
```



#### Enum lass

enumerated type, '열거형'의 준말로,

```kotlin
enum class Color {
    RED, // 특이한 형태이지만, 모두 enum class인 
    BLUE, // Color의 객체를 생성하기 위한 선언
    GREEN 
}
```



enum 클래스 안의 객체들은 관행적으로 상수를 나타낼 때 대문자로 기술함

또한 enum의 객체들은 고유한 속성을 가질 수 있음

``` kotlin
enum class Color (val number: Int) {
    RED(1),
    BLUE(2),
    GREEN(3);
    
    fun isRed() = this == Color.RED // 또한 일반 클래스처럼 함수도 추가 가능
}
```



```kotlin
fun main() {
    
    var state = State.SING // *enum은 선언시에 만든 객체를 이름으로 참조하여 그대로 사용하게 됨
    println(state) // SING
    
    state = State.SLEEP
    println(state.isSleeping()) // true
    
    state = State.EAT
    println(state.message) // 밥을 먹습니다
}

enum class state(val message: String) {
    SING("노래를 부릅니다"),
    EAT("밥을 먹습니다"),
    SLEEP("잠을 잡니다");
    
    fun isSleeping() = this == State.SLEEP
}
```

data class와 enum class는 일반 클래스에서 제공되지 않는 특정한 용도의 기능들을 제공.