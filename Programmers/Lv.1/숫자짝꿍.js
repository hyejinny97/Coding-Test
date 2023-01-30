// https://school.programmers.co.kr/learn/courses/30/lessons/131128?language=javascript
// 코딩테스트연습 < 연습문제 < 문제.숫자 짝꿍



// 입력
/*
1. 두 정수 X, Y
- 3 <= X, Y 길이 <= 3,000,000
- 0으로 시작하지 않음
*/




// 출력
/*
1. X, Y의 짝꿍을 return
- 짝꿍이 존재하지 않으면 -1을 return
- X, Y의 짝꿍이 0으로만 구성되어 있다면 0을 return

<짝꿍 찾는법>
- 두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)를 찾음
- 정수 k들을 이용하여 만들 수 있는 가장 큰 정수가 두 수의 짝꿍임
*/




// 코드
'use strict'
function solution(X, Y) {
  const xNums = new Array(10).fill(0);  // idx = 문자, value = 문자 개수
  const yNums = new Array(10).fill(0);

  // X, Y 문자열의 각 char의 개수 카운트
  for (let char of X) {
    xNums[Number(char)] += 1
  }
  for (let char of Y) {
    yNums[Number(char)] += 1
  }

  // 두 문자열의 짝꿍 찾기
  let partner = '';
  for (let i = 9; i >= 0; i--) {
    const min_val = Math.min(xNums[i], yNums[i]);
    // 두 문자열에서 여러 개의 '0'만 공통으로 존재하는 경우, 짝꿍은 '0'
    partner += !partner && !i && min_val ? '0' : String(i).repeat(min_val);
  }

  return partner ? partner : '-1'
}


// 실행 결과: 성공
