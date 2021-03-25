function findUniqueNumbers(numbers){

    let filtered = [];
    let temp="";
    let duplicated = false;
    for(let i=0; i<numbers.length ; i++){
        temp = numbers[i];
        duplicated = false;
        for(let j=0; j<numbers.length; j++){
            if(i==j) continue;
            // console.log(numbers[j])
            if(temp==numbers[j]) duplicated = true;
        }
        
        if(!duplicated) filtered.push(temp);    

    }
    
    return filtered;
}

let result = findUniqueNumbers([]);

console.log("======= FINAL  =========");
console.log(result);
