# 문제13732번.정사각형 판정
# 시간: 3초, 메모리: 256MB


# 입력
"""
1. 테스트 케이스 T
2. 격자판 크기 N
- 1 <= N <= 20
3. N개의 줄에 '.'과 '#'으로 구성된 N개만큼의 문자열
- 모든 격자판에는 최소 1개 이상의 ‘#’ 칸이 있음
"""


# 출력
"""
1. #{테스트케이스} {격자판의 막혀 있는 칸들이 하나의 정사각형을 이루면 ‘yes’, 그렇지 않다면 ‘no’}
"""


# 코드 1 - 문제를 잘못 읽음(격자판 내 모든 #이 하나의 정사각형을 이루어야 함)
import sys

sys.stdin = open("../input_text/13732.txt")


def check_square(r, c):
    N = len(matrix)
    dr = [0, 1, 1]  # 오른쪽, 아래, 우측아래
    dc = [1, 0, 1]
    for i in range(3):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= N or nc >= N or matrix[nr][nc] != "#":
            return False
    return True


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # N x N 크기의 격자판
    matrix = [input() for _ in range(N)]

    # 격자판을 순회하면서 '#'이 있는 칸 오른쪽, 아래, 우측아래에 모두 '#'이 있으면 yes
    rst = "no"
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == "#" and check_square(r, c):
                rst = "yes"
            # 불필요한 순회 방지
            if rst == "yes":
                break
        # 불필요한 순회 방지
        if rst == "yes":
            break

    print(f"#{test_case} {rst}")


# 실행 결과: 실패(테스트케이스 20개 중 6개 통과)


# 코드 2
import sys
from pprint import pprint

sys.stdin = open("../input_text/13732.txt")


def dfs(start):
    N = len(matrix)
    matrix[start[0]][start[1]] = "."  # 시작 위치 방문체크
    stack = [start]
    while stack:
        r, c = stack.pop()  # 현재 위치

        # 오른쪽, 아래 탐색
        dr = [0, 1]  # 오른쪽, 아래
        dc = [1, 0]
        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < N and nc < N and matrix[nr][nc] == "#":
                stack.append((nr, nc))
                matrix[nr][nc] = "."  # 방문체크


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # N x N 크기의 격자판
    matrix = [list(input()) for _ in range(N)]

    # 격자판을 순회
    cnt = 0  # 정사각형(#의 모음) 갯수
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == "#":
                dfs((r, c))
                cnt += 1

    # 격자판의 막혀 있는 칸들이 하나의 정사각형을 이루는지 확인
    if cnt == 1:
        rst = "yes"
    else:
        rst = "no"

    print(f"#{test_case} {rst}")


# 실행 결과: 실패(테스트케이스 20개 중 13개 통과)


# 코드 3
import sys

sys.stdin = open("../input_text/13732.txt")


def check_square():
    # locations의 모든 # 위치가 첫번째 #과 마지막 # 사이에 존재하는지 확인
    fst = locations[0]
    last = locations[-1]
    for loc in locations:
        # 행 확인
        if fst[0] > loc[0] or loc[0] > last[0]:
            return False
        # 열 확인
        if fst[1] > loc[1] or loc[1] > last[1]:
            return False

    # 첫번째 #과 마지막 # 사이가 모두 #인지 확인
    for r in range(fst[0], last[0] + 1):
        for c in range(fst[1], last[1] + 1):
            if matrix[r][c] != "#":
                return False

    return True


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # N x N 크기의 격자판
    matrix = [list(input()) for _ in range(N)]

    # 격자판을 순회하면서 #의 위치(인덱스) 기록
    locations = []
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == "#":
                locations.append((r, c))

    # 격자판의 막혀 있는 칸들이 하나의 정사각형을 이루면 ‘yes’
    if check_square():
        rst = "yes"
    else:
        rst = "no"

    print(f"#{test_case} {rst}")


# 실행 결과: 실패(테스트케이스 20개 중 15개 통과)


# 코드 4
import sys

sys.stdin = open("../input_text/13732.txt")


def check_square():
    # 제곱근이 정수가 아니면 정사각형이 이루어질 수 있는 개수가 아님
    square_length = len(locations) ** 0.5
    if square_length % 1 != 0:
        return "no"

    # 첫번째 #과 마지막 # 사이가 모두 #인지 확인
    fst = locations[0]
    for r in range(fst[0], fst[0] + int(square_length)):
        for c in range(fst[1], fst[1] + int(square_length)):
            if matrix[r][c] != "#":
                return "no"

    return "yes"


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # N x N 크기의 격자판
    matrix = [list(input()) for _ in range(N)]

    # 격자판을 순회하면서 #의 위치(인덱스) 기록
    locations = []
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == "#":
                locations.append((r, c))

    # 격자판의 막혀 있는 칸들이 하나의 정사각형을 이루면 ‘yes’
    rst = check_square()

    print(f"#{test_case} {rst}")


# 실행 결과: 성공(메모리:61,632 kb, 시간:146 ms)
