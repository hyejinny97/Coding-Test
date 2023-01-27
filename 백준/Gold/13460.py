# https://www.acmicpc.net/problem/13460
# 문제13460번.구슬 탈출2
# 시간: 2초, 메모리: 512MB



# 입력
'''
1. 보드의 세로 크기 N, 가로 크기 M
- 3 <= N, M <= 10
2. N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열
- 문자열은 '.', '#', 'O', 'R', 'B'로 이루어짐
- '.'(빈칸), '#'(공이 이동할 수 없는 장애물), 'o'(구멍), 'R'(빨간구슬), 'B'(파란구슬)
- 모든 보드의 가장자리에는 모두 '#'이 있음
- 구멍, 빨간 구슬, 파란 구슬 개수는 각각 1개
- 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없음
'''



# 출력
'''
1. 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력
- 만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력
- 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 함
- 왼쪽/오른쪽/위쪽/아래쪽으로 기울이기와 같은 네 가지 동작이 가능
- 파란 구슬이 구멍에 들어가면 실패
- 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패
'''





# 코드 1

# 접근방법
'''
참고: https://rebas.kr/724
'''

import sys
from collections import deque

sys.stdin = open('input_text/13460.txt')

def bfs(board, visited, init_blue, init_red):
    q = deque([[init_blue, init_red, 0]])   # [파란 구슬 위치, 빨간 구슬 위치, 구슬 이동 횟수] 모음
    visited[init_red[0]][init_red[1]] = True  # 빨간 구슬 방문 체크
    while q:
        blue, red, moves = q.popleft()   # 현재 파란 구슬과 빨간 구슬의 위치
        
        if moves > 10:
            break

        # 동서남북 방향으로 빨간 구슬과 파란 구슬을 동시에 이동시킴
        dr = [0, 0, 1, -1]  # 동서남북
        dc = [1, -1, 0, 0]
        for i in range(4):
            # 파란 구슬 - 지정한 방향으로 최대한 갈 수 있는 만큼 이동 시키기
            blue_goal = False
            blue_distance = 0
            blue_r, blue_c = blue[0], blue[1]
            while board[blue_r + dr[i]][blue_c + dc[i]] != '#':
                # 구슬 이동
                blue_r += dr[i]
                blue_c += dc[i]
                blue_distance += 1
                # 다음 위치로 이동한 구슬이 구멍을 통과하는지
                if board[blue_r][blue_c] == 'O':
                    blue_goal = True

            # 빨간 구슬 - 지정한 방향으로 최대한 갈 수 있는 만큼 이동 시키기
            red_goal = False
            red_distance = 0
            red_r, red_c = red[0], red[1]
            while board[red_r + dr[i]][red_c + dc[i]] != '#':
                # 구슬 이동
                red_r += dr[i]
                red_c += dc[i]
                red_distance += 1
                # 다음 위치로 이동한 구슬이 구멍을 통과하는지
                if board[red_r][red_c] == 'O':
                    red_goal = True

            # 구슬이 구멍을 통과했는지 
            if blue_goal or red_goal:
                return moves + 1 if red_goal and not blue_goal else -1

            # 두 구슬이 한 곳에서 만난 경우
            if blue_r == red_r and blue_c == red_c:
                if blue_distance > red_distance:
                    blue_r -= dr[i]
                    blue_c -= dc[i]
                else:
                    red_r -= dr[i]
                    red_c -= dc[i]

            # 현재 두 구슬의 최종 위치 추가
            if not visited[red_r][red_c]:
                visited[red_r][red_c] = True    # 빨간 구슬 방문 체크
                q.append([[blue_r, blue_c], [red_r, red_c], moves + 1])
                
    return -1


# 보드 세로 크기 N, 가로 크기 M과 보드판 입력 받기
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 빨간 구슬, 파란 구슬, 구멍 각각의 위치 찾기
blue, red = None, None
for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            blue = [i, j]
        elif board[i][j] == 'R':
            red = [i, j]

print(bfs(board, visited, blue, red))


# 실행 결과: 실패 - 7% (이유: 파란공이 먼저 빠지는 경우, -1이 출력됨)
'''
반례) ans : 10

10 10
##########
#RB....#.#
#..#.....#
#........#
#.O......#
#...#....#
#........#
#........#
#.......##
##########
'''





# 코드 2
import sys
from collections import deque

sys.stdin = open('input_text/13460.txt')

