# https://school.programmers.co.kr/learn/courses/30/lessons/86051
# 코딩테스트연습 < 월간 코드 챌린지 시즌3 < 문제.없는 숫자 더하기



# 입력
'''
1. 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers
- 1 ≤ numbers의 길이 ≤ 9
- 0 ≤ numbers의 모든 원소 ≤ 9
- numbers의 모든 원소는 서로 다름
'''



# 출력
'''
1. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return
'''


# 코드
import sys

sys.stdin = open('input_text/없는숫자더하기.txt')

def solution(numbers):
    result = sum(range(0, 9 + 1))
    tot_sum = sum(numbers)
    return result - tot_sum


# 실행 결과: 성공