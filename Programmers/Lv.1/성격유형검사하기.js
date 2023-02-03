// https://school.programmers.co.kr/learn/courses/30/lessons/118666
// 코딩테스트연습 < 2022 KAKAO TECH INTERNSHIP < 문제.성격 유형 검사하기



// 입력
/*
1. 질문마다 판단하는 지표를 담은 1차원 문자열 배열 survey
- 1 ≤ survey의 길이 ( = n) ≤ 1,000
- survey의 원소: "RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"
  - survey[i]의 첫번째 문자: '비동의' 관련 선택지를 선택하면 받는 성격 유형
  - survey[i]의 두번째 문자: '동의' 관련 선택지를 선택하면 받는 성격 유형
2. 검사자가 각 질문마다 선택한 선택지를 담은 1차원 정수 배열 choices
- choices의 길이 = survey의 길이
- choices[i]: 검사자가 선택한 i+1번째 질문의 선택지
- 1 ≤ choices의 원소 ≤ 7
  - 1(매우 비동의) ~ 7(매우 동의)
*/




// 출력
/*
1. 검사자의 성격 유형 검사 결과를 지표 번호 순서대로 return

<성격 유형 검사 방법>
- 7가지 선택지의 점수
  - 매우 동의(7), 매우 비동의(1): 3점
  - 동의(6), 비동의(2): 2점
  - 약간 동의(5), 약간 비동의(3): 1점
  - 모르겠음(4): 0점
- 모든 질문의 성격 유형 점수를 더하여 더 높은 점수를 받은 성격 유형이 검사자의 성격 유형이라고 판단
  - 단, 성격 유형 점수가 같으면 사전 순으로 빠른 것으로 판단
*/



// 코드 
function solution(survey, choices) {
  const types = {  // 성격 유형 (key:유형, value:점수)
    R: 0,
    T: 0,
    C: 0,
    F: 0,
    J: 0,
    M: 0,
    A: 0,
    N: 0
  }
  for (let i = 0; i < survey.length; i++) {
    switch (choices[i]) {
      case 1:  // 매우 비동의
        types[survey[i][0]] += 3
        break
      case 2:  // 비동의
        types[survey[i][0]] += 2
        break
      case 3:  // 약간 비동의
        types[survey[i][0]] += 1
        break
      case 5:  // 약간 동의
        types[survey[i][1]] += 1
        break
      case 6:  // 동의
        types[survey[i][1]] += 2
        break
      case 7:  // 매우 동의
        types[survey[i][1]] += 3
      default:  // 모르겠음
        break
    }
  }

  function Judge(type1, type2) {
    if (types[type1] === types[type2]) {
      return type1 > type2 ? type2 : type1
    } else if (types[type1] > types[type2]) {
      return type1
    } else {
      return type2
    }
  }

  return `${Judge('R', 'T')}${Judge('C', 'F')}${Judge('J', 'M')}${Judge('A', 'N')}`
}


// 실행 결과: 성공