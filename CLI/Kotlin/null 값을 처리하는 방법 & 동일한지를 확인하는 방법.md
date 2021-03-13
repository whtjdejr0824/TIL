# null 값을 처리하는 방법 & 동일한지를 확인하는 방법

코틀린에서 nullable  변수를 만들어 `var sample: String? = null`을 만들 수 있음

하지만 null 상태로 속성이나 함수를 쓰려고 하면 null pointer exception이 발생하기 때문에

(* null인 객체를 참조하면 발생하는 오류)

```kotlin
var sample: String? = null
if(sample != null) 
// nullable 변수를 사용할 때에는 null 체크 없이는 코드가 컴파일 되지 않음
  println(sample.toUpperCase())
```

null  체크를 하기 위해 일일히 if문으로 조건을 체크하는 대신 `?.`(null safeoperator), `?:`(elvis operator), `!!.`(non-null assertion operator) 등을 사용할 수 있음

`sample?.toUpperCase()`-> `?.`(null safeoperator)는 참조연산자를 실행하기 전에 먼저 객체가 null인지 확인부터하고, 객체가 null이라면 뒤따라오는 구문(`toUpperCase()`을 실행하지 않는다.



`sample?:"default"` -> `?:`(elvis operator)는 객체가 null이 아니라면 그대로 사용하지만, null이라면 

연산자 우측 객체로 대체되는 연산자(sample이 null이면, "default"사용)



`sample!!.toUpperCase()`-> `!!.`(non-null assertion operator)는 참조연산자를 사용할 때, null 여부를 컴파일시 확인하지 않도록 하여 런타임시 null pointer exception이 나도록 의도적으로 방치하는 연산자



```kotlin
fun main() {
    var a: String? = null 
    println(a?.toUpperCase()) // -> null
    println(a?:"default".toUpperCase()) // -> DEFAULT
    println(a!!.toUpperCase()) // -> error발생 후 프로그램 종료 (Exception in thread "main" kotlin.KotlinNullPointerException)
}
```

null safe 연산자는 스코프 함수와 사용하면, 더욱 편리

```kotlin
fun main() {
   // var a: String? = null // a가 null이기 때문에, scope 함수 전체가 수행되지 않음(print 결과가 없음)
    var a: String? = "Kotlin Exam" // scope 함수 run 전체가 실행
    // null을 체크하기 위해 if문 대신 사용하면 상당히 편리한 기능
    
    a?.run{
        println(toUpperCase()) // KOTLIN EXAM
        println(toLowerCase()) // kotlin exam
    }
}
```



변수의 동일성을 체크하는 방법

동일성에는 두가지 개념이 있음

내용의 동일성 : 메모리 상의 서로 다른 곳에 할당된 객체라고 해도, 그 내용이 같다면, 동일하다고 판단하는 것

내용의 동일성을 판단하는 연산자 :  `a==b`



객체의 동일성 : 서로 다른 변수가 메모리 상에 같은 객체를 가리키고 있을 때만 동일하다고 판단

객체의 동일성을 판단하는 연산자 :  `a === b`



이 중 내용의 동일성은 자동으로 판단되는 것이 아닌, 코틀린의 모든 클래스가 내부적으로 상속받는 ''`Any`"라는 최상의 클래스의 `equals()`함수가 반환하는 Boolean 값으로 판단하게 됨



기본 자료형에는 자료형의 특징에 따라 `equals()`함수가 이미 구현되어 있지만,



커스텀 class를 만들때는 `open fun equals(other: Any?):Boolean`를 상속받아 동일성을 확인해주는 구문을 별도로 구현해야 함.

``` kotlin
fun main() {
    var a = Product("콜라", 1000)
    var b = Product("콜라", 1000)
    var c = a
    var d = Product("사이다", 1000)
    
    println(a == b) // true
    println(a === b) // false
    
    println(a == c) // true
    println(a === c) // true
    
    println(a == d) // false
    println(a === d) // false
}

class Product(val name: String, val price: Int) {
    override fun equals(other: Any?): Boolean {
        if(other is Product) {
            return other.name == name && other.price == price
        } else {
            return false
        }
    }
}
```



null 처리와 동일성 확인은 프로그램 작성 도중 빈번하게 사용하는 기능