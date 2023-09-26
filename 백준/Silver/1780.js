// https://www.acmicpc.net/problem/1780
// 문제 1780번.종이의 개수
// 시간: 2초, 메모리: 256MB

// 입력
/*
1. N×N크기의 종이
- N = 3 ^ k
- 1 <= N <= 3^7
2. N개의 줄마다 문자열이 N개
- 각 칸에는 -1, 0, 1 중 하나가 저장됨
*/

// 출력
/* 
1. -1로만 채워진 종이의 개수
2. 0로만 채워진 종이의 개수
3. 1로만 채워진 종이의 개수

<종이를 자르는 규칙>
- 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용
- 위가 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 위 과정을 반복
*/

// 코드
const isSameNumber = function (startR, startC, length) {
  const firstNumber = paper[startR][startC];

  for (let r = startR; r < startR + length; r++) {
    for (let c = startC; c < startC + length; c++) {
      if (paper[r][c] !== firstNumber) return false;
    }
  }

  return true;
};

const cutPaper = function (startR, startC, length) {
  if (isSameNumber(startR, startC, length)) {
    const number = paper[startR][startC];
    switch (number) {
      case "-1":
        negative += 1;
        return;
      case "1":
        positive += 1;
        return;
      case "0":
        zero += 1;
        return;
    }
  }

  const newLength = length / 3;
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      const newStartR = startR + newLength * i;
      const newStartC = startC + newLength * j;
      cutPaper(newStartR, newStartC, newLength);
    }
  }
};

const fs = require("fs");
let [N, ...input] = fs
  .readFileSync("./input_text/1780.txt")
  .toString()
  .split("\n");

N = +N.trim();

const paper = input.map((line) => line.trim().split(" ")); // 2차원 배열

let negative = 0; // -1로만 채워진 종이 개수
let positive = 0; // 1로만 채워진 종이 개수
let zero = 0; // 0로만 채워진 종이 개수
cutPaper(0, 0, N);

console.log(negative);
console.log(zero);
console.log(positive);

// 실행 결과: 성공(메모리:99096kb, 시간:712ms)
