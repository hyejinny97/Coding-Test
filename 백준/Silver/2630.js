// https://www.acmicpc.net/problem/2630
// 문제 2630번.색종이 만들기
// 시간: 1초, 메모리: 128MB

// 입력
/*
1. 전체 종이의 한 변의 길이 N
- N = 2 ^ k
- 1 <= k <= 7
2. N개의 줄마다 정사각형칸들의 색이 주어짐
- 0: 하얀색 칸
- 1: 파란색 칸
*/

// 출력
/* 
1. 잘려진 햐얀색 색종이의 개수를 출력
2. 잘려진 파란색 색종이의 개수를 출력
*/

// 코드 1
// 참고) js에서 입력값 받는 법: https://velog.io/@imysh578/%EB%B0%B1%EC%A4%80-NodeJsJavascript-%EC%9E%85%EB%A0%A5%EA%B0%92-%EB%B0%9B%EB%8A%94-%EB%B0%A9%EB%B2%95

/*
// 같은 색깔인지 확인
function isSameColors(paper) {
  const firstColor = paper[0][0];

  for (const line of paper) {
    for (const color of line) {
      if (color !== firstColor) return false;
    }
  }

  return true;
}

// 4등분으로 자르기
function cutQuarters(paper) {
  const rowLength = paper.length;
  const colLength = paper[0].length;

  const q1 = paper
    .filter((_, idx) => idx < rowLength / 2)
    .map((row) => row.slice(0, colLength / 2));

  const q2 = paper
    .filter((_, idx) => idx < rowLength / 2)
    .map((row) => row.slice(colLength / 2));

  const q3 = paper
    .filter((_, idx) => idx >= rowLength / 2)
    .map((row) => row.slice(0, colLength / 2));

  const q4 = paper
    .filter((_, idx) => idx >= rowLength / 2)
    .map((row) => row.slice(colLength / 2));

  return [q1, q2, q3, q4];
}

// 색종이 만들기
const WHITE = "0";
const BLUE = "1";
let whitePaper = 0;
let bluePaper = 0;
function makeColorPaper(paper) {
  if (isSameColors(paper) || paper.length === 1) {
    paper[0][0] === WHITE ? (whitePaper += 1) : (bluePaper += 1);
    return;
  }

  const [q1, q2, q3, q4] = cutQuarters(paper);
  makeColorPaper(q1);
  makeColorPaper(q2);
  makeColorPaper(q3);
  makeColorPaper(q4);
}

const fs = require("fs");
const [N, ...input] = fs
  .readFileSync("./input_text/2630.txt")
  .toString()
  .split("\n");

const paper = input
  .filter((_, idx) => idx < N)
  .map((line) => line.trim().split(" ")); // 2차원 배열

makeColorPaper(paper);
console.log(whitePaper);
console.log(bluePaper);
*/

// 실행 결과: 성공(메모리:18180kb, 시간:300ms)

// 코드 2

// 같은 색깔인지 확인
function isSameColors(startR, startC, length) {
  const firstColor = paper[startR][startC];

  for (let r = startR; r < startR + length; r++) {
    for (let c = startC; c < startC + length; c++) {
      if (paper[r][c] !== firstColor) return false;
    }
  }

  return true;
}

// 색종이 만들기 (start = paper 시작점, length = paper 한변 길이)
function makeColorPaper(startR, startC, length) {
  if (isSameColors(startR, startC, length)) {
    const WHITE = "0";
    paper[startR][startC] === WHITE ? (whitePaper += 1) : (bluePaper += 1);
    return;
  }

  const newLength = length / 2;
  const quarters = [
    [startR, startC, newLength],
    [startR, startC + newLength, newLength],
    [startR + newLength, startC, newLength],
    [startR + newLength, startC + newLength, newLength],
  ];
  for (const quarter of quarters) {
    makeColorPaper(...quarter);
  }
}

const fs = require("fs");
let [N, ...input] = fs
  .readFileSync("./input_text/2630.txt")
  .toString()
  .split("\n");

N = +N.trim();

const paper = input
  .filter((_, idx) => idx < N)
  .map((line) => line.trim().split(" ")); // 2차원 배열

let whitePaper = 0;
let bluePaper = 0;
makeColorPaper(0, 0, N);

console.log(whitePaper);
console.log(bluePaper);

// 실행 결과: 성공(메모리:12500kb, 시간:192ms)
