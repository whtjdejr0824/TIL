# argument & infix

코틀린에서도 대부분의 언어에서 지원하는 함수의 overloading이 지원됨

'같은 Scope 안'에서  같은 이름의 함수를 여러개 만들 수 있는 기능.

`fun same (x: Int)` `fun same (x: Int, text: String)` `fun same (x: Int, y: Int)` 

이름이 같더라도, 패러미터의 자료형이 다르거나, 갯수가 다르다면, 서로 다른 함수로 동작할 수 있음.

다만, 패러미터 이름만 다르게 묶고, 자료형과 갯수가 동일 하다면, 오버로딩을 할 수 없음.

`fun same (x: Int, y: Int)`, `fun same (a: Int, b: Int)`



```kotlin
fun main() {
    
    read(7)
    read("감사합니다")
    
} 

fun read(x: Int) {
    println("숫자 $x 입니다") // 숫자 7입니다.
}

fun read(x: String) {
    println(x)  // 감사합니다.
}
```



패러미터를 받아야 하는 함수이지만,  별다른 패러미터가 없더라도 기본값으로 동작해야 한다면,

`default arguments`사용.



```kotlin
fun main() {
    deliveryItem("짬뽕") //짬뽕, 1개를 집에 배달하였습니다.
    deliveryItem("책", 3) //책, 3개를 집에 배달하였습니다.
    deliveryItem("노트북", 30, "학교") //노트북, 30개를 학교에 배달하였습니다.
    
    deliveryItem("선물", destination = "친구집") //선물, 1개를 친구집에 배달하였습니다.
}

fun deliveryItem(name: String, count: Int = 1, destination: String = "집") {
    println("${name}, ${count}개를 ${destination}에 배달하였습니다")
}
```

이름과 목적지만 넣고, 개수는 기본값을 이용하고 싶다면, `named argument` 사용

`named argument`는 패러미터 순서와 관계없이, 패러미터의 이름을 사용하여 직접 패러미터의 값을 할당하는 기능.

`deliveryItem("선물",1,"친구집")` -> 가운데 숫자를 지우게 되면 동작X



같은 자료형을 갯수에 상관없이, 패러미터로 받고 싶을 때  `variable number of argument`(vararg)

```kotlin
fun main() {
    sum(1, 2, 3, 4)
}

fun sum(vararg numbers: Int) {
    var sum = 0
    
    for(n in numbers) {
        sum += n
    }
    
    print(sum) // 10
}
```

vararg는 개수가 지정하지 않는 패러미터라는 특징이 있음

`fun sample(text; String, vararg x: Int)`



연산자처럼 쓸 수 있는`infix function`

```kotlin
fun main() {
    println(6 multiply 4) // 24
    
    println(6.multiply(4)) // 24
}

infix fun Int.multiply(x: Int): Int = this*x
```

class안에서 infix 함수를 선언할 때에는 적용할 클래스가 자기 자신이므로, `infix fun multiply(x: Int): Int = this*x`