def bfs(board, visited_red, visited_blue, init_blue, init_red):
    q = deque([[init_blue, init_red, 0]])   # [파란 구슬 위치, 빨간 구슬 위치, 구슬 이동 횟수] 모음
    visited_red[init_red[0]][init_red[1]] = True  # 빨간 구슬 방문 체크
    visited_blue[init_blue[0]][init_blue[1]] = True  # 파란 구슬 방문 체크
    while q:
        blue, red, moves = q.popleft()   # 현재 파란 구슬과 빨간 구슬의 위치
        # print('------------------------------------')
        # print(f'현재 blue: {blue}, 현재 red: {red}, 현재 moves: {moves}')
        if moves > 10:
            break

        # 동서남북 방향으로 빨간 구슬과 파란 구슬을 동시에 이동시킴
        dr = [0, 0, 1, -1]  # 동서남북
        dc = [1, -1, 0, 0]
        for i in range(4):
            # print(f'동서남북 방향: {i}')

            # 파란 구슬 - 지정한 방향으로 최대한 갈 수 있는 만큼 이동 시키기
            blue_goal = False
            blue_distance = 0
            blue_r, blue_c = blue[0], blue[1]
            while board[blue_r + dr[i]][blue_c + dc[i]] != '#':
                # 구슬 이동
                blue_r += dr[i]
                blue_c += dc[i]
                blue_distance += 1
                # 다음 위치로 이동한 구슬이 구멍을 통과하는지
                if board[blue_r][blue_c] == 'O':
                    blue_goal = True

            # 빨간 구슬 - 지정한 방향으로 최대한 갈 수 있는 만큼 이동 시키기
            red_goal = False
            red_distance = 0
            red_r, red_c = red[0], red[1]
            while board[red_r + dr[i]][red_c + dc[i]] != '#':
                # 구슬 이동
                red_r += dr[i]
                red_c += dc[i]
                red_distance += 1
                # 다음 위치로 이동한 구슬이 구멍을 통과하는지
                if board[red_r][red_c] == 'O':
                    red_goal = True

            # 구슬이 구멍을 통과했는지 
            if blue_goal:
                continue
            if red_goal:
                return moves + 1

            # 두 구슬이 한 곳에서 만난 경우
            if blue_r == red_r and blue_c == red_c:
                if blue_distance > red_distance:
                    blue_r -= dr[i]
                    blue_c -= dc[i]
                else:
                    red_r -= dr[i]
                    red_c -= dc[i]

            # 현재 두 구슬의 최종 위치 추가
            if not visited_red[red_r][red_c] or not visited_blue[blue_r][blue_c]:
                # print(f'{[[blue_r, blue_c], [red_r, red_c], moves + 1]} 추가됨')
                visited_red[red_r][red_c] = True    # 빨간 구슬 방문 체크
                visited_blue[blue_r][blue_c] = True    # 파란 구슬 방문 체크
                q.append([[blue_r, blue_c], [red_r, red_c], moves + 1])
                
    return -1


# 보드 세로 크기 N, 가로 크기 M과 보드판 입력 받기
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited_red = [[False] * M for _ in range(N)]
visited_blue = [[False] * M for _ in range(N)]

# 빨간 구슬, 파란 구슬, 구멍 각각의 위치 찾기
blue, red = None, None
for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            blue = [i, j]
        elif board[i][j] == 'R':
            red = [i, j]

print(bfs(board, visited_red, visited_blue, blue, red))


# 실행 결과: 실패 - 26% (이유: 아래 테스트에서 -1이 뜸)
'''
반례) 7

8 8
########
#.####.#
#...#B##
#.##.R.#
######.#
##.##O.#
###.##.#
########
'''





# 코드 3
import sys
from collections import deque

sys.stdin = open('input_text/13460.txt')

def bfs(board, init_blue, init_red):
    q = deque([[init_blue, init_red, 0]])   # [파란 구슬 위치, 빨간 구슬 위치, 구슬 이동 횟수] 모음
    visited = set((init_blue, init_red))  # 두 구슬 방문 체크
    while q:
        blue, red, moves = q.popleft()   # 현재 파란 구슬과 빨간 구슬의 위치
        # print('------------------------------------')
        # print(f'현재 blue: {blue}, 현재 red: {red}, 현재 moves: {moves}')
        if moves > 10:
            break

        # 동서남북 방향으로 빨간 구슬과 파란 구슬을 동시에 이동시킴
        dr = [0, 0, 1, -1]  # 동서남북
        dc = [1, -1, 0, 0]
        for i in range(4):
            # print(f'동서남북 방향: {i}')

            # 파란 구슬 - 지정한 방향으로 최대한 갈 수 있는 만큼 이동 시키기
            blue_goal = False
            blue_distance = 0
            blue_r, blue_c = blue[0], blue[1]
            while board[blue_r + dr[i]][blue_c + dc[i]] != '#':
                # 구슬 이동
                blue_r += dr[i]
                blue_c += dc[i]
                blue_distance += 1
                # 다음 위치로 이동한 구슬이 구멍을 통과하는지
                if board[blue_r][blue_c] == 'O':
                    blue_goal = True

            # 빨간 구슬 - 지정한 방향으로 최대한 갈 수 있는 만큼 이동 시키기
            red_goal = False
            red_distance = 0
            red_r, red_c = red[0], red[1]
            while board[red_r + dr[i]][red_c + dc[i]] != '#':
                # 구슬 이동
                red_r += dr[i]
                red_c += dc[i]
                red_distance += 1
                # 다음 위치로 이동한 구슬이 구멍을 통과하는지
                if board[red_r][red_c] == 'O':
                    red_goal = True

            # 구슬이 구멍을 통과했는지 
            if blue_goal:
                continue
            if red_goal:
                return moves + 1

            # 두 구슬이 한 곳에서 만난 경우
            if blue_r == red_r and blue_c == red_c:
                if blue_distance > red_distance:
                    blue_r -= dr[i]
                    blue_c -= dc[i]
                else:
                    red_r -= dr[i]
                    red_c -= dc[i]

            # 현재 두 구슬의 최종 위치 추가
            if ((blue_r, blue_c), (red_r, red_c)) not in visited:
                # print(f'{[(blue_r, blue_c), (red_r, red_c), moves + 1]} 추가됨')
                visited.add(((blue_r, blue_c), (red_r, red_c)))  # 두 구슬 방문 체크
                q.append([(blue_r, blue_c), (red_r, red_c), moves + 1])
                
    return -1


