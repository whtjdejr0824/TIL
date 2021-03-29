function compareArr(arr1, arr2){

    let temp = "";
    if(arr1.length!=arr2.length) return false;

    for(let i=0; i<arr1.length; i++) {
        temp = arr1[i];
        let index = arr2.indexOf(temp);
        if(index == -1) return false;
        arr2.splice(index, 1);
    }

    return true;

}
console.log(compareArr(['i','c','e','c','r','e','a','m'], ['c','r','e','a','m','i','c','e'])); // ---> true
console.log(compareArr(['a','s','d','f','a','s','d','f'], ['a','s','d','f','a','s','d','d'])); // ---> false
