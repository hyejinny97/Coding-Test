// https://www.acmicpc.net/problem/2740
// 문제 2740번.행렬 곱셈
// 시간: 1초, 메모리: 128MB

// 입력
/*
1. 행렬 A의 크기 N(행) 과 M(열)
2. N개의 줄에 행렬 A의 원소 M개
3. 행렬 B의 크기 M(행)과 K(열)
4. M개의 줄에 행렬 B의 원소 K개
- 0 < N, M, K <= 100
- -100 <= 행렬의 원소 <= 100
*/

// 출력
/* 
1. N개의 줄에 행렬 A와 B를 곱한 행렬을 출력
- 행렬의 각 원소는 공백으로 구분한다.
*/

// 코드
// 두 1차원 배열을 곱하는 함수
const multiplyArrays = function (arr1, arr2) {
  let rst = 0;
  for (let i = 0; i < arr1.length; i++) {
    rst += arr1[i] * arr2[i];
  }
  return rst;
};

// 두 2차원 배열을 곱하는 함수
const multiply2DArrays = function (arr1, arr2) {
  const newArray = [];
  const newArrayRow = arr1.length;
  const newArrayCol = arr2[0].length;

  for (let r = 0; r < newArrayRow; r++) {
    const row = [];
    for (let c = 0; c < newArrayCol; c++) {
      row.push(
        multiplyArrays(
          arr1[r],
          arr2.map((arrRow) => arrRow[c])
        )
      );
    }
    newArray.push(row);
  }

  return newArray;
};

const fs = require("fs");
const input = fs.readFileSync("./input_text/2740.txt").toString().split("\n");

let N, M, K;
const arrA = [];
const arrB = [];
for (let idx = 0; idx < input.length; idx++) {
  const trimRow = input[idx].trim().split(" ").map(Number);
  if (idx === 0) {
    [N, M] = trimRow;
    continue;
  }

  if (idx === N + 1) {
    K = trimRow[1];
    continue;
  }

  if (1 <= idx && idx <= N) {
    arrA.push(trimRow);
    continue;
  }

  arrB.push(trimRow);
}

const arr = multiply2DArrays(arrA, arrB);
console.log(arr.map((c) => c.join(" ")).join("\n"));

// 실행 결과: 성공(메모리:12736kb, 시간208ms)
