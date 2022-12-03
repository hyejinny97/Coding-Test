# https://school.programmers.co.kr/learn/courses/30/lessons/12911
# 코딩테스트연습 < 연습문제 < 문제.다음 큰 숫자

# 입력
'''
1. 자연수 n
- n <= 1,000,000
'''



# 출력
'''
1. n의 다음 큰 숫자
<n의 다음 큰 숫자 조건>
1) n보다 큰 자연수
2) n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같음
3) n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수
'''


# 코드 
import sys

sys.stdin = open('input_text/다음큰숫자.txt')

def solution(n):
    n_binary_cnt = str(format(n, 'b')).count('1')  # 2진수 변환된 n의 1 갯수
    next = n + 1
    while True:
        if str(format(next, 'b')).count('1') == n_binary_cnt:
            return next
        next += 1


# 실행 결과: 성공