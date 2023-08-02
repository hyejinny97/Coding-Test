// https://school.programmers.co.kr/learn/courses/30/lessons/154540
// 코딩테스트연습 < 연습문제 < 문제.무인도 여행



// 입력
/*
1. 지도를 나타내는 문자열 배열 maps
- 3 ≤ maps의 길이 ≤ 100
- 3 ≤ maps[i]의 길이 ≤ 100
- maps[i]는 'X' 또는 1 과 9 사이의 자연수로 이루어진 문자열
- 지도는 직사각형 형태
*/




// 출력
/*
1. 각 섬에서 최대 며칠씩 머무를 수 있는지 배열에 오름차순으로 담아 return
- 만약 지낼 수 있는 무인도가 없다면 -1을 배열에 담아 return
*/




// 코드 
const noAccess = 'X';

function dfs(map, curLocation) {
    const stack = [curLocation];  // 방문 가능한 곳

    const [curR, curC] = curLocation;
    let cnt = map[curR][curC];  // 머무를 수 있는 총 일수 
    map[curR][curC] = noAccess;  // 방문 체크

    while (stack.length > 0) {
        const [r, c] = stack.pop();  // 현재 방문한 곳
        
        const dr = [-1, 1, 0, 0];  // 상, 하, 좌, 우
        const dc = [0, 0, -1, 1];
        for (let i=0; i < 4; i++) {
            const nr = r + dr[i];
            const nc = c + dc[i];

            if (nr < 0 || nr >= map.length || nc < 0 || nc >= map[0].length) continue;
            if (map[nr][nc] === noAccess) continue;
            
            stack.push([nr, nc]); 
            cnt += map[nr][nc];
            map[nr][nc] = noAccess;  // 방문 체크
        }
    }

    return cnt;
}

function solution(maps) {
    const newMaps = maps.map(row => row.split('').map(val => parseInt(val) || noAccess));
    
    const answer = [];
    for (let r=0; r < newMaps.length; r++) {
        for (let c=0; c < newMaps[0].length; c++) {
            if (newMaps[r][c] === noAccess) continue;

            const stayDays = dfs(newMaps, [r, c]);
            answer.push(stayDays);
        }
    }

    return answer.length > 0 ? answer.sort((a, b) => a - b) : [-1];
}

console.log(solution(["X591X","X1X5X","X231X", "1XXX1"]))
console.log(solution(["XXX","XXX","XXX"]))
  
// 실행 결과: 성공