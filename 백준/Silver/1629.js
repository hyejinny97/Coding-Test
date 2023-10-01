// https://www.acmicpc.net/problem/1629
// 문제 1629번.곱셈
// 시간: 0.5초, 메모리: 128MB

// 입력
/*
1. 자연수 A, B, C
- 0 < A, B, C <= 2,147,483,647  
*/

// 출력
/* 
1. A를 B번 곱한 수를 C로 나눈 나머지를 출력
*/

// 코드 1
// const fs = require("fs");
// const [A, B, C] = fs
//   .readFileSync("./input_text/1629.txt")
//   .toString()
//   .trim()
//   .split(" ")
//   .map((n) => +n);

// let currentRemainder = 1;
// const remainders = [];
// for (let n = 1; n <= B; n++) {
//   currentRemainder = (currentRemainder * A) % C;

//   const idx = remainders.indexOf(currentRemainder);
//   const noExist = idx === -1;
//   if (noExist) {
//     remainders.push(currentRemainder);
//   } else {
//     console.log(
//       remainders.slice(idx).at(((B - idx) % (remainders.length - idx)) - 1)
//     );
//     break;
//   }
// }

// 실행 결과: 실패

// 코드 2
// 접근 방법
/*
- 모듈러 연산: (A * B) mod C = ((A mod C) * (B mod C)) mod C
- 소수점 결과를 포함하는 연산을 BigInt와 사용하면 소수점 이하는 사라짐

문제 풀이 참고) https://tesseractjh.tistory.com/249
BigInt 참고) https://velog.io/@ywc8851/javascript-Number-vs-BigInt
*/
// // A^B % C (= A^power % C)를 구하는 함수
// const mode = function (power) {
//   if (power == 1n) {
//     return A % C;
//   }

//   const isEven = power % 2n === 0;

//   if (isEven) {
//     return (mode(power / 2n) * mode(power / 2n)) % C;
//   } else {
//     return (mode(power / 2n) * mode(power / 2n) * mode(1)) % C;
//   }
// };

// const fs = require("fs");
// const [A, B, C] = fs
//   .readFileSync("./input_text/1629.txt")
//   .toString()
//   .trim()
//   .split(" ")
//   .map(BigInt);

// console.log(mode(B).toString());

// 실행 결과: 실패 (시간 초과)

// 코드 3
// // A^B % C (= A^power % C)를 구하는 함수
// const mode = function (power) {
//   if (power === 1) {
//     record[1] = A % C;
//   }

//   if (Object.keys(record).includes(power.toString())) {
//     return record[power.toString()];
//   }

//   const isEven = power % 2 === 0;
//   const half = mode(Math.floor(power / 2));

//   if (isEven) {
//     record[power] = (half * half) % C;
//   } else {
//     record[power] = (half * half * mode(1)) % C;
//   }

//   return record[power];
// };

// const fs = require("fs");
// const [A, B, C] = fs
//   .readFileSync("./input_text/1629.txt")
//   .toString()
//   .trim()
//   .split(" ")
//   .map((num) => +num);

// const record = {}; // key: (A^x % C)에서 지수 값(x), value: (A^x % C) 계산값
// console.log(mode(B));

// 실행 결과: 실패

// 코드 4
// A^B % C (= A^power % C)를 구하는 함수
const mode = function (power) {
  if (power === 1n) {
    return A % C;
  }

  const isEven = power % 2n === 0n;
  const half = mode(power / 2n);

  if (isEven) {
    return (half * half) % C;
  } else {
    return (half * half * mode(1n)) % C;
  }
};

const fs = require("fs");
const [A, B, C] = fs
  .readFileSync("./input_text/1629.txt")
  .toString()
  .trim()
  .split("\n")
  .at(0)
  .split(" ")
  .map(BigInt);

console.log(mode(B).toString());

// 실행 결과: 성공(메모리: 9332kb, 시간: 124ms)
