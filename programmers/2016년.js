function solution(a, b) {
  // set dates
  let date = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
  // set days in each month
  let days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  let totalDate = days.splice(0, a - 1).reduce((acc, cur) => acc + cur, 0) + b
  
  const idx = (totalDate - 1) % 7;
  
  return date[idx];
}

const a = 5,
    b = 24;

const result = solution(a, b)
console.log(result)