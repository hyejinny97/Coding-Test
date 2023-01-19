# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 코딩테스트연습 < 스택/큐 < 문제.프린터



# 입력
'''
1. 현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities,
내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location
- 1 <= 대기목록에 있는 문서 개수 <= 100
- 1 <= 인쇄 작업의 중요도(클수록 중요함) <= 9
- 0 <= location <= (대기목록에 있는 작업 수 - 1)
'''



# 출력
'''
1. 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return

<프린터의 인쇄 작업>
1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 꺼냄
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣음
3. 그렇지 않으면 J를 인쇄함
'''


# 코드
import sys
from collections import deque

sys.stdin = open('input_text/프린터.txt')

def solution(priorities, location):
    q = deque(enumerate(priorities))
    order = 0   # 작업 순서
    while q:
        max_priority = max(q, key=lambda priority: priority[1])   # 작업들 중 가장 높은 중요도
        while q[0][1] < max_priority[1]:
            q.append(q.popleft())
        
        order += 1
        if q[0][0] == location:
            return order
        q.popleft()

    return order


# 실행 결과: 성공