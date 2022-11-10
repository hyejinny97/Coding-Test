# https://school.programmers.co.kr/learn/courses/30/lessons/12932
# 코딩테스트연습 < 연습문제 < 문제.자연수 뒤집어 배열로 만들기

# 입력
'''
1. 자연수 n
- 0 < n <= 10,000,000,000
'''



# 출력
'''
1. 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴
'''


# 코드 
import sys

sys.stdin = open('input_text/자연수뒤집어배열로만들기.txt')

def solution(n):
    return [int(num) for num in str(n)[::-1]]


# 실행 결과: 성공