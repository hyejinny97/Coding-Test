# https://school.programmers.co.kr/learn/courses/30/lessons/76502
# 코딩테스트연습 < 월간 코드 챌린지 시즌2 < 문제.괄호 회전하기

# 입력
'''
1. 대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s
- 1 <= s <= 1,000
'''



# 출력
'''
1. s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 

<올바른 괄호 문자열>
- (), [], {} 는 모두 올바른 괄호 문자열
- 만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열
- 만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열
'''



# 코드 
import sys
from collections import deque

sys.stdin = open('input_text/괄호회전하기.txt')

def solution(s):
    def is_correct_parentheses(parentheses):
        pair = {
            '(':')',
            '{':'}',
            '[':']'
        }
        left = []  # 왼쪽 괄호
        for p in parentheses:
            if p in ('(', '[', '{'):
                left.append(p)
            else:
                if left and pair[left[-1]] == p:
                    left.pop()
                else:
                    return False
        return not left

    cnt = 0   # 올바른 괄호 문자열 갯수
    s = deque(s)
    for _ in range(len(s)):
        if is_correct_parentheses(s):
            cnt += 1
        s.append(s.popleft())

    return cnt


# 실행 결과: 성공