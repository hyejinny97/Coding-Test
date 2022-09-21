# 문제1258번.행렬찾기
# 시간: 20초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 수 T
2. 테스트 케이스 번호
3. n개의 줄에 n x n 행렬
- 0: 빈 용기
- 숫자: 화학물질이 들어있는 용기
'''



# 출력
'''
1. #{테스트케이스} {부분 행렬들을 개수} {부분 행렬들의 행과 열의 크기를 출력}
- 크기는 행과 열을 곱한 값으로, 크기가 작은 순서대로 출력
- 크기가 같을 경우 행이 작은 순으로 출력
'''



# 코드 
import sys

sys.stdin = open('../input_text/1258.txt')

# 부분 행렬의 (행크기, 열크기)를 반환
def dfs(start):
    N = len(matrix)   # 행렬 크기
    stack = [start]
    rows = [start[0]]   # 방문한 모든 행의 인덱스
    cols = [start[1]]   # 방문한 모든 열의 인덱스
    
    while stack:
        r, c = stack.pop()   # 현재 노드

        # 동서남북 방향으로 탐색
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] != '0':
                stack.append((nr, nc))
                matrix[nr][nc] = '0'   # 방문한 곳 체크
                rows.append(nr)
                cols.append(nc)

    return (max(rows) - min(rows) + 1, max(cols) - min(cols) + 1)



T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    matrix = [input().split() for _ in range(n)]

    # n X n 크기의 행렬을 모두 순회하면서 부분행렬 깊이우선탐색
    tot_cnt = 0   # 부분 행렬 총 갯수
    submatrix = []   # 부분행렬 (행 크기, 열 크기)
    for r in range(n):
        for c in range(n):
            if matrix[r][c] != '0':
                submatrix.append(dfs((r, c)))
                tot_cnt += 1

    # 행과 열을 곱한 값이 작은 순서대로 출력
    # 곱한 값이 같을 경우, 행이 작은 순으로 출력
    print(f'#{test_case} {tot_cnt}', end=" ")
    order = sorted(submatrix, key=lambda loc: (loc[0] * loc[1], loc[0]))
    for r, c in order:
        print(r, c, end=" ")
    print()
    


# 실행 결과: 성공(메모리:62,024 kb, 시간:170 ms)