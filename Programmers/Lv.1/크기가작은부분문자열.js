// https://school.programmers.co.kr/learn/courses/30/lessons/147355
// 코딩테스트연습 < 연습문제 < 문제.크기가 작은 부분문자열



// 입력
/*
1. 숫자로 이루어진 문자열 t와 p
- 1 <= p 길이 <= 18
- p 길이 <= t 길이 <= 10,000
- t, p: 숫자로만 이루어진 문자열(0으로 시작하진 않음)
*/




// 출력
/*
1. t에서 p와 길이가 같은 부분문자열 중에서, 이 부분문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 나오는 횟수를 return
*/




// 코드 
function solution(t, p) {
  let cnt = 0;
  const num_p = Number(p)
  for (i = 0; i <= t.length - p.length; i++) {
    if (Number(t.slice(i, i + p.length)) <= num_p) {
      cnt += 1
    }
  }
  return cnt
}


// 실행 결과: 성공