// https://school.programmers.co.kr/learn/courses/30/lessons/12940
// 코딩테스트연습 < 연습문제 < 문제.최대공약수와 최소공배수



// 입력
/*
1. 두 자연수
- 1 <= 자연수 <= 1,000,000
*/




// 출력
/*
1. 두 수의 최대공약수와 최소공배수를 반환
*/


// 코드 1
function solution(n, m) {
  // 최대공약수(GCD)
  let gcd;
  for (num = Math.min(n, m); num > 0; num--) {
    if (m % num === 0 && n % num === 0) {
      gcd = num
      break;
    }
  }

  // 최소공배수(LCM)
  const lcm = n * m / gcd
  return [gcd, lcm];
}


// 실행 결과: 성공



// 코드 2 

// 접근방법
/* 
<유클리드 호제법>
- 참고: https://velog.io/@yerin4847/W1-%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95
*/

function solution(n, m) {
  // 최대공약수(GCD)
  function makeGcd(a, b) {
    return b ? makeGcd(b, a % b) : a
  }
  const gcd = makeGcd(n, m)

  // 최소공배수(LCM)
  const lcm = n * m / gcd
  return [gcd, lcm];
}
console.log(solution(3, 12))
console.log(solution(2, 5))

// 실행 결과: 성공