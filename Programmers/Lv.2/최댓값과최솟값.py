# https://school.programmers.co.kr/learn/courses/30/lessons/12939
# 코딩테스트연습 < 연습문제 < 문제.최댓값과 최솟값



# 입력
'''
1. 문자열 s
- 문자열 s에는 공백으로 구분된 숫자들이 저장되어 있음
'''



# 출력
'''
1. 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환
'''


# 코드 
import sys

sys.stdin = open('input_text/최댓값과최솟값.txt')

def solution(s):
    nums = list(map(int, s.split()))
    return f'{min(nums)} {max(nums)}'


# 실행 결과: 성공