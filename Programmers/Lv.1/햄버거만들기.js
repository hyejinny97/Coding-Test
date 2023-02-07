// https://school.programmers.co.kr/learn/courses/30/lessons/133502
// 코딩테스트연습 < 연습문제 < 문제.햄버거 만들기



// 입력
/*
1. 재료의 정보를 나타내는 정수 배열 ingredient
- 1 ≤ ingredient의 길이 ≤ 1,000,000
- ingredient의 원소는 1, 2, 3 중 하나의 값이며, 순서대로 빵, 야채, 고기를 의미
*/




// 출력
/*
1. 상수가 포장하는 햄버거의 개수를 return

<햄버거 포장 방법>
- 정해진 순서(아래서부터, 빵 – 야채 – 고기 - 빵)로 쌓인 햄버거만 포장을 함
*/



// 코드 1

// 접근방법
/*
every() 메서드 참고: https://inpa.tistory.com/entry/JS-%F0%9F%9A%80-%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EB%B0%B0%EC%97%B4-%EA%B5%AC%EC%84%B1-%EB%B9%84%EA%B5%90%ED%95%98%EA%B8%B0
*/

function equal(arr1, arr2) {
  if (arr1.length === arr2.length) {
    return arr1.every((val, idx) => val === arr2[idx])
  }
}

function solution(ingredient) {
  const burger = [1, 2, 3, 1];
  let cnt = 0;   // 만들 수 있는 총 햄버거 개수
  while (true) {
    // 햄버거 포장 순서대로 만들기 
    let makeOne = false;   // 햄버거를 만들 수 있는지 여부
    for (let i = 0; i < ingredient.length; i++) {
      if (ingredient[i] === 1 && equal(ingredient.slice(i, i + 4), burger)) {
        cnt += 1;
        ingredient.splice(i, 4);
        makeOne = true;
        break
      }
    }

    // 더이상 햄버거를 만들 수 없으면 반복문 종료
    if (!makeOne) {
      break
    }
  }

  return cnt
}


// 실행 결과: 실패(시간초과)



// 코드 2

// 접근방법
/*
stack을 이용해서 풀이
*/

function equal(arr1, arr2) {
  if (arr1.length === arr2.length) {
    return arr1.every((val, idx) => val === arr2[idx])
  }
}

function solution(ingredient) {
  const burger = [1, 2, 3, 1];
  let cnt = 0;   // 만들 수 있는 총 햄버거 개수
  const stack = [];
  while (ingredient.length !== 0) {
    let next = ingredient.shift();
    stack.push(next);
    if (stack.length >= 4 && equal(stack.slice(-4), burger)) {
      cnt += 1;
      stack.splice(stack.length - 4, 4);
    }
  }

  return cnt
}


// 실행 결과: 실패(시간초과)



// 코드 3
function equal(arr1, arr2) {
  if (arr1.length === arr2.length) {
    return arr1.every((val, idx) => val === arr2[idx])
  }
}

function solution(ingredient) {
  const burger = [1, 2, 3, 1];
  let cnt = 0;   // 만들 수 있는 총 햄버거 개수
  const stack = [];
  while (ingredient.length !== 0) {
    let next = ingredient.shift();
    stack.push(next);
    if (stack.length >= 4 && stack[stack.length - 4] === 1 && equal(stack.slice(-4), burger)) {
      cnt += 1;
      for (let i = 0; i < 4; i++) {
        stack.pop();
      }
    }
  }

  return cnt
}


// 실행 결과: 실패(시간초과)



// 코드 4
function solution(ingredient) {
  let cnt = 0;   // 만들 수 있는 총 햄버거 개수
  const stack = [];
  while (ingredient.length !== 0) {
    let next = ingredient.shift();
    stack.push(next);
    if (stack.length >= 4 && stack[stack.length - 4] === 1) {
      const burger = stack.slice(-4).join('');
      if (burger === '1231') {
        cnt += 1;
        for (let i = 0; i < 4; i++) {
          stack.pop();
        }
      }
    }
  }

  return cnt
}


// 실행 결과: 실패(시간초과)



// 코드 5
function solution(ingredient) {
  let cnt = 0;   // 만들 수 있는 총 햄버거 개수
  const stack = [];
  for (next of ingredient) {
    stack.push(next);
    if (stack.length >= 4 && stack[stack.length - 4] === 1) {
      const burger = stack.slice(-4).join('');
      if (burger === '1231') {
        cnt += 1;
        for (let i = 0; i < 4; i++) {
          stack.pop();
        }
      }
    }
  }

  return cnt
}


// 실행 결과: 성공