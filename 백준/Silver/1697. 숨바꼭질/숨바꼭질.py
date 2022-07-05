# 내 풀이2 - 위 풀이 정리
# BFS로 X-1, X+1, 2X를 탐색해 나가기
# 성공(메모리:, 시간:)

import sys
from collections import deque

def bfs(N,K) -> int: 
  q = deque([N]) # N이 이동가능한 위치
  visited = set()   # N이 방문한 곳
  time = 0
  while q:
    for _ in range(len(q)):
      N = q.popleft()   # 현재 N의 방문 위치
      # 수빈이가 동생을 찾은 경우
      if N == K:
        return time
      # 현재 방문한 곳 마크
      visited.add(N)
      # 현재 N위치에서 x-1, x+1, 2x위치 탐색한 후, 아직 방문하지 않은 곳이면 이동가능하므로 q에 쌓음 
      if N - 1 not in visited and 0 <= N - 1:
        q.append(N - 1)
      if N + 1 not in visited and N + 1 <= K + 1:
        q.append(N + 1)
      if 2 * N not in visited and 2 * N <= K + 1:
        q.append(2 * N)
    # 한 세대를 모두 방문하면 1초가 지남
    time += 1
  


input = sys.stdin.readline
N, K = map(int, input().split())
print(bfs(N,K))