# https://school.programmers.co.kr/learn/courses/30/lessons/87389
# 코딩테스트연습 < 월간 코드 챌린지 시즌3 < 문제.나머지가 1이 되는 수 찾기



# 입력
'''
1. 자연수 n
- 3 <= n <= 1,000,000
'''



# 출력
'''
1. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return
'''



# 코드 
import sys

sys.stdin = open('input_text/나머지가1이되는수찾기.txt')

def solution(n):
    for num in range(1, n + 1):
        if n % num == 1:
            return num


# 실행 결과: 성공