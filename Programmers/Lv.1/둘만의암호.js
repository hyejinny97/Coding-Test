// https://school.programmers.co.kr/learn/courses/30/lessons/155652
// 코딩테스트연습 < 연습문제 < 문제.둘만의 암호



// 입력
/*
1. 두 문자열 s와 skip, 그리고 자연수 index
- 5 ≤ s의 길이 ≤ 50
- 1 ≤ skip의 길이 ≤ 10
- s와 skip은 알파벳 소문자로만 이루어져 있음
- skip에 포함되는 알파벳은 s에 포함되지 않음
- 1 ≤ index ≤ 20
*/




// 출력
/*
1. 암호 규칙에 따라 s를 변환한 결과를 return

<암호 규칙>
- 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿔줘야 함
- index만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아감
- skip에 있는 알파벳은 제외하고 건너뜀
*/




// 코드 1
function solution(s, skip, index) {
  // 알파벳 소문자 26개에서 skip에 있는 알파벳 제거
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  let newAlphabet = '';
  for (let char of alphabet) {
    if (!skip.includes(char)) {
      newAlphabet += char
    }
  }

  // 암호 규칙에 따라 s를 변환
  let newS = '';
  for (let char of s) {
    const idx = (newAlphabet.indexOf(char) + index) % newAlphabet.length
    newS += newAlphabet[idx]
  }

  return newS
}


// 실행 결과: 성공



// 코드 2
function solution(s, skip, index) {
  // 알파벳 소문자 26개에서 skip에 있는 알파벳 제거
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  let newAlphabet = alphabet.match(new RegExp(`[^${skip}]`, 'g'));

  // 암호 규칙에 따라 s를 변환
  let newS = '';
  for (let char of s) {
    const idx = (newAlphabet.indexOf(char) + index) % newAlphabet.length
    newS += newAlphabet[idx]
  }

  return newS
}


// 실행 결과: 성공