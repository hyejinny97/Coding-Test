# https://school.programmers.co.kr/learn/courses/30/lessons/12953
# 코딩테스트연습 < 연습문제 < 문제.N개의 최소공배수



# 입력
'''
1. n개의 숫자를 담은 배열 arr
- 1 <= arr 길이 <= 15
- 0 < 숫자 <= 100
'''



# 출력
'''
1. n개 숫자들의 최소공배수(Least Common Multiple)를 반환
'''



# 코드 1
import sys

# sys.stdin = open('input_text/N개의최소공배수.txt')

def solution(arr):
    # 최대공약수(Greatest Common Divisor, GCD) 구하기
    min_num = min(arr)
    for num in range(min_num, 0, -1):
        if len(list(filter(lambda n : n % num == 0, arr))) == len(arr):
            GCD = num
            break

    # 최소공배수(Least Common Multiple, LCM) 구하기
    LCM = GCD
    for ele in arr:
        LCM *= ele // GCD 

    return LCM 


# 실행 결과: 실패(arr = [2,3,4]일때, 12가 아닌 24를 반환)



# 코드 2

# 접근방법
'''
두 수 a, b의 최대공약수 gcd
두 수 a, b의 최소공배수 lcm = (a * b) // gcd
세 수 a, b, c의 최소공배수 = 두 수 a, b의 최소공배수인 l과 c의 최소공배수 lcm
'''

import sys

# sys.stdin = open('input_text/N개의최소공배수.txt')

def solution(arr):
    # 두 수의 최대공약수(Greatest Common Divisor, GCD) 구하기
    def GCD(num1, num2):
        min_num = min(num1, num2)
        for n in range(min_num, 0, -1):
            if num1 % n == 0 and num2 % n == 0:
                return n

    # 두 수의 최소공배수(Least Common Multiple, LCM) 구하기
    def LCM(num1, num2):
        return num1 * num2 // GCD(num1, num2)

    # 배열을 순회하면서 두 요소의 최소공배수를 반복해서 구하기
    if len(arr) == 1:
        return arr[0]

    LCM_of_two = LCM(arr[0], arr[1])
    for i in range(2, len(arr)):
        LCM_of_two = LCM(LCM_of_two, arr[i])

    return LCM_of_two


# 실행 결과: 성공



# 코드 3

import sys
from math import gcd

# sys.stdin = open('input_text/N개의최소공배수.txt')

def LCM(arr):
    rst = arr[0]
    # 배열을 순회하면서 두 요소의 최소공배수를 반복해서 구하기
    for num in arr:
        rst = num * rst // gcd(rst, num)
    return rst


# 실행 결과: 성공