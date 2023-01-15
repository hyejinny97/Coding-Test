// https://school.programmers.co.kr/learn/courses/30/lessons/17681
// 코딩테스트연습 < 2018 KAKAO BLIND RECRUITMENT < 문제.[1차] 비밀지도



// 입력
/*
1. 지도의 한 변 크기 n, 2개의 정수 배열 arr1과 arr2
- 1 <= n <= 16
- arr1, arr2는 길이 n인 정수 배열로 주어짐
- 정수 배열의 각 원소 x를 이진수로 변환했을 때의 길이 <= n
*/




// 출력
/*
1. 원래의 비밀지도를 해독하여 '#', 공백으로 구성된 문자열 배열로 출력

<지도 암호 해독 방법>
- 지도 = 한 변의 길이가 n인 정사각형 배열 형태
- "공백"(" ") 또는 "벽"("#") 두 종류로 이루어짐
- 전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있음
- 전체 지도에서 벽 = 지도 1 또는 지도 2 중 어느 하나라도 벽인 경우
- 전체 지도에서 공백 = 지도 1과 지도 2에서 모두 공백인 경우
- 지도는 정수 배열로 암호화되어 있음
- 암호화된 배열 = 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열
*/




// 코드 
function solution(n, arr1, arr2) {
  // 2개의 지도 만들기
  const map1 = [];
  const map2 = [];
  for (let i = 0; i < n; i++) {
    let bin1 = arr1[i].toString(2);
    let bin2 = arr2[i].toString(2);
    map1.push('0'.repeat(n - bin1.length) + bin1);
    map2.push('0'.repeat(n - bin2.length) + bin2);
  }

  // 2개 지도의 암호를 해독해 전체 지도 만들기
  const finalMap = [];
  for (let r = 0; r < n; r++) {
    let row = '';
    for (let c = 0; c < n; c++) {
      if (Number(map1[r][c]) || Number(map2[r][c])) {  // 하나라도 벽이면 벽
        row += '#';
      } else {  // 둘 다 공백이면 공백
        row += ' ';
      }
    }
    finalMap.push(row);
  }

  return finalMap
}


// 실행 결과: 성공