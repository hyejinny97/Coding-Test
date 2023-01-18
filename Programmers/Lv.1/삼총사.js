// https://school.programmers.co.kr/learn/courses/30/lessons/131705?language=javascript
// 코딩테스트연습 < 연습문제 < 문제.삼총사



// 입력
/*
1. 한국중학교 학생들의 번호를 나타내는 정수 배열 number
- 3 <= number의 길이 <= 13
- -1,000 <= number의 각 원소 <= 1,000
- 서로 다른 학생의 정수 번호가 같은 수 있음
*/




// 출력
/*
1. 학생들 중 삼총사를 만들 수 있는 방법의 수를 return
- 삼총사: 학생 3명의 정수 번호를 더했을 때 0이 되면 3명의 학생은 삼총사
*/



// 코드 1 - 재귀함수로 조합 구현
function solution(number) {
  function findThree(numbers, people) {
    // 3명 선택 완료된 경우, 3명의 정수 합이 0이면 삼총사
    if (people.length === 3) {
      const sumThreeNums = people.reduce((acc, val) => acc + val, 0)
      if (sumThreeNums === 0) totCnt += 1
      return
    }

    // 중복되지 않게 3명 선택(조합)
    for (let i = 0; i < numbers.length; i++) {
      const newNumbers = numbers.slice(i + 1)
      findThree(newNumbers, people.concat([numbers[i]]))
    }
  }

  let totCnt = 0;
  findThree(number, [])
  return totCnt
}


// 실행 결과: 성공



// 코드 2 - 반복문으로 조합 구현
function solution(number) {
  let totCnt = 0;
  for (let fst = 0; fst < number.length; fst++) {
    for (let snd = fst + 1; snd < number.length; snd++) {
      for (let trd = snd + 1; trd < number.length; trd++) {
        // console.log(number[fst], number[snd], number[trd])
        const sumThreeNums = number[fst] + number[snd] + number[trd]
        if (sumThreeNums === 0) totCnt += 1
      }
    }
  }

  return totCnt
}


// 실행 결과: 성공