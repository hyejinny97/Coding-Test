# https://www.acmicpc.net/problem/16928
# 문제16928.뱀과 사다리 게임
# 시간: 1초, 메모리: 512MB



# 입력
'''
1.사다리의 수 N, 뱀의 수 M
- 1 <= N <= 15
- 1 <= M <= 15
- 사다리를 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 큼
- 뱀을 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 작아짐
2.N개의 줄에 사다리의 정보를 의미하는 (x,y)
- x번 칸에 도착하면, y번 칸으로 이동
3.M개의 줄에 뱀의 정보를 의미하는 (u,v)
- u번 칸에 도착하면, v번 칸으로 이동 
'''



# 출력
'''
1.100번 칸에 도착하기 위해 주사위를 최소 몇 번 굴려야하는지 출력
- 1번 칸에서 시작 -> 100번 칸에 도착
'''



# 코드 - 큐를 이용한 반복구조로 bfs 풀이
import sys
from collections import deque

def bfs(start, end):
  q = deque([start])   # 현재 이동가능한 모든 위치
  cnt = 0   # 주사위를 총 몇 번 굴렸는지
  while q:
    for _ in range(len(q)):   
      loc = q.popleft()   # 현재 위치

      # 현재 위치가 100번인 경우
      if loc == end:
        return cnt

      # 현재 위치에서 주사위를 던졌을 때 나오는 모든 경우의 수만큼 이동해 탐색
      dice = [1, 2, 3, 4, 5, 6]
      for num in dice:
        next_loc = loc + num
        # 이동가능한 경우(게임판을 벗어나지 않거나 아직 탐색하지 않은 위치) 이동
        if next_loc <= 100 and not plate[next_loc]:
        
          # 탐색한 곳에 사다리나 뱀이 있는 경우 이동
          if next_loc in teleport:
            next_loc = teleport[next_loc]
  
          # 탐색한 곳을 q에 추가하고, 마킹
          q.append(next_loc)
          plate[next_loc] = 1
      
    # 한 세대를 모두 탐색한 후, 카운트 세기
    cnt += 1



N, M = map(int, sys.stdin.readline().split())   # N: 사다리수, M: 뱀의 수

# 사다리와 뱀 정보를 딕셔너리에 기록 ({출발점:도착점})
teleport = {}
for _ in range(N+M):
  start, end = map(int, sys.stdin.readline().split())
  teleport[start] = end

# 10 x 10 크기의 게임판 만들기
plate = [0] * 101

# 1번 칸에서 출발해서 100번 칸에 도달하기 위해 주사위를 최소 몇 번 굴려야하는지 출력
print(bfs(1, 100))  



# 실행 결과: 성공(메모리:32452kb, 시간:96ms)