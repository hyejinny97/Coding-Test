// https://school.programmers.co.kr/learn/courses/30/lessons/72411
// 코딩테스트연습 < 2021 KAKAO BLIND RECRUITMENT < 문제.메뉴 리뉴얼



// 입력
/*
1. 각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders
- 2 <= orders 배열 크기 <= 20
- 2 <= orders 원소 크기 <= 10
- 원소는 알파벳 대문자로 이루어져 있음
2. 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course
- 1 <= course 배열 크기 <= 10
- 2 <= course 원소 크기 <= 10
- 원소는 오름차순으로 정렬되어 있음
*/




// 출력
/*
1. 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return
- 코스요리 메뉴 구성을 오름차순으로 정렬해 반환해야 함
- 각 원소에 저장된 문자열 또한 오름차순 정렬되어있어야 함
- 만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return

<코스요리 메뉴 구성 조건>
- 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성
- 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성해야함
- 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함
*/




// 코드 
// 접근방법
/* 
조합 참고: https://devbirdfeet.tistory.com/271
*/

function combination(arr, k) { // nCk
  const result = [];
  if (k === 1) return arr.map(ele => [ele]);

  arr.forEach((fixedEl, idx, elements) => {
    const rst = combination(elements.slice(idx + 1), k - 1);
    const attach = rst.map(ele => [fixedEl, ...ele]);
    result.push(...attach);
  });

  return result;
}


function solution(orders, course) {
  const menuCombinations = new Map();
  course.forEach(k => {
    menuCombinations.set(k, new Map());
  })

  // 각 order마다 course에 나타난 개수만큼 각 조합을 찾은 후, 개수 카운트
  orders.forEach(order => {
    course.forEach(k => {
      const results = combination([...order].sort(), k);
      results.forEach(rst => {
        const menu = rst.join('');
        menuCombinations.get(k).set(menu, menuCombinations.get(k).get(menu) + 1 || 1);
      })
    })
  })

  const answer = [];
  course.forEach(k => {
    const menus = menuCombinations.get(k);
    const maxNum = Math.max(...menus.values());
    answer.push(...[...menus].filter(menu => menu[1] >= 2 && menu[1] === maxNum).map(menu => menu[0]));
  })

  return answer.sort();
}


// 실행 결과: 성공