// https://school.programmers.co.kr/learn/courses/30/lessons/12936
// 코딩테스트연습 < 완전탐색 < 문제.줄 서는 방법



// 입력
/*
1. 사람의 수 n
- 0 < n <= 20
2. 자연수 k
- 0 < k <= n!
*/




// 출력
/*
1. 사람을 나열 하는 방법을 사전 순으로 나열 했을 때, k번째 방법을 return
*/




// 코드
const results = [];

function permutation(n, rst=[]) {
    if (rst.length === n) {
        results.push(rst);
        return
    };

    for (let x = 1; x <= n; x++) {
        if (rst.includes(x)) continue;
        permutation(n, [...rst, x])
    } 
}

function solution(n, k) {
    permutation(n);
    return results[k - 1];
}

console.log(solution(3, 5))


// 실행 결과: 실패(signal: aborted (core dumped))