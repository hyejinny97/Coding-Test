# https://school.programmers.co.kr/learn/courses/30/lessons/12922
# 코딩테스트연습 < 연습문제 < 문제.수박수박수박수박수박수?



# 입력
'''
1. 길이가 n
- n의 길이 <= 10,000
'''



# 출력
'''
1. "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴
'''



# 코드 
import sys

sys.stdin = open('input_text/수박수박.txt')

def solution(n):
    return '수박' * (n // 2) + '수' * (n % 2)


# 실행 결과: 성공