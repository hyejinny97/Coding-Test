// https://school.programmers.co.kr/learn/courses/30/lessons/12926
// 코딩테스트연습 < 연습문제 < 문제.시저 암호



// 입력
/*
1. 문자열 s, 거리 n
- 공백은 아무리 밀어도 공백
- s는 알파벳 소문자, 대문자, 공백으로만 이루어짐
- 0 < s <= 8,000
- 1 <= n <= 25
*/




// 출력
/*
1. s를 n만큼 민 암호문을 만들어 반환
<시저 암호>
- 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식
*/


// 코드 1
function solution(s, n) {
  // 문자열 -> 유니코드
  unicodes = [];
  for (let i = 0; i < s.length; i++) {
    if (s[i] === ' ') {
      movedCode = 32
    } else if (s[i] === 'z') {
      movedCode = 97 + (n - 1)
    } else if (s[i] === 'Z') {
      movedCode = 65 + (n - 1)
    } else {
      unicode = s.charCodeAt(i)
      movedCode = unicode + n
    }
    unicodes.push(movedCode)
  }

  // 유니코드 -> 문자열
  let answer = '';
  for (let unicode of unicodes) {
    answer += String.fromCharCode(unicode)
  }
  return answer
}


// 실행 결과: 실패(s="bC" n=25인경우, "{\"가 나옴)



// 코드 2
function solution(s, n) {
  // 문자열 -> 유니코드
  const unicodes = [];
  for (let i = 0; i < s.length; i++) {
    let unicode = s.charCodeAt(i)
    let movedCode;
    if (unicode === 32) {  // 공백인 경우
      movedCode = 32
    } else if (65 <= unicode && unicode <= 90 && (unicode + n) > 90) {  // 대문자
      movedCode = 65 + (unicode + n) % 90 - 1
    } else if (97 <= unicode && unicode <= 122 && (unicode + n) > 122) {  // 소문자
      movedCode = 97 + (unicode + n) % 122 - 1
    } else {
      movedCode = unicode + n
    }
    unicodes.push(movedCode)
  }

  // 유니코드 -> 문자열
  let answer = '';
  for (let unicode of unicodes) {
    answer += String.fromCharCode(unicode)
  }
  return answer
}


// 실행 결과: 성공



// 코드 3
function solution(s, n) {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  let answer = '';
  for (let i = 0; i < s.length; i++) {
    if (s[i] === ' ') {  // 공백인 경우
      answer += ' '
    } else if (s[i].toLowerCase() === s[i]) {  // 소문자인 경우
      let idx = (s[i].charCodeAt(0) - 97 + n) % 26
      answer += alphabet[idx]
    } else {  // 대문자인 경우
      let idx = (s[i].toLowerCase().charCodeAt(0) - 97 + n) % 26
      answer += alphabet[idx].toUpperCase()
    }
  }
  return answer
}


// 실행 결과: 성공



// 코드 4
function solution(s, n) {
  let answer = '';
  let unicode, movedCode;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === ' ') {  // 공백인 경우
      answer += ' '
      continue
    }

    unicode = s[i].charCodeAt(0)
    if (s[i].charCodeAt(0) >= 97) {  // 소문자인 경우
      movedCode = (s[i].charCodeAt(0) - 97 + n) % 26 + 97
    } else {  // 대문자인 경우
      movedCode = (s[i].charCodeAt(0) - 65 + n) % 26 + 65
    }
    answer += String.fromCharCode(movedCode)
  }
  return answer
}


// 실행 결과: 성공