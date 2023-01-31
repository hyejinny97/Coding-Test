// https://school.programmers.co.kr/learn/courses/30/lessons/136798
// 코딩테스트연습 < 연습문제 < 문제.기사단원의 무기



// 입력
/*
1. 기사단원의 수를 나타내는 정수 number
- 1 ≤ number ≤ 100,000
- 기사단의 각 기사에게는 1번부터 number까지 번호가 지정되어 있음
2. 이웃나라와 협약으로 정해진 공격력의 제한수치를 나타내는 정수 limit
- 2 ≤ limit ≤ 100
3. 제한수치를 초과한 기사가 사용할 무기의 공격력을 나타내는 정수 power
- 1 ≤ power ≤ limit
*/




// 출력
/*
1. 무기점의 주인이 무기를 모두 만들기 위해 필요한 철의 무게를 return
- 각 기사는 자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기를 구매
- 단, 제한수치보다 큰 공격력을 가진 무기를 구매해야 하는 기사는 협약기관에서 정한 공격력을 가지는 무기를 구매해야 함
- 무기를 만들 때, 무기의 공격력 1당 1kg의 철이 필요
*/




// 코드 
function solution(number, limit, power) {
  // 약수의 개수를 구해주는 함수
  function findDivisors(num) {
    let divisors = new Set();
    for (let n = 1; n < num ** 0.5 + 1; n++) {
      if (num % n === 0) {
        divisors.add(n);
        divisors.add(num / n);
      }
    }
    return divisors.size;
  }

  // 기사 1번부터 number번까지 약수 개수 구해서, 필요한 철의 무게 계산하기
  let ironWeight = 0;
  for (let n = 1; n < number + 1; n++) {
    const cnt = findDivisors(n);
    if (cnt > limit) {
      ironWeight += power;
    } else {
      ironWeight += cnt;
    }
  }

  return ironWeight
}


// 실행 결과: 성공