# https://school.programmers.co.kr/learn/courses/30/lessons/132265
# 코딩테스트연습 < 연습문제 < 문제.롤케이크 자르기



# 입력
'''
1. 롤케이크에 올려진 토핑들의 번호를 저장한 정수 배열 topping
- 1 ≤ topping의 길이 ≤ 1,000,000
- 1 ≤ topping의 원소 ≤ 10,000
'''



# 출력
'''
1. 롤케이크를 공평하게 자르는 방법의 수를 return
'''



# 코드 1
import sys

sys.stdin = open('input_text/롤케이크자르기.txt')

def solution(topping):
    rst = 0
    for i in range(len(topping)):
        if len(set(topping[:i + 1])) == len(set(topping[i + 1:])):
            rst += 1
    return rst


# 실행 결과: 실패(시간 초과)



# 코드 2
import sys
from collections import Counter

sys.stdin = open('input_text/롤케이크자르기.txt')

def solution(topping):
    tot_topping = Counter(topping)   # 각 토핑당 개수
    chulsu_topping = set()   # 철수가 가져간 토핑 종류
    rst = 0
    for i in range(len(topping)):
        # 철수가 토핑을 가져감
        tot_topping[topping[i]] -= 1
        if tot_topping[topping[i]] == 0:
            del tot_topping[topping[i]]
        chulsu_topping.add(topping[i])
        
        # 철수가 가져간 토핑 개수와 남아있는 토핑 개수가 같은 경우
        if len(chulsu_topping) == len(tot_topping):
            rst += 1
    
    return rst


# 실행 결과: 성공

