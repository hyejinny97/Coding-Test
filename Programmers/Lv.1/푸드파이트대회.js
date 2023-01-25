// https://school.programmers.co.kr/learn/courses/30/lessons/134240?language=javascript
// 코딩테스트연습 < 연습문제 < 문제.푸드 파이트 대회



// 입력
/*
1. 수웅이가 준비한 음식의 양을 칼로리가 적은 순서대로 나타내는 정수 배열 food
- 2 <= food 길이 <= 9
- 1 <= food 원소 <= 1,000
- food: 칼로리가 적은 순선대로 음식의 양이 담겨 있음
- food[i]: i번 음식의 수
- food[0]: 수웅이가 준비한 물의 양(항상 1)
*/




// 출력
/*
1. 대회를 위한 음식의 배치를 나타내는 문자열을 return

<대회 진행 방식>
- 한 선수는 왼쪽에서 오른쪽으로, 다른 선수는 오른쪽에서 왼쪽으로 음식을 먹음
- 중앙에는 물을 배치하고, 물을 먼저 먹는 선수가 승리
- 두 선수가 먹는 음식의 종류와 양이 같아야 하며, 음식을 먹는 순서도 같아야 함
- 칼로리가 낮은 음식을 먼저 먹을 수 있게 배치해야 함
- 몇 개의 음식은 대회에 사용하지 못할 수도 있음
*/




// 코드
'use strict'

function solution(food) {
  let rst = '';
  for (let i = 1; i < food.length; i++) {
    rst += String(i).repeat(food[i] / 2)
  }

  return `${rst}0${rst.split('').reverse().join('')}`
}


// 실행 결과: 성공