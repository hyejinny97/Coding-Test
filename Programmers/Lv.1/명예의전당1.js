// https://school.programmers.co.kr/learn/courses/30/lessons/138477
// 코딩테스트연습 < 연습문제 < 문제.과일 장수



// 입력
/*
1. 명예의 전당 목록의 점수의 개수 k, 1일부터 마지막 날까지 출연한 가수들의 점수인 score
- 3 <= k <= 100
- 7 <= score 길이 <= 1,000
- 0 <= score <= 2,000
*/




// 출력
/*
1. 매일 발표된 명예의 전당의 최하위 점수를 return

<명예의 전당 선정 방식>
- 매일 1명의 가수가 노래를 부르고 점수를 받음
- 점수가 지금까지의 점수들 중 상위 K번째 이내이면 명예의 전당에 올라감
*/



// 코드 1
function solution(k, scores) {
  const honor = [];
  const rst = [];
  for (let score of scores) {
    honor.push(score);
    if (honor.length > k) {
      const min_idx = honor.indexOf(Math.min(...honor));
      honor.splice(min_idx, 1);
    };
    rst.push(Math.min(...honor));
  }
  return rst
}


// 실행 결과: 성공



// 코드 2
function solution(k, scores) {
  const honor = [];
  const rst = [];
  for (let score of scores) {
    honor.push(score);
    honor.sort((a, b) => a - b);
    if (honor.length > k) {
      honor.shift();
    };
    rst.push(honor[0]);
  }
  return rst
}


// 실행 결과: 성공