# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# 코딩테스트연습 < 2017 팁스타운 < 문제.짝지어 제거하기



# 입력
'''
1. 문자열 s
- s의 길이 <= 1,000,000 
- s는 모두 소문자로 이루어짐
'''



# 출력
'''
1. 문자열을 모두 제거할 수 있으므로 1을 반환, 아니면 0을 반환
- 같은 알파벳 2개를 제거한 후, 이어붙이는 과정을 반복
'''


# 코드 1
import sys

sys.stdin = open('input_text/짝지어제거하기.txt')

def solution(s):
    while s:
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                s = s[:i - 1] + s[i + 1:]
                break
        else:
            break

    return 0 if s else 1


# 실행 결과: 실패(시간초과)



# 코드 2
import sys

sys.stdin = open('input_text/짝지어제거하기.txt')

def solution(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        if s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])

    return 0 if stack else 1


# 실행 결과: 실패(런타임에러)



# 코드 3
import sys

sys.stdin = open('input_text/짝지어제거하기.txt')

def solution(s):
    # 문자가 홀수이면 완전 제거 불가
    if len(s) % 2 == 1:
        return 0

    stack = [s[0]]
    for i in range(1, len(s)):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])

    return 0 if stack else 1


# 실행 결과: 성공