# https://school.programmers.co.kr/learn/courses/30/lessons/118667
# 코딩테스트연습 < 2022 KAKAO TECH INTERNSHIP < 문제.두 큐 합 같게 만들기

# 입력
'''
1. 길이가 같은 두 개의 큐를 나타내는 정수 배열 queue1, queue2
- 1 ≤ queue1의 길이 = queue2의 길이 ≤ 300,000
- 1 ≤ queue1의 원소, queue2의 원소 ≤ 10^9
'''



# 출력
'''
1. 각 큐의 원소 합을 같게 만들기 위해 필요한 작업의 최소 횟수를 return
- 단, 어떤 방법으로도 각 큐의 원소 합을 같게 만들 수 없는 경우, -1을 return 
'''



# 코드 
import sys
from collections import deque

sys.stdin = open('input_text/두큐합같게만들기.txt')

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    
    if (sum_q1 + sum_q2) % 2 == 1:
        return -1
    
    cnt = 0
    limit = len(queue1) * 4
    while queue1 and queue2 and cnt <= limit:
        if sum_q1 == sum_q2:
            return cnt 
        elif sum_q1 > sum_q2:
            pop_el = queue1.popleft()
            queue2.append(pop_el)
            sum_q1 -= pop_el
            sum_q2 += pop_el
        else:
            pop_el = queue2.popleft()
            queue1.append(pop_el)
            sum_q2 -= pop_el
            sum_q1 += pop_el
        cnt += 1
        
    return -1


# 실행 결과: 성공