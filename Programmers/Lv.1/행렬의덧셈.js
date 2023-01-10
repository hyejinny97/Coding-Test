// https://school.programmers.co.kr/learn/courses/30/lessons/12950
// 코딩테스트연습 < 연습문제 < 문제.행렬의 덧셈



// 입력
/*
1. 2개의 행렬 arr1과 arr2
- 0 < 행과 열의 길이 <= 500
*/




// 출력
/*
1. 행렬 덧셈의 결과를 반환
<행렬의 덧셈>
행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과
*/


// 코드
function solution(arr1, arr2) {
  var answer = [];
  for (let r = 0; r < arr1.length; r++) {
    row = []
    for (let c = 0; c < arr1[0].length; c++) {
      row.push(arr1[r][c] + arr2[r][c])
    }
    answer.push(row)
  }
  return answer
}


// 실행 결과: 성공