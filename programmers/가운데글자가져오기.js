function solution(s) {
  var answer = '';
  const len = s.length;
  const isOne = len % 2;

  if (isOne === 1) {
    const value = parseInt(s.length / 2)
    answer += value
  } else {
    const firstIdx = parseInt(s.length / 2) - 1,
        secondIdx = parseInt(s.length / 2);
    const firstValue = s[firstIdx],
        secondValue = s[secondIdx];
    answer += firstValue
    answer += secondValue
  }

  return answer;
}

const s = "qwer";
const result = solution(s);
console.log(result)