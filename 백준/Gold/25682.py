# https://www.acmicpc.net/problem/25682
# 문제25682번.체스판 다시 칠하기2
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 보드판 크기 N(행), M(열), 체스판 크기 K x K
- 1 ≤ N, M ≤ 2,000
- 1 ≤ K ≤ min(N, M)
2. N개의 줄에는 보드의 각 행의 상태
- B: 검은색
- W: 흰색
'''



# 출력
'''
1. N(행) x M(열) 크기의 체스판에서 K x K 크기만큼 잘라내 체스판으로 만들기 위해 다시 칠해야 하는 정사각형 개수의 최솟값을 출력
- K x K 크기 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 함
- 즉, 체스판을 색칠하는 경우는 맨 왼쪽 위 칸이 '흰색'인 경우와 '검은색'인 경우 두가지 뿐임
'''



# 코드 1
import sys

sys.stdin = open('input_text/25682.txt')

# 현재 칸을 다시 칠해야하는지 판단
def need_paint(r, c, first_color):
    if (r + c) % 2 == 0:
        if plate[r][c] == first_color: return 0
        else: return 1
    else:
        if plate[r][c] == first_color: return 1
        else: return 0

N, M, K = map(int, input().split())
plate = [input() for _ in range(N)]   # N x M 크기의 체스판 

# N x M 크기의 체스판 => 다시 칠해야하는 칸 개수 누적
acc_plate = [[[0, 0]] * (M + 1) for _ in range(N + 1)]

# 맨 왼쪽 위 칸이 B/W일 때, 각 칸을 다시 칠해야 하는지 
for r in range(1, N + 1):
    for c in range(1, M + 1):
        acc_plate[r][c] = [need_paint(r - 1, c - 1, 'B'), need_paint(r - 1, c - 1, 'W')]

# 가로 누적합
for r in range(1, N + 1):
    for c in range(1, M + 1):
        for i in range(2):
            acc_plate[r][c][i] += acc_plate[r][c - 1][i]

# 세로 누적합
for c in range(1, M + 1):
    for r in range(1, N + 1):
        for i in range(2):
            acc_plate[r][c][i] += acc_plate[r - 1][c][i]

# k x k 크기의 체스판 자르기
rst = 2000   # 다시 칠해야 하는 칸 개수 최솟값 
for r in range(K, N + 1):
    for c in range(K, M + 1):
        for i in range(2):
            rst = min(rst, acc_plate[r][c][i] - acc_plate[r - K][c][i] - acc_plate[r][c - K][i] + acc_plate[r - K][c - K][i])

print(rst)


# 실행 결과: 실패(메모리 초과)



# 코드 2
import sys

sys.stdin = open('input_text/25682.txt')

# 현재 칸을 다시 칠해야하는지 판단
def need_paint(r, c, first_color):
    if (r + c) % 2 == 0:
        if plate[r][c] == first_color: return 0
        else: return 1
    else:
        if plate[r][c] == first_color: return 1
        else: return 0

N, M, K = map(int, input().split())
plate = [sys.stdin.readline() for _ in range(N)]   # N x M 크기의 체스판 

# N x M 크기의 체스판 => 다시 칠해야하는 칸 개수 누적
acc_plate = [[0] * (M + 1) for _ in range(N + 1)]

rst = 2000   # 다시 칠해야 하는 칸 개수 최솟값 
for first in ['B', 'W']:
    # 맨 왼쪽 위 칸이 B/W일 때, 각 칸을 다시 칠해야 하는지 
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            acc_plate[r][c] = need_paint(r - 1, c - 1, first)

    # 가로 누적합
    for r in range(1, N + 1):
        for c in range(1, M + 1):
                acc_plate[r][c] += acc_plate[r][c - 1]

    # 세로 누적합
    for c in range(1, M + 1):
        for r in range(1, N + 1):
                acc_plate[r][c] += acc_plate[r - 1][c]

    # k x k 크기의 체스판 자르기
    for r in range(K, N + 1):
        for c in range(K, M + 1):
                rst = min(rst, acc_plate[r][c] - acc_plate[r - K][c] - acc_plate[r][c - K] + acc_plate[r - K][c - K])

print(rst)


# 실행 결과: 실패