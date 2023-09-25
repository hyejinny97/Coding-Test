// https://www.acmicpc.net/problem/1992
// 문제 1992번.쿼드트리
// 시간: 2초, 메모리: 128MB

// 입력
/*
1. 영상의 크기를 나타내는 숫자 N 
- N = 2 ^ k
- 1 <= N <= 64
2. N개의 줄마다 문자열이 N개
- 문자열: 0(흰점) 또는 1(검은점)
*/

// 출력
/* 
1. 영상을 압축한 결과를 출력

<영상 압축 방법>
- 모두 0으로만 되어 있으면, '0'으로 압축
- 모두 1으로만 되어 있으면, '1'으로 압축
- 0과 1이 섞여 있으면, 4개의 영상으로 나누어 다시 압축 시도
  - 4개의 영상으로 나누는 경우, 괄호 안에 묶어서 표현
*/

// 코드
const isSamePoint = function (startR, startC, length) {
  const firstPoint = video[startR][startC];

  for (let r = startR; r < startR + length; r++) {
    for (let c = startC; c < startC + length; c++) {
      if (video[r][c] !== firstPoint) return false;
    }
  }

  return true;
};

const compressVideo = function (startR, startC, length) {
  if (isSamePoint(startR, startC, length)) {
    rst += video[startR][startC];
    return;
  }

  const halfLength = length / 2;
  rst += "(";
  compressVideo(startR, startC, halfLength);
  compressVideo(startR, startC + halfLength, halfLength);
  compressVideo(startR + halfLength, startC, halfLength);
  compressVideo(startR + halfLength, startC + halfLength, halfLength);
  rst += ")";
};

const fs = require("fs");
let [N, ...input] = fs
  .readFileSync("./input_text/1992.txt")
  .toString()
  .split("\n");

N = +N.trim();

const video = input
  .filter((_, idx) => idx < N)
  .map((line) => line.trim().split("")); // 2차원 배열

let rst = ""; // 압축 결과
compressVideo(0, 0, N);

console.log(rst);

// 실행 결과: 성공(메모리:10480kb, 시간:176ms)
