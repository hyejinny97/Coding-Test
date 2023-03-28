# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 코딩테스트연습 < 깊이/너비 우선 탐색(DFS/BFS) < 문제.게임 맵 최단거리



# 입력
'''
1. 게임 맵의 상태 maps
- n x m 크기의 2차원 배열
- 1 <= n, m <= 100
- 0: 벽이 있는 자리
- 1: 벽이 없는 자리
- 처음에 캐릭터는 (1, 1) 위치, 상대방 진영은 (n, m) 위치에 있음
'''



# 출력
'''
1. 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return
- 단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 
'''


# 코드 1
import sys
from collections import deque

sys.stdin = open('input_text/게임맵최단거리.txt')

def solution(maps):
    def bfs(matrix, start, target):
        q = deque([start]) # 캐릭터가 이동 가능한 칸
        blocks = 0 # 캐릭터가 지난 칸의 개수의 최솟값
        while q:
            for _ in range(len(q)):
                r, c = q.popleft() # 캐릭터가 현재 위치하는 칸
                
                # 지나온 길 체크
                matrix[r][c] = 0  

                # 상대 팀 진영에 도착한 경우
                if r == target[0] and c == target[1]:
                    return blocks + 1

                # 동서남북 방향으로 이동 가능한지 확인
                dr = [0, 0, 1, -1] # 동서남북
                dc = [1, -1, 0, 0]
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    
                    # maps 범위를 벗어난 경우
                    if nr < 0 or nr >= len(matrix) or nc < 0 or nc >= len(matrix[0]):
                        continue
                    
                    # 벽이 있는 경우
                    if matrix[nr][nc] == 0:
                        continue
                    
                    q.append((nr, nc))
            
            blocks += 1
        
        return -1

    return bfs(maps, (0,0), (len(maps) - 1, len(maps[0]) - 1)) 


# 실행 결과: 실패(정확성  테스트 = 통과, 효율성  테스트 = 실패(시간 초과))



# 코드 2

# 접근방법
'''
https://school.programmers.co.kr/questions/23794
'''
import sys
from collections import deque

sys.stdin = open('input_text/게임맵최단거리.txt')

def bfs(matrix, start, target):
    q = deque([start]) # 캐릭터가 이동 가능한 칸
    blocks = 0 # 캐릭터가 지난 칸의 개수의 최솟값
    while q:
        for _ in range(len(q)):
            r, c = q.popleft() # 캐릭터가 현재 위치하는 칸

            # 상대 팀 진영에 도착한 경우
            if r == target[0] and c == target[1]:
                return blocks + 1

            # 동서남북 방향으로 이동 가능한지 확인
            dr = [0, 0, 1, -1] # 동서남북
            dc = [1, -1, 0, 0]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                
                # maps 범위를 벗어난 경우
                if nr < 0 or nr >= len(matrix) or nc < 0 or nc >= len(matrix[0]):
                    continue
                
                # 벽이 있는 경우
                if matrix[nr][nc] == 0:
                    continue
                
                matrix[nr][nc] = 0   # 지나간 길 체크
                q.append((nr, nc))        
        blocks += 1
    
    return -1


def solution(maps):
    # 상대 진영을 정복할 수 있는지 먼저 확인
    tar_r, tar_c = (len(maps) - 1, len(maps[0]) - 1)  
   
    if 0 <= tar_r < len(maps) and 0 <= tar_c - 1 < len(maps[0]) and maps[tar_r][tar_c - 1]: # 상대 진영의 서쪽
        return bfs(maps, (0,0), (tar_r, tar_c))
   
    if 0 <= tar_r - 1 < len(maps) and 0 <= tar_c < len(maps[0]) and maps[tar_r - 1][tar_c]:  # 상대 진영의 북쪽
        return bfs(maps, (0,0), (tar_r, tar_c))

    return -1


# 실행 결과: 성공