# https://www.acmicpc.net/problem/7569
# 문제7569.토마토
# 시간: 1초, 메모리: 256MB



# 입력
'''
1.상자의 크기 M, N / 쌓아올려지는 상자의 수 H
- M: 상자의 가로 칸 수, 2 <= M <= 100
- N: 상자의 세로 칸 수, 2 <= N <= 100
- 1 <= H <= 100
2.가장 밑의 상자부터 가장 위의 상자까지 저장된 토마토들의 정보가 주어짐
- N개의 줄에는 하나의 상자에 담긴 토마토 정보가 주어짐
- 각 줄에는 상자 가로줄에 들어있는 M개의 토마토들 상태가 주어짐
- N개의 줄이 H번 반복하여 주어짐
- 정수1: 익은 토마토
- 정수0: 익지 않은 토마토
- 정수-1: 토마토가 들어있지 않은 칸
'''



# 출력
'''
1.토마토가 익을 때까지 최소 며칠이 걸리는지 출력
- 저장될때부터 모든 토마토가 익어있는 상태면 0 출력
- 토마토가 모두 익지 못하는 상황이면 -1 출력
'''



# 코드
import sys
from collections import deque

def bfs(riped) -> int:
  global cnt_0

  # 탐색 위치가 상자를 벗어나거나, 안익은 토마토가 없는 경우 True를 반환
  def impossible(r,c,h) -> bool:
    idx = M * r + c
    if r < 0 or r >= N or c < 0 or c >= M or h < 0 or h >= H:
      return True
    if boxs[h][idx] != 0:
      return True
    return False


  q = deque(riped)   # 익은 토마토 담기
  days = 0 # 상자들의 토마토가 모두 익는데 걸리는 시간
  while q and cnt_0:
    # 익은 토마토를 기준으로 동서남북/위아래를 탐색하며 안익은 토마토 익히기
    for _ in range(len(q)):
      h, idx = q.popleft()   # 탐색 기준(한 세대)
      r, c = idx // M, idx % M
      if not impossible(r, c + 1, h):   # 동
        boxs[h][idx + 1] = 1
        cnt_0 -= 1
        q.append([h, idx + 1])
      if not impossible(r, c - 1, h):   # 서 
        boxs[h][idx - 1] = 1
        cnt_0 -= 1
        q.append([h, idx - 1])
      if not impossible(r + 1, c, h):   # 남
        boxs[h][idx + M] = 1
        cnt_0 -= 1
        q.append([h, idx + M])
      if not impossible(r - 1, c, h):   # 북
        boxs[h][idx - M] = 1
        cnt_0 -= 1
        q.append([h, idx - M])
      if not impossible(r, c, h - 1):   # 위
        boxs[h - 1][idx] = 1
        cnt_0 -= 1
        q.append([h - 1, idx])
      if not impossible(r, c, h + 1):   # 아래
        boxs[h + 1][idx] = 1
        cnt_0 -= 1
        q.append([h + 1, idx])
    # 한 세대 토마토를 익히는데 하루 걸림
    days += 1 

  return days if cnt_0 == 0 else -1



input = sys.stdin.readline
M, N, H = map(int, input().split())

boxs = []
cnt_0 = 0   # 익지 않은 토마토 갯수
riped = []  # 상자에 최초로 담은 익은 토마토의 위치 = [H위치, idx(한 박스 내 위치)]
for h in range(H):
  box = []
  idx = 0
  for _ in range(N):
    row = list(map(int, input().split()))
    box += row     # 상자에 토마토들 담기
    for tomato in row:  
      if tomato == 0:    # 익지 않은 토마토 갯수 세기
        cnt_0 += 1
      if tomato == 1:
        riped.append([h,idx])
      idx += 1
  boxs.append(box)

print(bfs(riped))



# 실행 결과: 성공(메모리:515244kb, 시간:3080ms)