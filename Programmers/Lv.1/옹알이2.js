// https://school.programmers.co.kr/learn/courses/30/lessons/133499
// 코딩테스트연습 < 연습문제 < 문제.옹알이(2)



// 입력
/*
1. 문자열 배열 babbling
- 1 ≤ babbling의 길이 ≤ 100
- 1 ≤ 단어의 길이 ≤ 30
- 알파벳 소문자로만 이루어짐
*/




// 출력
/*
1. 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return

<머쓱이의 조카가 할 수 있는 발음>
- "aya", "ye", "woo", "ma" 네 가지 발음
- 네 가지 발음을 조합해서 만들 수 있는 발음
- 연속해서 같은 발음을 하는 것은 못함
*/




// 코드 1
'use strict'
function solution(babbling) {
  const words = ["aya", "ye", "woo", "ma"];
  for (let word of words) {
    for (let i = 0; i < babbling.length; i++) {
      if (!babbling[i].includes(word.repeat(2))) {
        babbling[i] = babbling[i].replace(word, '')
      }
    }
  }
  return babbling.reduce((acc, val) => acc + (val ? 0 : 1), 0)
}


// 실행 결과: 실패(이유: ["woayao"]도 카운트 됨)



// 코드 2
function solution(babbling) {
  const words = ["aya", "ye", "woo", "ma"];
  for (let word of words) {
    for (let i = 0; i < babbling.length; i++) {
      if (!babbling[i].includes(word.repeat(2))) {
        babbling[i] = babbling[i].replace(word, ' ')
      }
    }
  }
  return babbling.reduce((acc, val) => acc + (val.trim() ? 0 : 1), 0)
}


// 실행 결과: 실패(이유: ["ayayeaya"]는 카운트 안됨)



// 코드 3

// 접근방법
/* 
참고: https://elena90.tistory.com/entry/JavaScript-%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8%EC%97%90%EC%84%9C-replace-%EB%A5%BC-replaceAll-%EC%B2%98%EB%9F%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC-%EB%AA%A8%EB%93%A0-%EB%AC%B8%EC%9E%90-%EB%B0%94%EA%BE%B8%EA%B8%B0-feat%EC%A0%95%EA%B7%9C%EC%8B%9D
*/

function solution(babbling) {
  const words = ["aya", "ye", "woo", "ma"];
  for (let word of words) {
    for (let i = 0; i < babbling.length; i++) {
      if (!babbling[i].includes(word.repeat(2))) {
        babbling[i] = babbling[i].replace(new RegExp(`${word}`, 'g'), ' ')
      }
    }
  }
  return babbling.reduce((acc, val) => acc + (val.trim() ? 0 : 1), 0)
}


// 실행 결과: 성공