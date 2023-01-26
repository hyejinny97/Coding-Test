// https://school.programmers.co.kr/learn/courses/30/lessons/142086?language=javascript
// 코딩테스트연습 < 연습문제 < 문제.가장 가까운 같은 글자



// 입력
/*
1. 문자열 s
- 1 <= s 길이 <= 10,000
- s는 영어 소문자로만 이루어짐
*/




// 출력
/*
1. s의 각 위치마다 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자 위치를 return
*/




// 코드 1
'use strict'
function solution(s) {
  const record = {}
  const answer = [];
  for (let i = 0; i < s.length; i++) {
    if (record[s[i]]) {
      answer.push(i - record[s[i]])
    } else {
      answer.push(-1)
    }
    record[s[i]] = i
  }
  return answer;
}


// 실행 결과: 실패(이유: record[s[i]] = 0인 경우에도 undefined와 같이 false로 처리됨)



// 코드 2
'use strict'
function solution(s) {
  const record = {}
  const answer = [];
  for (let i = 0; i < s.length; i++) {
    if (record[s[i]] !== undefined) {
      answer.push(i - record[s[i]])
    } else {
      answer.push(-1)
    }
    record[s[i]] = i
  }
  return answer;
}


// 실행 결과: 성공



// 코드 3

// 접근방법
/* 
Array.prototype.lastIndexOf() 참고: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/lastIndexOf
*/

'use strict'
function solution(s) {
  const answer = [];
  for (let i = 0; i < s.length; i++) {
    const idx = [...s].slice(0, i).lastIndexOf(s[i])
    const val = idx === -1 ? -1 : i - idx
    answer.push(val)
  }
  return answer
}


// 실행 결과: 성공