# 문제4615번.재밌는 오셀로 게임
# 시간: 4초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 수 T
2. 보드의 한 변의 길이 N, 플레이어가 돌을 놓는 횟수 M
- N은 4, 6, 8 중 하나
3. M개 줄에 돌을 놓을 위치, 돌의 색
- 1: 흑돌, 2: 백돌
'''



# 출력
'''
1. #{테스트케이스} {게임이 끝난 후 보드 위의 흑돌, 백돌의 개수}
- 처음에 플레이어는 다음과 같이 돌을 놓고 시작
- 자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을 경우에만 그 곳에 돌을 놓을 수 있고, 그 때의 상대편의 돌은 자신의 돌로 만들 수 있음
- 여기에서 "사이"란 가로/세로/대각선을 의미
'''



# 코드
import sys
from pprint import pprint

sys.stdin = open('../input_text/4615.txt')

def check(start, player):
    N = len(board)

    # (x, y) 위치에 자신의 돌 놓기
    start_c, start_r = start
    board[start_r][start_c] = player

    # 좌, 우, 대각선 방향을 탐색하면서 상대편 돌 뒤집기
    # 왼 오 위 아래 좌측위 좌측아래 우측위 우측아래
    dr = [0, 0, -1, 1, -1, 1, -1, 1]   
    dc = [-1, 1, 0, 0, -1, -1, 1, 1]
    for i in range(8):
        path = []
        r, c = start_r, start_c
        while True:
            nr = r + dr[i]
            nc = c + dc[i]
            # 탐색한 곳이 범위를 벗어나거나 0인 경우
            if nr < 0 or N <= nr or nc < 0 or N <= nc or board[nr][nc] == 0:
                break
            # 지나온 길 체크
            path.append((nr, nc))
            # 자신의 돌을 만나면 지나온 길 모두 자신의 돌 색깔로 바꾸기
            if board[nr][nc] == player:
                for r, c in path:
                    board[r][c] = player
                break
            r, c = nr, nc



T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    # N x N 크기의 보드판
    board = [[0] * (N + 1) for _ in range(N + 1)]

    # 처음에 플레이어는 다음과 같이 돌을 놓고 시작
    board[N // 2][N // 2] = 2
    board[N // 2 + 1][N // 2 + 1] = 2
    board[N // 2][N // 2 + 1] = 1
    board[N // 2 + 1][N // 2] = 1
    
    # 번갈아가며 흑, 백 플레이어가 돌을 놓음
    for m in range(M):
        c, r, player = map(int, input().split())
        # 자신의 돌을 놓고 주위의 상대방 돌을 바꾸기
        check((c, r), player)
    
    # 게임이 끝난 후 흑돌, 백돌의 갯수 출력
    black = 0
    white = 0
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if board[r][c] == 1:
                black += 1
            elif board[r][c] == 2:
                white += 1
    
    print(f'#{test_case} {black} {white}')


# 실행 결과: 성공(메모리:62,364 kb, 시간:206 ms)