// Math.max.apply(null, 배열); // 최대값
// Math.min.apply(null, 배열); //최소값

// var test = [-4, -3, 0, 1, 3, 5, 7];

// console.log(Math.max.apply(null, test)); //결과값은 99
// console.log(Math.min.apply(null, test)); //결과값은 0
// console.log(Math.abs.apply(null, test));

function findCouple(num){
    let temp = ""
    let collected = [];
    for(i=0; i<num.length; i++) {
        temp = num[i]
        console.log(num)
        if(Math.abs(temp) == num[i]) collected.push(temp);
    }
    return collected;
}
let result = findCouple([-4,-3,0,1,3,5]);

console.log(result);
