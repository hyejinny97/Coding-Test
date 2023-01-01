# https://school.programmers.co.kr/learn/courses/30/lessons/12934
# 코딩테스트연습 < 연습문제 < 문제.정수 제곱근 판별



# 입력
'''
1. 임의의 양의 정수 n
- 1 <= n <= 50000000000000
'''



# 출력
'''
1. n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴, x의 제곱이 아니라면 -1을 리턴
'''



# 코드 1
import sys

sys.stdin = open('input_text/정수제곱근판별.txt')

def solution(n):
    square_root = n ** 0.5
    if square_root == int(square_root):
        return (int(square_root) + 1) ** 2
    return -1


# 실행 결과: 성공



# 코드 2
import sys
from math import sqrt

sys.stdin = open('input_text/정수제곱근판별.txt')

def solution(n):
    return -1 if sqrt(n) % 1 else (sqrt(n) + 1) ** 2

# 실행 결과: 성공