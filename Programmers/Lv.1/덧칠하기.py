# https://school.programmers.co.kr/learn/courses/30/lessons/161989
# 코딩테스트연습 < 연습문제 < 문제.덧칠하기



# 입력
'''
1. 1미터 길이의 구역 n개
2. 벽에 페인트를 칠하는 롤러의 길이는 m미터
- 1 ≤ m ≤ n ≤ 100,000
3. 다시 페인트를 칠하기로 정한 구역들의 번호가 담긴 정수 배열 section
- 1 ≤ section의 길이 ≤ n
- 1 ≤ section의 원소 ≤ n
'''



# 출력
'''
1. 롤러로 페인트칠해야 하는 최소 횟수를 return
'''



# 코드 
import sys
from collections import deque

sys.stdin = open('input_text/덧칠하기.txt')

def solution(n, m, section):
    section = deque(section)
    cnt = 0   # 롤러로 페인트칠해야 하는 최소 횟수
    while section:
        start = section[0]  # 페인트칠해야 하는 시작 구역
        while section and start <= section[0] < start + m:
            section.popleft()
        cnt += 1

    return cnt


# 실행 결과: 성공

