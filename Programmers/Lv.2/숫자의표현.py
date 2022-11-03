# https://school.programmers.co.kr/learn/courses/30/lessons/12924
# 코딩테스트연습 < 연습문제 < 문제.숫자의 표현



# 입력
'''
1. 자연수 n
- 0 < n <= 10,000
'''



# 출력
'''
1. 연속된 자연수들로 n을 표현하는 방법의 수를 return
'''


# 코드 
import sys

sys.stdin = open('input_text/숫자의표현.txt')

def solution(n):
    cnt = 0
    for start in range(1, n + 1):
        num = start
        sum_nums = 0
        while sum_nums < n:
            sum_nums += num
            num += 1
        if sum_nums == n:
            cnt += 1

    return cnt


# 실행 결과: 성공