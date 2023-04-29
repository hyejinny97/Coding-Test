# https://school.programmers.co.kr/learn/courses/30/lessons/42883
# 코딩테스트연습 < 탐욕법(Greedy) < 문제.큰 수 만들기



# 입력
'''
1. 문자열 형식으로 숫자 number
- 2 ≤ numbers의 길이 ≤ 1,000,000
2. 제거할 수의 개수 k
- 1 ≤ k ≤ numbers의 길이
'''



# 출력
'''
1. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return
'''



# 코드 1
import sys
from itertools import combinations

sys.stdin = open('input_text/큰수만들기.txt')

def solution(number, k):
    return ''.join(max(list(combinations(number, len(number) - k))))


# 실행 결과: 실패(시간 초과)



# 코드 2

# 접근방법
'''
가장 높은 자리수에 위치한 수가 클수록 가장 큰 수를 구할 수 있음
- (number의 개수 - k - 1)개 만큼 number 뒤에서 끊어준 후,
끊어준 위치 앞에 있는 모든 수를 비교해 가장 큰 수를 찾음
- (number의 개수 - k - 2)개 만큼 number 뒤에서 끊어준 후, 
첫번째 끊어준 위치에서 현재 끊어준 위치 앞에 있는 모든 수를 비교해 가장 큰 수를 찾음
- 위 과정을 (number의 개수 - k)번 반복
'''
import sys

sys.stdin = open('input_text/큰수만들기.txt')

def solution(number, k):
    start = 0   # 앞 순서에서 끊어준 위치 (인덱스)
    end = k   # 현재 끊어야하는 위치 (인덱스)
    rst = ''
    while end < len(number):
        max_num = '0'
        max_idx = -1
        for i in range(start, end + 1):
            if number[i] > max_num:
                max_num = number[i]
                max_idx = i
        start = max_idx + 1
        end += 1
        rst += number[max_idx]
    
    return rst


# 실행 결과: 실패(시간 초과)



# 코드 3

# 접근방법
'''
- 가장 높은 자리수에 위치한 수가 클수록 가장 큰 수를 구할 수 있음
- 참고: https://wellsw.tistory.com/m/205
'''
import sys

sys.stdin = open('input_text/큰수만들기.txt')

def solution(number, k):
    stack = []   # 만들고자하는 가장 큰 수
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    
    # 아직 제거되지 못한 숫자는 뒤에서 삭제
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)


# 실행 결과: 성공