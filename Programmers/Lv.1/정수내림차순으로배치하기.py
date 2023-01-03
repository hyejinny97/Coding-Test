# https://school.programmers.co.kr/learn/courses/30/lessons/12933
# 코딩테스트연습 < 연습문제 < 문제.정수 내림차순으로 배치하기



# 입력
'''
1. 정수 n
- 1 <= n <= 8,000,000,000
'''



# 출력
'''
1. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴
'''



# 코드 
import sys

sys.stdin = open('input_text/정수내림차순으로배치하기.txt')

def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))


# 실행 결과: 성공