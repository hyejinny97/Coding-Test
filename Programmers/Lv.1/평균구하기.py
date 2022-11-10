# https://school.programmers.co.kr/learn/courses/30/lessons/12944
# 코딩테스트연습 < 연습문제 < 문제.평균 구하기

# 입력
'''
1. 정수를 담고 있는 배열 arr
- 1 <= arr 길이 <= 100
- -10,000 <= 원소 <= 10,000
'''



# 출력
'''
1. 정수를 담고 있는 배열 arr의 평균값을 return
'''


# 코드 
import sys

sys.stdin = open('input_text/평균구하기.txt')

def solution(arr):
    return sum(arr) / len(arr)


# 실행 결과: 성공