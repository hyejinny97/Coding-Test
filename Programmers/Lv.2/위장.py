# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# 코딩테스트연습 < 해시 < 문제.위장



# 입력
'''
1. 스파이가 가진 의상들이 담긴 2차원 배열 clothes
- clothes의 각 행 = [의상의 이름, 의상의 종류]
- 1 <= 스파이가 가진 의상의 수 <= 30
- 같은 이름을 가진 의상은 존재하지 않음
- clothes의 모든 원소는 문자열(알파벳 소문자, '_')로 이루어짐
- 1 <= 문자열 길이 <= 20
- 스파이는 하루에 최소 한 개의 의상은 입음
'''



# 출력
'''
1. 서로 다른 옷의 조합의 수를 return
'''


# 코드 1

# 접근방법
'''
"headgear" 2개, "eyewear" 1개인 경우
"headgear" 경우의 수 -> 2 + 1(착용 안함) = 3
"eyewear" 경우의 수 -> 1 + 1(착용 안함) = 2
그러므로, 3 x 2 - 1(아무것도 착용 안한 경우) = 5
'''

import sys

sys.stdin = open('input_text/위장.txt')

def solution(clothes):
    cloth_types = {}   # 옷 종류
    
    # 옷 종류에 따른 옷 개수 카운트
    for one in clothes:
        cloth_type = one[1]
        if cloth_types.get(cloth_type):
            cloth_types[cloth_type] += 1
        else:
            cloth_types[cloth_type] = 1
    
    # 조합 구하기
    rst = 1
    for cloth_type in cloth_types:
        rst *= cloth_types[cloth_type] + 1

    return rst - 1


# 실행 결과: 성공



# 코드 2

# 접근방법
'''
reduce 함수 참고: https://www.daleseo.com/python-functools-reduce/
reduce(집계 함수, 순회 가능한 데이터[, 초기값])
'''
from collections import Counter
from functools import reduce
import sys

sys.stdin = open('input_text/위장.txt')

def solution(clothes):
    cloth_types = Counter([cloth_type for _, cloth_type in clothes])
    rst = reduce(lambda acc, val: acc * (val + 1), cloth_types.values(), 1)
    return rst - 1


# 실행 결과: 성공