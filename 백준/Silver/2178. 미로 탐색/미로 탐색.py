# 내 풀이
# 참고: https://wewinserv.tistory.com/m/175 

import sys
from collections import deque

def bfs(r,c):
  
  # 탐색하는 칸이 이동불가한 곳인 경우 True를 반환
  def impossible(r,c):
    if r < 0 or r >= N or c < 0 or c >= M or grid[r][c] != 1:
      return True
    return False

  # 너비우선탐색
  q = deque([[r,c]])
  while q:
    # 이동 및 방문
    r,c = q.popleft()
    # 방문한 칸이 도착 칸인 경우 탈출
    if r == N - 1 and c == M - 1:
      break
    # 현재 칸에서 동서남북 방향의 칸을 탐색하면서 이동 가능하면 q에 쌓기
    # 해당 방향으로 이동할 경우, 시작칸부터 해당칸까지의 최소이동거리가 얼마나 되는지 표시(다음칸 = 현재칸 + 1)
    if not impossible(r, c + 1):   # 동
      q.append([r, c + 1])
      grid[r][c + 1] = grid[r][c] + 1   
    if not impossible(r, c - 1):   # 서
      q.append([r, c - 1])
      grid[r][c - 1] = grid[r][c] + 1 
    if not impossible(r + 1, c):   # 남
      q.append([r + 1, c])
      grid[r + 1][c] = grid[r][c] + 1 
    if not impossible(r - 1, c):   # 북
      q.append([r - 1, c])
      grid[r - 1][c] = grid[r][c] + 1 

  return grid[N - 1][M - 1]



input = sys.stdin.readline
N, M = map(int, input().split())

# 그래프(미로) 만들기
grid = []
for _ in range(N):
  grid.append(list(map(int,input().rstrip())))

print(bfs(0,0))   # depart위치 = (0,0)