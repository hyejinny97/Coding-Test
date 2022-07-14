# 내 풀이2 - 위 풀이 정리

import sys
from collections import deque

def impossible(x, y):   # (x,y)위치로 이동 가능한지 탐색
  global l
  # 이동 불가한 경우(체스판을 벗어나는 경우, 이미 방문한 경우) True 반환
  if x < 0 or x >= l or y < 0 or y >= l or plate[x][y] == '1':
    return True
  return False


def bfs(start, goal, plate):
  q = deque([start])   # 이동가능한 좌표
  cnt = 0   # 최소 이동 횟수
  while q:
    for _ in range(len(q)):   # 현재 이동가능한 모든 위치에 순차적으로 나이트를 이동시킴
      x, y = q.popleft()   # 현재 나이트가 위치하는 좌표 
      
      # 현재 위치한 곳이 목적지인 경우 탐색 종료
      if x == goal[0] and y == goal[1]:
        return cnt
      
      # 동서남북으로 이동가능한 위치 탐색 (총 8가지 경우의 수)
      if not impossible(x - 1, y + 2):   # 동쪽으로 두칸-위로 한칸
        plate[x - 1][y + 2] = '1'   # 이동가능한 곳 마킹
        q.append([x - 1, y + 2])
      if not impossible(x + 1, y + 2):   # 동쪽으로 두칸-아래로 한칸
        plate[x + 1][y + 2] = '1'   
        q.append([x + 1, y + 2])
      if not impossible(x - 1, y - 2):   # 서쪽으로 두칸-위로 한칸
        plate[x - 1][y - 2] = '1'
        q.append([x - 1, y - 2])
      if not impossible(x + 1, y - 2):   # 서쪽으로 두칸-아래로 한칸
        plate[x + 1][y - 2] = '1'
        q.append([x + 1, y - 2])
      if not impossible(x + 2, y - 1):   # 남쪽으로 두칸-왼쪽으로 한칸
        plate[x + 2][y - 1] = '1'
        q.append([x + 2, y - 1])
      if not impossible(x + 2, y + 1):   # 남쪽으로 두칸-오른쪽으로 한칸
        plate[x + 2][y + 1] = '1'
        q.append([x + 2, y + 1])
      if not impossible(x - 2, y - 1):   # 북쪽으로 두칸-왼쪽으로 한칸
        plate[x - 2][y - 1] = '1'
        q.append([x - 2, y - 1])
      if not impossible(x - 2, y + 1):   # 북쪽으로 두칸-오른쪽으로 한칸
        plate[x - 2][y + 1] = '1'
        q.append([x - 2, y + 1])
    
    # 한세대를 모두 이동하면 1 카운트
    cnt += 1

      

T = int(input())
for _ in range(T):
  # 체스판 만들기
  l = int(input())
  plate = []   # 체스판 초기화
  for _ in range(l):
    plate.append(['0'] * l)
  #  현재 나이트 위치에서 목적지까지 이동하는데 걸리는 최소 이동 횟수 구하기
  start = list(map(int, input().split()))
  goal = list(map(int, input().split()))
  print(bfs(start, goal, plate))