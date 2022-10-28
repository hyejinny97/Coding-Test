# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 코딩테스트연습 < 스택/큐 < 문제.올바른 괄호



# 입력
'''
1. '(' 또는 ')' 로만 이루어진 문자열 s
- 0 < 문자열 길이 <= 100,000
'''



# 출력
'''
1. 문자열 s가 올바른 괄호이면 true를 return, 올바르지 않은 괄호이면 false를 return
'''


# 코드 
import sys

sys.stdin = open('input_text/올바른괄호.txt')

def solution(s):
    stack = []
    for par in s:
        if par == '(':
            stack.append('(')
        else:
            if not stack or stack.pop() != '(':
                return False
    
    if not stack:
        return True
    else:
        return False


# 실행 결과: 성공