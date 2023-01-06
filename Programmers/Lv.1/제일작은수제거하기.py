# https://school.programmers.co.kr/learn/courses/30/lessons/12935
# 코딩테스트연습 < 연습문제 < 문제.제일 작은 수 제거하기



# 입력
'''
1. 정수를 저장한 배열 arr
- 1 <= arr 길이
'''



# 출력
'''
1. arr 에서 가장 작은 수를 제거한 배열을 리턴
- 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1
'''


# 코드
import sys

sys.stdin = open('input_text/제일작은수제거하기.txt')

def solution(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]


# 실행 결과: 성공