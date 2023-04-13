# https://school.programmers.co.kr/learn/courses/30/lessons/172928
# 코딩테스트연습 < 연습문제 < 문제.공원산책



# 입력
'''
1. 공원을 나타내는 문자열 배열 park
- 3 ≤ park의 길이 ≤ 50
- 3 ≤ park[i]의 길이 ≤ 50
- S : 시작 지점
- O : 이동 가능한 통로
- X : 장애물
2. 로봇 강아지가 수행할 명령이 담긴 문자열 배열 routes
- 1 ≤ routes의 길이 ≤ 50
- routes: "이동할방향(op) 이동할칸수(n)"
- 이동할 방향: 동(E), 서(W), 남(S), 북(N)
- 1 <= 이동할 칸 수 <= 9
'''



# 출력
'''
1. 로봇 강아지가 모든 명령을 수행 후 놓인 위치를 [세로 방향 좌표, 가로 방향 좌표] 순으로 배열에 담아 return
- 주어진 방향으로 이동할 때 공원을 벗어나거나, 장애물을 만나면 로봇은 해당 명령을 무시하고 다음 명령을 수행
'''



# 코드 
import sys

sys.stdin = open('input_text/공원산책.txt')

def solution(park, routes):
    # 로봇의 시작 위치 찾기
    now = []   # 현재 위치
    for r in range(len(park)):
        for c in range(len(park[0])):
            if park[r][c] == 'S':
                now += [r, c]
                break
        if now:
            break

    # 로봇 이동시키기
    directions = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}
    for route in routes:
        op, n = route.split()
        for cnt in range(1, int(n) + 1):
            dr, dc = directions[op][0] * int(cnt), directions[op][1] * int(cnt)
            nr, nc = now[0] + dr, now[1] + dc
            if nr < 0 or nr >= len(park) or nc < 0 or nc >= len(park[0]):
                break
            if  park[nr][nc] == 'X':
                break
        else:
            now[0], now[1] = nr, nc

    return now


# 실행 결과: 성공

