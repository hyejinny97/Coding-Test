# https://school.programmers.co.kr/learn/courses/30/lessons/12925
# 코딩테스트연습 < 연습문제 < 문제.문자열을 정수로 바꾸기



# 입력
'''
1. 문자열 s
- 1 <= 길이 <= 5
- 맨앞에는 부호(+, -)가 올 수 있음
- "0"으로 시작하지 않음
'''



# 출력
'''
1. 문자열 s를 숫자로 변환한 결과를 반환
'''



# 코드 
import sys

sys.stdin = open('input_text/문자열을정수로바꾸기.txt')

def solution(s):
    return int(s)


# 실행 결과: 성공