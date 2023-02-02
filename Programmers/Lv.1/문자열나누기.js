// https://school.programmers.co.kr/learn/courses/30/lessons/140108
// 코딩테스트연습 < 연습문제 < 문제.문자열 나누기



// 입력
/*
1. 문자열 s
- 1 ≤ s의 길이 ≤ 10,000
- 영어 소문자로만 이루어짐
*/




// 출력
/*
1. 문자열들로 분해하고, 분해한 문자열의 개수를 return

<문자열 분해 방식>
- 첫 글자를 x라고 지정
- 왼쪽에서 오른쪽으로 읽어나가면서, x와 x가 아닌 다른 글자들이 나온 횟수를 각각 센다
- 처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리
- s에서 분리한 문자열을 빼고 남은 부분에 대해서 이 과정을 반복
*/



// 코드 
function solution(s) {
  const stack = [];
  let cnt = 0;  // 첫 글자 카운트
  for (let char of s) {
    if (stack.length === 0) {  // 첫글자 지정
      stack.push(char)
      cnt += 1
    } else if (stack[0] === char) {  // 첫글자와 동일한 글자인 경우 추가
      stack.push(char)
    } else {  // 첫글자와 다른 글자인 경우 제거
      stack.pop()
    }
  }

  return cnt
}
console.log(solution("banana"))
console.log(solution("abracadabra"))
console.log(solution("aaabbaccccabba"))

// 실행 결과: 성공