// https://school.programmers.co.kr/learn/courses/30/lessons/12906
// 코딩테스트연습 < 스택/큐 < 문제.같은 숫자는 싫어



// 입력
/*
1. 배열 arr
- 0 < arr 크기 <= 1,000,000
- 0 < 원소 <= 9
*/




// 출력
/*
1. 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return
*/


// 코드 1 - stack으로 구현
function solution(arr) {
  const answer = [];
  while (arr.length > 0) {
    last_ele = arr.pop()
    if ((answer[answer.length - 1] !== last_ele)) {
      answer.push(last_ele)
    }
  }
  answer.reverse()
  return answer;
}


// 실행 결과: 성공



// 코드 2 - queue로 구현
function solution(arr) {
  const answer = [];
  while (arr.length > 0) {
    last_ele = arr.shift()
    if ((answer[answer.length - 1] !== last_ele)) {
      answer.push(last_ele)
    }
  }
  return answer;
}


// 실행 결과: 효율성 테스트 실패(시간초과)



// 코드 3
function solution(arr) {
  return arr.filter((val, idx) => val !== arr[idx + 1]);
}


// 실행 결과: 성공