// https://school.programmers.co.kr/learn/courses/30/lessons/12915?language=javascript
// 코딩테스트연습 < 연습문제 < 문제.문자열 내 마음대로 정렬하기



// 입력
/*
1. 문자열로 구성된 리스트 strings, 정수 n
- 1 <= strings 배열 길이 <= 50
- 1 <= strings 원소 길이 <= 100
- strings 원소: 소문자 알파벳으로 이루어짐
*/




// 출력
/*
1. 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬한 결과를 return
- 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치
*/



// 코드 1
function solution(strings, n) {
  strings.sort((str1, str2) => {
    if (str1[n] < str2[n]) {
      return -1
    } else if (str1[n] > str2[n]) {
      return 1
    } else {
      if (str1 < str2) {
        return -1
      } else if (str1 > str2) {
        return 1
      } else {
        return 0
      }
    }
  })

  return strings
}


// 실행 결과: 성공



// 코드 2
function solution(strings, n) {
  strings.sort((str1, str2) => {
    compare = str1.charCodeAt(n) - str2.charCodeAt(n)
    switch (compare) {
      case 0:
        if (str1 < str2) {
          return -1
        } else if (str1 > str2) {
          return 1
        } else {
          return 0
        }
      default:
        return compare
    }
  })

  return strings
}


// 실행 결과: 성공



// 코드 3

// 접근방법
/*
<String.prototype.localeCompare() 메서드>
- 참조 문자열이 정렬 순으로 지정된 문자열 앞 혹은 뒤에 오는지 또는 동일한 문자열인지 나타내는 수치를 반환
- 참고: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare
*/

function solution(strings, n) {
  strings.sort((str1, str2) => {
    if (str1[n] === str2[n]) {
      return str1.localeCompare(str2)
    }
    return str1[n].localeCompare(str2[n])
  })

  return strings
}


// 실행 결과: 성공