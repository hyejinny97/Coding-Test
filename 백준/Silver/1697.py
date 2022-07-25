# https://www.acmicpc.net/problem/1697
# 문제1697.숨바꼭질
# 시간: 2초, 메모리: 128MB



# 입력
'''
1.수빈이의 위치 N, 동생의 위치 K
'''



# 출력
'''
1.수빈이가 동생을 찾는 가장 빠른 시간
- 수빈이의 위치가 X일때, 걷는다면 1초 후에 X-1/X+1로 이동, 순간이동을 한다면 1초 후에 2*X의 위치로 이동
'''



# 코드 - BFS로 X-1, X+1, 2X를 탐색해 나가기
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



# 실행 결과: 성공(메모리:54684kb, 시간:628ms)