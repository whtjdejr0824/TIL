# Set 과 Map

#### Set

List와 달리, 순서대로 정렬되지 않으며, 중복이 허용되지 않는 컬렉션.

인덱스로 위치를 지정하여 객체를 참조할 수는 없으며, `contains`로 확인하는 식으로만 사용.

`sampelSet.contains("디모")` -> "sampleSet"에 있는 "디모"가 어디있는지 알고 싶을때 사용.



`Set<out T`>, `MutableSet<T>`

List와 마찬가지로, 객체의 추가, 삭제가 가능하지 여부에 따라 사용하게 됨.

요소의 추가 :  `add(데이터)`  

​             삭제 : `remove(데이터)`

```kotlin
fun main() {
    
    val a = mutableSetOf("귤","바나나","키위")
    
    for(item in a){
        println("${item}")
        // 귤
        // 바나나
        // 키위
    }
    
    a.add("자몽") // [귤, 바나나, 키위, 자몽]
    println(a)
    
    a.remove("바나나") // [귤, 키위, 자몽]
    println(a)
    
    println(a.contains("귤")) // true
}
```

