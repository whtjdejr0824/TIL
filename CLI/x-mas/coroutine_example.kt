import kotlinx.coroutines.*
import kotlin.system.measureTimeMillis


fun main(args: Array<String>) = runBlocking<Unit> {
//    val time = measureTimeMillis {// measureTimeMillis 블록 내부 실행에 걸리는 시간 반환
//        val one = testOne()		// suspend 함수 1
//        val two = testTwo()		// suspend 함수 2
//    }
//    println("Completed in ${time}ms") // 총 걸린 시간 표시
//
//    val dateAndtime: LocalDateTime = LocalDateTime.now()
////    println("Current date and time: $dateAndtime")

-------------------------------------------------------------------------------------
3초 대기
10초 대기
Completed in 13045 ms
-------------------------------------------------------------------------------------

    val time = measureTimeMillis {
        val one = async { testOne() }
        val two = async { testTwo() }
    }
    println("Completed in $time ms")
}


suspend fun testOne() {
    delay(3000)
    println("3초 대기")// 3초 대기
}

suspend fun testTwo() {
    delay(10000)			// 10초 대기
    println("10초 대기")
}

------------------------------------------------------------------------------------------
3초 대기
10초 대기
Completed in 10044 ms
------------------------------------------------------------------------------------------
 
