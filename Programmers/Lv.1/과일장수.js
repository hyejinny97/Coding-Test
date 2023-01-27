// https://school.programmers.co.kr/learn/courses/30/lessons/135808?language=javascript
// 코딩테스트연습 < 연습문제 < 문제.과일 장수



// 입력
/*
1. 사과의 최대 점수 k, 한 상자에 들어가는 사과의 수 m, 사과들의 점수 score
- 3 <= k <= 9
- 3 <= m <= 10
- 7 <= score 길이 <= 1,000,000
*/




// 출력
/*
1. 과일 장수가 얻을 수 있는 최대 이익을 return
- 이익이 발생하지 않는 경우, 0을 return

<사과 한 상자의 가격>
- 한 상자에 사과를 m개씩 담아 포장
- 상자에 담긴 사과 중 가장 낮은 점수가 p (1 ≤ p ≤ k)점
- 사과 한 상자의 가격은 p * m 
- 총 가격 = (최저 사과 점수) x (한 상자에 담긴 사과 개수) x (상자의 개수)
*/



// 코드 

// 접근방법
/*
1. 사과 점수(score)을 내림차순으로 정렬
2. 앞에서부터 m개씩 끊어 사과 한 상자를 만듦
  - 사과 한 상자의 가격 = 최저 사과 점수 x m
3. 2번을 반복해서 사과 상자 가격을 구해 더해줌
*/

function solution(k, m, score) {
  score.sort((a, b) => b - a)
  let totPrice = 0;
  for (let i = 0; i < score.length; i += m) {
    if (score.length - i >= m) {
      totPrice += score[i + m - 1] * m
    }
  }
  return totPrice
}


// 실행 결과: 성공