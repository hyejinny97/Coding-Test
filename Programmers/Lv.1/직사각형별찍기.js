// https://school.programmers.co.kr/learn/courses/30/lessons/12969
// 코딩테스트연습 < 연습문제 < 문제.직사각형 별찍기



// 입력
/*
1. 두 개의 정수 n과 m
- 0 < n, m <= 1,000
*/




// 출력
/*
1. 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력
*/


// 코드 1
process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
  const n = data.split(" ");
  const a = Number(n[0]), b = Number(n[1]);
  for (i = 0; i < b; i++) {
    console.log('*'.repeat(a))
  }
});


// 실행 결과: 성공



// 코드 2
process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
  const n = data.split(" ");
  const a = Number(n[0]), b = Number(n[1]);
  console.log(('*'.repeat(a) + '\n').repeat(b))
});


// 실행 결과: 성공