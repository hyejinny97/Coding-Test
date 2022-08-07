# 문제1954번.달팽이 숫자
# 시간: 30초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 달팽이 크기 N
- 1 <= N <= N
'''



# 출력
'''
1. #{테스트케이스}
2. {N x N 크기의 달팽이}
- 달팽이는 1부터 N x N까지의 숫자가 시계방향으로 이루어져 있음
'''



# 접근방법
'''
1. N x N의 이차원 배열 만들기
2. 1부터 N까지 반복문을 돌기
----------------------------------------------
<N까지 반복문을 다 돌때까지 아래 과정을 반복>
1) (N - 1)번 숫자 넣기
2) 90도 오른쪽 회전
3) 1번과 2번을 총 4번 반복
4) (N - 3)번 숫자 넣기
5) 90도 오른쪽 회전
6) 4번과 5번을 총 4번 반복
----------------------------------------------
3. N = 홀수인 경우, 마지막은 하나의 숫자만 넣어주면 됨
'''



# 코드 1
import sys

sys.stdin = open('../input_text/1954.txt')

T = int(input())
for test_case in range(1, T + 1):
    # N x N 크기의 달팽이집 만들기
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    
    # 달팽이집에 시계방향으로 숫자 넣기
    num = 1
    n = 0
    start = row = 0
    while num <= N * N:
        # N = 홀수인 경우
        if N % 2 == 1 and num == N * N:
            snail[row][start] = num
            break

        # 90도 회전 x 4번
        for _ in range(4):
            # 네바퀴마다 각각 N-1, N-3, N-5...번만큼 열에 숫자 넣기
            for c in range(start, start + (N - (2 * n + 1))):
                snail[row][c] = num
                num += 1
            # 오른쪽으로 90도 회전
            rotated_snail = [[0] * N for _ in range(N)]
            for c in range(N):
                for r in range(N):
                    rotated_snail[c][r] = snail[r][N - c - 1]
            snail = rotated_snail

        row += 1
        start += 1
        n += 1
    
    # snail 출력
    print(f'#{test_case}')
    for row in snail:
        print(*row)
    


# 실행 결과: 성공(메모리:56,920 kb, 시간:145ms)



# 코드 2
import sys

sys.stdin = open('../input_text/1954.txt')

def create_snail(grid, N, num, r, c):
    # 시작위치 숫자 넣기
    grid[r][c] = num 
    
    while num < N * N:
        # 동남서북 총 네방향으로 숫자 넣기
        dr = [0, 1, 0, -1]   # 동남서북
        dc = [1, 0, -1, 0]
        for i in range(4):
            while True:
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0 or nr >= N or nc < 0 or nc >= N or grid[nr][nc] != 0:
                    break
                num += 1
                grid[nr][nc] = num
                r, c = nr, nc
        
    return grid     



T = int(input())
for test_case in range(1, T + 1):
    # N x N 크기의 달팽이집 만들기
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    
    # snail 출력
    print(f'#{test_case}')
    snail = create_snail(snail, N, 1, 0, 0)
    for row in snail:
        print(*row)



# 실행 결과: 성공(메모리:56,920 kb, 시간:134ms)