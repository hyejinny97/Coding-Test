# https://school.programmers.co.kr/learn/courses/30/lessons/131127
# 코딩테스트연습 < 연습문제 < 문제.할인 행사



# 입력
'''
1. 정현이가 원하는 제품을 나타내는 문자열 배열 want
2. 정현이가 원하는 제품의 수량을 나타내는 정수 배열 number
- 1 ≤ want의 길이 = number의 길이 ≤ 10
- 1 ≤ number의 원소 ≤ 10
- number의 원소의 합은 10
3. 마트에서 할인하는 제품을 나타내는 문자열 배열 discount
- 10 ≤ discount의 길이 ≤ 100,000
- want, discount의 원소: 알파벳 소문자로 이루어진 문자열
- 1 ≤ want의 원소의 길이, discount의 원소의 길이 ≤ 12
'''



# 출력
'''
1. 회원등록시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수를 return
- 가능한 날이 없으면 0을 return
'''


# 코드 1
import sys
from collections import Counter

sys.stdin = open('input_text/할인행사.txt')

def solution(want, number, discount):
    want_products = dict(zip(want, number))   # 원하는 제품들 (종류, 개수)

    register_days = 0   # 회원등록 날짜의 총 일수
    for i in range(len(discount) - 10 + 1):
        discount_products = Counter(discount[i:i+10])   # 10일동안 할인하는 제품들 (종류, 개수)
        # 10일동안 원하는 제품을 모두 할인받을 수 있는지 확인
        for pdt in want_products:
            # 원하는 제품이 없는 경우
            if not discount_products[pdt]:  
                break
            # 제품의 개수가 부족한 경우
            if want_products[pdt] > discount_products[pdt]:
                break
        else:
            register_days += 1

    return register_days


# 실행 결과: 성공



# 코드 2 - 다른 사람 풀이 참고
import sys
from collections import Counter

sys.stdin = open('input_text/할인행사.txt')

def solution(want, number, discount):
    want_products = dict(zip(want, number))

    register_days = 0   
    for i in range(len(discount) - 10 + 1):
        discount_products = Counter(discount[i:i+10])   
        if want_products == discount_products:
            register_days += 1

    return register_days


# 실행 결과: 성공