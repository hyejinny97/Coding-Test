# https://school.programmers.co.kr/learn/courses/30/lessons/64065
# 코딩테스트연습 < 2019 카카오 개발자 겨울 인턴십 < 문제.튜플

# 입력
'''
1. 특정 튜플을 표현하는 집합이 담긴 문자열 s
- 문자열 s: 원소의 개수가 n개이고, 중복되는 원소가 없는 튜플 (a1, a2, a3, ..., an)을 집합으로 표현함
- 집합은 원소의 순서가 바뀌어도 상관없음
- 5 <= s 길이 <= 1,000,000
- s는 숫자와 '{', '}', ',' 로만 이루어져 있음
- 숫자가 0으로 시작하는 경우는 없음
- 1 <= s가 표현하는 튜플의 원소 <= 100,000
- 1 <= s가 표현하는 튜플의 길이 <= 500
'''



# 출력
'''
1. s가 표현하는 튜플을 배열에 담아 return
<튜플 특징>
- 중복된 원소가 있을 수 있음
- 원소의 순서가 다르면 서로 다른 튜플!!
- 튜플의 원소 개수는 유한
'''


# 코드 1
import sys, re

sys.stdin = open('input_text/튜플.txt')

def solution(s):
    p = re.compile('{[0-9,]+}')
    s_list = p.findall(s)   # ['{1,2,3}', '{2,1}', '{1,2,4,3}', '{2}']
    s_list.sort(key=lambda ele:len(ele))   # ['{2}', '{2,1}', '{1,2,3}', '{1,2,4,3}']

    s_set = set()
    rst = []
    for ele_set in s_list:
        ele_set = map(int, ele_set[1:-1].split(','))
        for ele in ele_set:
            if ele not in s_set:
                rst.append(ele)
            s_set.add(ele)
    
    return rst


# 실행 결과: 성공



# 코드 2
import sys
import re
from collections import Counter

sys.stdin = open('input_text/튜플.txt')

def solution(s):
    p = re.compile('[0-9]+')
    nums = p.findall(s)   # ['2', '2', '1', '2', '1', '3', '2', '1', '3', '4']
    cnts = Counter(nums)   # {'2':4, '1':3, '3':2, '4':1 }
    
    order = sorted(cnts.items(), key=lambda item:item[1], reverse=True)   # [('2', 4), ('1', 3), ('3', 2), ('4', 1)]
    rst = []
    for num, cnt in order:
        rst.append(int(num))
    
    return rst


# 실행 결과: 성공