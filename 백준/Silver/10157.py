# https://www.acmicpc.net/problem/10157
# 문제10157번.자리배정
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 격자 크기 세로 C, 가로 R
- 5 <= C, R <= 1,000
2. 대기번호 K
- 1 <= K <= 100,000,000
'''



# 출력
'''
1. 대긴번호 K인 관객에게 배정될 좌석번호 (x,y) 출력
- 만일 해당 대기번호의 관객에게 좌석을 배정할 수 없는 경우엔 0을 출력
- 좌석은 시계방향 달팽이 모양으로 순차적으로 배정됨
'''



# 코드
import sys
from pprint import pprint

sys.stdin = open('input_text/10157.txt')

def find_loc(col, row, num):
    r, c = 0, 0
    n = 1
    matrix[r][c] = n   # 시작위치
    
    while n <= num:
        # 방향 벡터
        dr = [1, 0, -1, 0]   # 남서북동
        dc = [0, -1, 0, 1]   
        for i in range(4):
            while True:
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < row and 0 <= nc < col and not matrix[nr][nc]:
                    n += 1
                    matrix[nr][nc] = n 
                    r, c = nr, nc
                else:
                    break
                # 대기번호 K인 관객의 좌석 위치 반환
                if n == num:
                    return (c + 1, r + 1)


# 2차원 리스트로 C x R 크기의 공연장 만들기
col, row = map(int, input().split())
num = int(input())
matrix = []
for _ in range(row):
    matrix.append([0] * col)

# 대기번호 K인 관객의 좌석 위치 출력
if num > col * row:
    print(0)
elif num == 1:
    print(1, 1)
else:
    print(*find_loc(col, row, num))



# 실행 결과: 성공(메모리:64832kb, 시간:424ms)