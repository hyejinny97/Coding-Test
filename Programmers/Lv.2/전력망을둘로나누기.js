// https://school.programmers.co.kr/learn/courses/30/lessons/86971
// 코딩테스트연습 < 완전 탐색 < 문제.전력망을 둘로 나누기

// 입력
/*
1. 송전탑의 개수 n, 그리고 전선 정보 wires
- 2 <= n <= 100
- wires: 길이가 (n-1)인 정수형 2차원 배열
- wires 각 원소: [v1, v2] 2개의 자연수로, 전력망의 v1번 송전탑과 v2번 송전탑이 전선으로 연결되어 있다는 것을 의미
- 1 ≤ v1 < v2 ≤ n
*/

// 출력
/*
1. 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때, 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return
*/

// 코드 1
// function solution(n, wires) {
//   let minDiff = 100; // 두 전력망이 가지고 있는 송전탑 개수의 차이 최솟값

//   wires.forEach((_, cutLineIdx) => {
//     // 하나의 전선 끊기
//     const restWires = [
//       ...wires.slice(0, cutLineIdx),
//       ...wires.slice(cutLineIdx + 1),
//     ];

//     // 두 전력망이 갖게 되는 각각의 송전탑 개수 구하기
//     const firstTowerGroup = new Set([]);
//     const secondTowerGroup = new Set([]);
//     restWires.forEach((wire, idx) => {
//       const [tower1, tower2] = wire;
//       if (idx === 0) return firstTowerGroup.add(tower1).add(tower2);

//       if (firstTowerGroup.has(tower1) || firstTowerGroup.has(tower2))
//         return firstTowerGroup.add(tower1).add(tower2);
//       else return secondTowerGroup.add(tower1).add(tower2);
//     });

//     minDiff = Math.min(
//       minDiff,
//       Math.abs(firstTowerGroup.size - secondTowerGroup.size)
//     );
//   });

//   return minDiff;
// }

// const inputs = require("fs")
//   .readFileSync("./input_text/전력망을둘로나누기.txt")
//   .toString()
//   .trim()
//   .split("\n");

// const testCase = inputs.length;
// Array(testCase)
//   .fill(null)
//   .forEach((_, idx) => {
//     const [n, wires] = inputs[idx].trim().split(" ");

//     console.log(
//       solution(
//         +n,
//         wires.match(/\d,\d/g).map((val) => val.split(",").map(Number))
//       )
//     );
//   });

// 실행 결과: 실패(TC 6,7번만 정답) 👉 이유: https://school.programmers.co.kr/questions/20942

// 코드 2
// 참고: https://school.programmers.co.kr/questions/53200
function solution(n, wires) {
  let minDiff = 100; // 두 전력망이 가지고 있는 송전탑 개수의 차이 최솟값

  // 전력망 (양방향) 그래프 만들기
  const connect = {};
  wires.forEach(([tower1, tower2]) => {
    connect[tower1]
      ? connect[tower1].push(tower2)
      : (connect[tower1] = [tower2]);
    connect[tower2]
      ? connect[tower2].push(tower1)
      : (connect[tower2] = [tower1]);
  });

  wires.forEach((cutWire, _) => {
    // 두 전력망이 갖게 되는 각각의 송전탑 개수 구하기
    const firstTower = cutWire[0]; // 시작점
    const visited = new Set([firstTower]); // 방문한 타워
    const stack = [firstTower]; // 체크해야할 타워
    while (stack.length) {
      const targetTower = stack.pop();
      const connectTowers = connect[targetTower];

      connectTowers.forEach((tower) => {
        if (cutWire.includes(targetTower) && cutWire.includes(tower)) return;
        if (!visited.has(tower)) stack.push(tower);
        visited.add(tower);
      });
    }

    // 두 전력망의 송전탑 개수 차이 구하기
    const firstTowerGroupCnt = visited.size;
    const secondTowerGroupCnt = n - visited.size;
    minDiff = Math.min(
      minDiff,
      Math.abs(firstTowerGroupCnt - secondTowerGroupCnt)
    );
  });

  return minDiff;
}

const inputs = require("fs")
  .readFileSync("./input_text/전력망을둘로나누기.txt")
  .toString()
  .trim()
  .split("\n");

const testCase = inputs.length;
Array(testCase)
  .fill(null)
  .forEach((_, idx) => {
    const [n, wires] = inputs[idx].trim().split(" ");

    console.log(
      solution(
        +n,
        wires.match(/\d,\d/g).map((val) => val.split(",").map(Number))
      )
    );
  });

// 실행 결과: 성공
