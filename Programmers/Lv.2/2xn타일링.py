# https://school.programmers.co.kr/learn/courses/30/lessons/12900
# 코딩테스트연습 < 연습문제 < 문제.2 x n 타일링



# 입력
'''
1. 직사각형의 가로의 길이 n
- 0 < n <= 60,000
'''



# 출력
'''
1. 직사각형을 채우는 방법의 수를 1,000,000,007으로 나눈 나머지를 return

<타일을 채우는 방법>
- 타일을 가로로 배치 하는 경우
- 타일을 세로로 배치 하는 경우
'''


# 코드 1

# 접근방법 
'''
가로로 배치한 타일(horizontal tile) 2개 ⋉ n = 2 
세로로 배치한 타일(vertical tile) 1개 ⋉ n = 1

<n = 4인 경우, 타일을 채우는 방법>
1) hor_tile * 2 + ver_tile * 0 👉 2C2 = 1 (hor_tile이 위치할 수 있는 경우의 수)
2) hor_tile * 1 + ver_tile * 2 👉 3C1 = 3
3) hor_tile * 0 + ver_tile * 4 👉 4C0 = 1

<보충설명>
hor_tile * 1 + ver_tile * 2인 경우,
_ _ _ 여기 세 칸 중에 hor_tile이 한 곳에 위치할 수 있는 경우의 수는 
3C1 = 3 이다

<n= 5인 경우, 타일을 채우는 방법>
1) hor_tile * 2 + ver_tile * 1 👉 3C2 = 3
2) hor_tile * 1 + ver_tile * 3 👉 4C1 = 4
3) hor_tile * 0 + ver_tile * 5 👉 5C0 = 1
'''
import sys

sys.stdin = open('input_text/2xn타일링.txt')

def combination(n, m) -> int:  # nCm
    if n // 2 < m:
        m = n - m
    
    rst = 1
    for num in range(n, n - m, -1): # 분자
        rst *= num
    for num in range(1, m + 1): # 분모
        rst //= num
    return rst

def solution(n):
    cnt = 0  # 타일을 채우는 방법의 수
    for hor_tile in range(0, n // 2 + 1):  # 가로 타일 개수
        ver_title = n - hor_tile * 2  # 세로 타일 개수 
        cnt += combination(hor_tile + ver_title, hor_tile)

    return cnt % 1000000007


# 실행 결과: 실패(일부 TC 시간 초과)



# 코드 2
import sys
from math import comb

sys.stdin = open('input_text/2xn타일링.txt')

def solution(n):
    cnt = 0  # 타일을 채우는 방법의 수
    for hor_tile in range(0, n // 2 + 1):  # 가로 타일 개수
        ver_title = n - hor_tile * 2  # 세로 타일 개수 
        cnt += comb(hor_tile + ver_title, hor_tile)

    return cnt % 1000000007


# 실행 결과: 실패(일부 TC 시간 초과)



# 코드 3

# 접근방법
'''
n = 1인 경우, 타일을 채우는 방법 = 1
n = 2인 경우, 타일을 채우는 방법 = 2
n = 3인 경우, 타일을 채우는 방법 = 3
n = 4인 경우, 타일을 채우는 방법 = 5
n = 5인 경우, 타일을 채우는 방법 = 8
...
=> 피보나치 수열을 만족
  n  0 1 2 3 4 5 6  7  8  ...
F(n) 1 1 2 3 5 8 13 21 34 ...
     a b
       a b
'''
import sys

sys.stdin = open('input_text/2xn타일링.txt')

def solution(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b

    return b % 1000000007


# 실행 결과: 성공