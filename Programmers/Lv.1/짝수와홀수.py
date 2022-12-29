# https://school.programmers.co.kr/learn/courses/30/lessons/12937
# 코딩테스트연습 < 연습문제 < 문제.짝수와 홀수



# 입력
'''
1. 정수 num
'''



# 출력
'''
1. 정수 num이 짝수일 경우 "Even"을 반환, 홀수인 경우 "Odd"를 반환
'''



# 코드
import sys

sys.stdin = open('input_text/짝수와홀수.txt')

def solution(num):
    return 'Even' if num % 2 == 0 else 'Odd'
        

# 실행 결과: 성공