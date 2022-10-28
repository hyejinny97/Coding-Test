# https://school.programmers.co.kr/learn/courses/30/lessons/70129
# 코딩테스트연습 < 월간 코드 챌린지 시즌1 < 문제.이진 변환 반복하기



# 입력
'''
1. 0과 1로 이루어진 어떤 문자열 s
- 1 <= s <= 150,000
<문자열 s에 대한 이진변환>
- s의 모든 0을 제거
- s의 길이를 c라고 하면, s를 "c를 2진법으로 표현한 문자열"로 바꿈
'''



# 출력
'''
1. s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때, 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return
'''


# 코드 
import sys

sys.stdin = open('input_text/이진변환반복하기.txt')

def solution(s): 
    cnt_0 = 0   # 제거된 0의 갯수
    cnt_conversion = 0   # 이진 변환 횟수
    while s != '1': 
        cnt = s.count('0')   # 0의 갯수
        length = len(s) - cnt   # 0 제거 후 길이
        s = format(length, 'b')   # 이진 변환 결과
        cnt_0 += cnt
        cnt_conversion += 1
    return [cnt_conversion, cnt_0]


# 실행 결과: 성공