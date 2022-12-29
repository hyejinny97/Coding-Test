# https://school.programmers.co.kr/learn/courses/30/lessons/12931
# 코딩테스트연습 < 연습문제 < 문제.자릿수 더하기



# 입력
'''
1. 자연수 N
- 0 < N <= 100,000,000 
'''



# 출력
'''
1. N의 각 자릿수의 합을 구해서 return
'''



# 코드 1
import sys

sys.stdin = open('input_text/자릿수더하기.txt')

def solution(N):
    answer = 0
    for n in str(N):
        answer += int(n)

    return answer
        

# 실행 결과: 성공



# 코드 2
import sys

sys.stdin = open('input_text/자릿수더하기.txt')

def solution(N):
    answer = 0
    while N:
        answer += N % 10
        N //= 10

    return answer
        

# 실행 결과: 성공