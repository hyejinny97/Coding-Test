# https://school.programmers.co.kr/learn/courses/30/lessons/68645
# 코딩테스트연습 < 월간 코드 챌린지 시즌1 < 문제.삼각 달팽이



# 입력
'''
1. 밑변의 길이와 높이가 n인 삼각형
- 1 <= n <= 1,000
'''



# 출력
'''
1. 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return
'''



# 코드 
import sys

sys.stdin = open('input_text/삼각달팽이.txt')

def solution(n):
    snail = [[0] * i for i in range(1, n + 1)]
    snail[0][0] = 1
    max_num = sum(range(1, n + 1))   # 채워야 하는 숫자 최댓값

    # 반시계 방향으로 달팽이 채우기
    r, c = 0, 0  # 출발점
    dr = [1, 0, -1]  # 아래, 오른쪽, 위
    dc = [0, 1, -1]
    go = True
    while go:
        for i in range(3):
            while True:
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0 or nr >= n or nc < 0 or nc >= len(snail[nr]):
                    break
                if snail[nr][nc]:
                    break
                snail[nr][nc] = snail[r][c] + 1
                r, c = nr, nc  
        
            if snail[r][c] == max_num:
                go = not go
                break
    
    return sum(snail, [])


# 실행 결과: 성공

