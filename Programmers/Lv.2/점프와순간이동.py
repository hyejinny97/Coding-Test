# https://school.programmers.co.kr/learn/challenges?order=acceptance_desc&page=1&languages=python3&levels=2
# 코딩테스트연습 < Summer/Winter Coding(~2018) < 문제.점프와 순간 이동



# 입력
'''
1. 거리가 N 만큼 떨어져 있는 장소
- 1 <= N <= 1,000,000,000
'''



# 출력
'''
1. 사용해야 하는 건전지 사용량의 최솟값을 return
- K 칸을 앞으로 '점프', (현재까지 온 거리) x 2 에 해당하는 위치로 '순간이동' 가능 
- 순간이동을 하면 건전지 사용량이 줄지 않지만, 앞으로 K 칸을 점프하면 K 만큼의 건전지 사용량이 줄게 됨
'''



# 코드 1
import sys
from collections import deque

sys.stdin = open('input_text/점프와순간이동.txt')

def solution(destination):
    visited = {0:0}  # 방문한 숫자와 각 숫자에 도달하기 위한 최소 점프 수를 기록
    q = deque([0])  # 현 위치(숫자) = 새 출발점
    while True:
        now = q.popleft()
        # 점프를 최소한으로 해야하기 때문에 반드시 순간이동 먼저 고려
        if not visited.get(now * 2):  # 순간이동
            visited[now * 2] = visited[now]
            q.append(now * 2)
        if not visited.get(now + 1):  # 점프
            visited[now + 1] = visited[now] + 1
            q.append(now + 1)
        
        if visited.get(destination):
            return visited.get(destination)


# 실행 결과: 정확성 테스트 통과 / 효율성 테스트 실패(시간 초과)



# 코드 2
import sys

sys.stdin = open('input_text/점프와순간이동.txt')

def solution(N):
    jump = 0  # 점프 횟수
    while N:
        if N % 2 == 0:
            N //= 2
        else:
            jump += 1
            N -= 1

    return jump


# 실행 결과: 성공