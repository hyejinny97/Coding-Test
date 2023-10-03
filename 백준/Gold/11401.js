// https://www.acmicpc.net/problem/11401
// 문제 11401번.이항 계수3
// 시간: 1초, 메모리: 256MB

// 입력
/*
1. 자연수 N과 정수 K 
- 1 ≤ N ≤ 4,000,000, 0 ≤ K ≤ N
*/

// 출력
/* 
1. 이항 계수를 1,000,000,007로 나눈 나머지를 출력
*/

// 코드 1
// 접근방법
/*
(A / B) % p = (A * B^-1) % p = ((A % p) * (B % p)^-1) % p  => 잘못된 식!
*/
// (A * B) mod C 값을 반환
// ∴ num에서부터 1씩 감소한 숫자를 count 개수만큼 곱한 값 % DIVISION을 반환
// const mode = function (num, count) {
//   if (count === 0n) return 1n;

//   return (
//     ((num % DIVISION) * (mode(num - 1n, count - 1n) % DIVISION)) % DIVISION
//   );
// };

// const fs = require("fs");
// const [N, K] = fs
//   .readFileSync("./input_text/11401.txt")
//   .toString()
//   .trim()
//   .split("\n")
//   .at(0)
//   .split(" ")
//   .map(BigInt);

// const DIVISION = 1000000007n;

// const minCount = K > N - K ? N - K : K;
// const rstOfTop = mode(N, minCount); // 분자 모듈러 연산
// const rstOfBottom = mode(minCount, minCount); // 분모 모듈러 연산

// console.log(((rstOfTop / rstOfBottom) % DIVISION).toString());

// 실행 결과: 실패

// 코드 2
// 접근방법
/*
<이항계수 nCk>
nCk = n!/k!(n-k)!

<나눗셈에 대한 모듈러 연산>
(A / B) % p = (A * B^(p-2)) % p = ((A % p) * (B^(p-2) % p)) % p

<이항계수 nCk에 대한 모듈러 연산>
(n! / k!(n-k)!) % p = (n! * (k!(n-k)!)^(p-2)) % p = ((n! % p) * ((k!(n-k)!)^(p-2) % p)) % p

참고) 페르마의 소정리: https://velog.io/@gidskql6671/%EB%82%98%EB%A8%B8%EC%A7%80Modulo-%EC%97%B0%EC%82%B0-%EB%B6%84%EB%B0%B0%EB%B2%95%EC%B9%99
참고) https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-11401-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9D%B4%ED%95%AD-%EA%B3%84%EC%88%98-3-%EA%B3%A8%EB%93%9C1-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5
참고) https://rhdtka21.tistory.com/123
*/

// A**B mod C를 반환
// const mode = function (A, B, C) {
//   const recursion = function (power) {
//     if (power == 1n) return A % C;

//     const isEven = power % 2n === 0n;
//     const half = recursion(power / 2n);

//     if (isEven) {
//       return (half * half) % C;
//     } else {
//       return (half * half * recursion(1n)) % C;
//     }
//   };

//   return recursion(B);
// };

// const fs = require("fs");
// const [N, K] = fs
//   .readFileSync("./input_text/11401.txt")
//   .toString()
//   .trim()
//   .split("\n")
//   .at(0)
//   .split(" ")
//   .map(BigInt);
// const DIVISION = 1000000007n; // 나눠야할 값

// // DP를 이용해 팩토리얼 값 구하기
// const factorials = Array(Number(N) + 1).fill(null); // 각 idx에 해당하는 value = idx!

// factorials.forEach((_, idx, arr) => {
//   if (idx === 0 || idx === 1) return (arr[idx] = 1n);

//   return (arr[idx] = arr[idx - 1] * BigInt(idx));
// });

// const factOfTop = factorials[N]; // nCk의 분자값
// const factOfBottom = factorials[K] * factorials[N - K]; // nCk의 분모값

// console.log(
//   (
//     ((factOfTop % DIVISION) * mode(factOfBottom, DIVISION - 2n, DIVISION)) %
//     DIVISION
//   ).toString()
// );

// 실행 결과: 실패(메모리 초과)

// 코드 3
// A**B mod C를 반환
const mode = function (A, B, C) {
  const recursion = function (power) {
    if (power == 1n) return A % C;

    const isEven = power % 2n === 0n;
    const half = recursion(power / 2n);

    if (isEven) {
      return (half * half) % C;
    } else {
      return (half * half * recursion(1n)) % C;
    }
  };

  return recursion(B);
};

const fs = require("fs");
const [N, K] = fs
  .readFileSync("./input_text/11401.txt")
  .toString()
  .trim()
  .split("\n")
  .at(0)
  .split(" ")
  .map(BigInt);
const DIVISION = 1000000007n; // 나눠야할 값

// DP를 이용해 팩토리얼 값 구하기
const factorials = Array(Number(N) + 1).fill(null); // 각 idx에 해당하는 value = idx!

factorials.forEach((_, idx, arr) => {
  if (idx === 0 || idx === 1) return (arr[idx] = 1n);

  return (arr[idx] = (arr[idx - 1] * BigInt(idx)) % DIVISION);
});

const factOfTop = factorials[N]; // nCk의 분자값
const factOfBottom = factorials[K] * factorials[N - K]; // nCk의 분모값

console.log(
  (
    ((factOfTop % DIVISION) * mode(factOfBottom, DIVISION - 2n, DIVISION)) %
    DIVISION
  ).toString()
);

// 실행 결과: 성공(메모리: 197744kb, 시간: 1764ms)
