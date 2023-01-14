// https://school.programmers.co.kr/learn/courses/30/lessons/86491
// 코딩테스트연습 < 완전탐색 < 문제.최소직사각형



// 입력
/*
1. 모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes
- 1 <= sizes 길이 <= 10,000
- sizes의 원소 = [w, h]
- 1 <= w, h <= 1,000
*/




// 출력
/*
1. 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return
*/



// 코드 1

// 접근방법
/*
1. 각 명함의 긴 변들의 길이를 구함
2. 긴 변들 중 가장 긴 변 하나를 구함 => 명합지갑의 긴 변의 길이
3. 각 명함의 짧은 변들의 길이를 구함
4. 짧은 변들 중 가장 긴 변 하나를 구함 => 명합지갑의 짧은 변의 길이
*/

function solution(sizes) {
  // 각 명함의 긴 변과 짧은 변 길이 구하기
  const cardLongList = [];
  const cardShortList = [];
  let w, h;
  for (let size of sizes) {
    w = size[0]
    h = size[1]
    cardLongList.push(Math.max(w, h))
    cardShortList.push(Math.min(w, h))
  }

  // 명합지갑의 긴 변과 짧은 변 길이 구하기
  const walletLong = Math.max(...cardLongList);
  const walletShort = Math.max(...cardShortList);

  return walletLong * walletShort
}


// 실행 결과: 성공



// 코드 2
function solution(sizes) {
  const [wallet_w, wallet_h] = sizes.reduce(
    ([acc_w, acc_h], [card_w, card_h]) => [Math.max(acc_w, Math.max(card_w, card_h)), Math.max(acc_h, Math.min(card_w, card_h))]
    , [0, 0])

  return wallet_w * wallet_h
}


// 실행 결과: 성공