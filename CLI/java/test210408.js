let arr2 = []
let end = []
function Greatset(arr){
for(i=0; i<arr.length; i++){
    for(j=0; j<arr.length; j++){
        chk = arr[i]
        chk2 = arr[j]
        del = arr.indexOf(chk)
        if(i != j){
            if(chk + chk2 == 0){
            arr2.push(chk)
            arr2.sort(function(a, b){
                return a-b ;
            })
            }
        }
    }
}return arr2;
}
function End(array){
    let X = Greatset(array)
    end.push(arr2[0])
    arr2.sort(function(a, b){
        return b-a ;
    })
    end.push(arr2[0])
    return end;
}
A = [-4, 3, 7, -1, 0, 2, -3, 5, 4, 6, -6, -6, -7]
// Greatset(A)
console.log(End(A))
// a = arr2.length;
// console.log(arr2[0])
