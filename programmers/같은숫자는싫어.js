function solution(arr)
{
    let answer = [];

    if (arr.length > 0) {
        answer.push(arr[0])
    }
    
    let index = 0
    for (let i = 0; i < arr.length; i++) {
        const value = arr[i]
        const target = answer[index]
        if (value !== target) {
            answer.push(value)
            index++ 
        } 
    }
    
    return answer;
}