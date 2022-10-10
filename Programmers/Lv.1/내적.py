# https://school.programmers.co.kr/learn/courses/30/lessons/70128#
# 코딩테스트연습 < 월간 코드 챌린지 시즌1 < 문제.내적



# 입력
'''
1. 길이가 같은 두 1차원 정수 배열 a, b
- 1 <= a,b의 길이 <= 1,000
- -1,000 <= 수 <= 1,000
'''



# 출력
'''
1. a와 b의 내적을 return
- a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1]
- (n은 a, b의 길이)
'''



# 코드
import sys

sys.stdin = open('input_text/폰켓몬.txt')

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer
        

# 실행 결과: 성공