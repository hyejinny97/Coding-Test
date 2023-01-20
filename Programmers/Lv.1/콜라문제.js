// https://school.programmers.co.kr/learn/courses/30/lessons/132267
// 코딩테스트연습 < 연습문제 < 문제.콜라문제



// 입력
/*
1. 콜라를 받기 위해 마트에 주어야 하는 병 수 a, 
빈 병 a개를 가져다 주면 마트가 주는 콜라 병 수 b, 
상빈이가 가지고 있는 빈 병의 개수 n
- 1 <= b < a <= n <= 1,000,000
*/




// 출력
/*
1. 상빈이가 받을 수 있는 콜라의 병 수를 return 
- 보유 중인 빈 병이 a개 미만이면, 추가적으로 빈 병을 받을 순 없음

*/




// 코드 
function solution(a, b, n) {
  let totBottlesLeft = n;     // 남아있는 전체 콜라 병 수
  let totBottlesReceived = 0; // 받은 전체 콜라 병 수
  while (totBottlesLeft / a >= 1) {
    const bottlesReceived = Math.floor(totBottlesLeft / a) * b;
    totBottlesLeft = totBottlesLeft % a + bottlesReceived;
    totBottlesReceived += bottlesReceived;
  }
  return totBottlesReceived
}


// 실행 결과: 성공