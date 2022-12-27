# https://school.programmers.co.kr/learn/courses/30/lessons/12985
# 코딩테스트연습 < 2017 팁스타운 < 문제.예상 대진표



# 입력
'''
1. 게임 참가자 수 N, 참가자 번호 A, 경쟁자 번호 B
- 2^1 <= N <= 2^20
- 0 < A, B <= N
'''



# 출력
'''
1. 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 return
- 단, A번 참가자와 B번 참가자는 서로 붙게 되기 전까지 항상 이긴다고 가정
'''



# 코드 1

# 접근방법
'''
R1: 2^1명씩 묶은 후, 총 1번의 라운드 끝에 한 명의 승자가 정해짐
R2: 2^2명씩 묶은 후, 총 2번의 라운드 끝에 한 명의 승자가 정해짐
...
Rn: 2^n명씩 묶은 후, 총 n번의 라운드 끝에 한 명의 승자가 정해짐
=> 참가자 A와 참가자 B가 만나려면 둘이 일단 같이 묶여야 함
'''

import sys

sys.stdin = open('input_text/예상대진표.txt')

def solution(N,a,b):
    max_num = max(a, b)
    max_round = N // 2
    for n in range(1, max_round + 1):
        if max_num <= 2 ** n:
            return n


# 실행 결과: 부분 성공(N, a, b = 16, 9, 12인 경우 2가 아닌 4가 나옴)



# 코드 2

# 접근방법
'''
N을 2^1명씩 묶었을 때, 참가자 A와 B가 같이 묶이는 경우 => 1라운드에서 만남
N을 2^2명씩 묶었을 때, 참가자 A와 B가 같이 묶이는 경우 => 2라운드에서 만남
...
N을 2^n명씩 묶었을 때, 참가자 A와 B가 같이 묶이는 경우 => n라운드에서 만남
'''

import sys
from math import log

sys.stdin = open('input_text/예상대진표.txt')

def solution(N,a,b):
    max_round = int(log(N, 2))
    for n in range(1, max_round + 1):
        if (a - 1) // 2 ** n == (b - 1) // 2 ** n:
            return n


# 실행 결과: 성공



# 코드 3
import sys

sys.stdin = open('input_text/예상대진표.txt')

def solution(n,a,b):
    round = 0   # 경기 수
    while a != b:  
        round += 1   # 경기가 진행됨
        a, b = (a + 1) // 2, (b + 1) // 2  # 경기 결과, 참가자 A와 B는 새 번호 할당 받음

    return round


# 실행 결과: 성공