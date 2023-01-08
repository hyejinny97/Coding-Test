# https://school.programmers.co.kr/learn/courses/30/lessons/12918
# 코딩테스트연습 < 연습문제 < 문제.문자열 다루기 기본



# 입력
'''
1. 문자열 s
- 1 <= s <= 8
- 영문 알파벳 대소문자 또는 0부터 9까지 숫자로 이루어져 있음
'''



# 출력
'''
1. 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있으면 true 리턴
'''



# 코드 
import sys

sys.stdin = open('input_text/문자열다루기기본.txt')

def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()


# 실행 결과: 성공