# 보드 세로 크기 N, 가로 크기 M과 보드판 입력 받기
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

# 빨간 구슬, 파란 구슬, 구멍 각각의 위치 찾기
blue, red = None, None
for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            blue = (i, j)
        elif board[i][j] == 'R':
            red = (i, j)

print(bfs(board, blue, red))


# 실행 결과: 실패 - 63% (이유: 아래 테스트에서 11이 뜸)
'''
반례) ans = -1

11 13
#############
#.RB#########
#.#.........#
#.#.#######.#
#.#.#.....#.#
#.#.#..O#.#.#
#.#.#####.#.#
#.#.......#.#
#.#########.#
#...........#
#############
'''





# 코드 4
import sys
from collections import deque

sys.stdin = open('input_text/13460.txt')

def bfs(board, init_blue, init_red):
    q = deque([[init_blue, init_red, 0]])   # [파란 구슬 위치, 빨간 구슬 위치, 구슬 이동 횟수] 모음
    visited = set((init_blue, init_red))  # 두 구슬 방문 체크
    while q:
        blue, red, moves = q.popleft()   # 현재 파란 구슬과 빨간 구슬의 위치

        if moves > 10:
            break

        # 동서남북 방향으로 빨간 구슬과 파란 구슬을 동시에 이동시킴
        dr = [0, 0, 1, -1]  # 동서남북
        dc = [1, -1, 0, 0]
        for i in range(4):
            # 파란 구슬 - 지정한 방향으로 최대한 갈 수 있는 만큼 이동 시키기
            blue_goal = False
            blue_distance = 0
            blue_r, blue_c = blue[0], blue[1]
            while board[blue_r + dr[i]][blue_c + dc[i]] != '#':
                # 구슬 이동
                blue_r += dr[i]
                blue_c += dc[i]
                blue_distance += 1
                # 다음 위치로 이동한 구슬이 구멍을 통과하는지
                if board[blue_r][blue_c] == 'O':
                    blue_goal = True

            # 빨간 구슬 - 지정한 방향으로 최대한 갈 수 있는 만큼 이동 시키기
            red_goal = False
            red_distance = 0
            red_r, red_c = red[0], red[1]
            while board[red_r + dr[i]][red_c + dc[i]] != '#':
                # 구슬 이동
                red_r += dr[i]
                red_c += dc[i]
                red_distance += 1
                # 다음 위치로 이동한 구슬이 구멍을 통과하는지
                if board[red_r][red_c] == 'O':
                    red_goal = True

            # 구슬이 구멍을 통과했는지 
            if blue_goal:
                continue
            if red_goal:
                return moves + 1 if moves + 1 <= 10 else -1

            # 두 구슬이 한 곳에서 만난 경우
            if blue_r == red_r and blue_c == red_c:
                if blue_distance > red_distance:
                    blue_r -= dr[i]
                    blue_c -= dc[i]
                else:
                    red_r -= dr[i]
                    red_c -= dc[i]

            # 현재 두 구슬의 최종 위치 추가
            if ((blue_r, blue_c), (red_r, red_c)) not in visited:
                visited.add(((blue_r, blue_c), (red_r, red_c)))  # 두 구슬 방문 체크
                q.append([(blue_r, blue_c), (red_r, red_c), moves + 1])
                
    return -1


# 보드 세로 크기 N, 가로 크기 M과 보드판 입력 받기
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

# 빨간 구슬, 파란 구슬, 구멍 각각의 위치 찾기
blue, red = None, None
for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            blue = (i, j)
        elif board[i][j] == 'R':
            red = (i, j)

print(bfs(board, blue, red))


# 실행 결과: 성공(메모리: 34324KB, 시간: 64ms)