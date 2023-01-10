# https://school.programmers.co.kr/learn/courses/30/lessons/12949
# 코딩테스트연습 < 연습문제 < 문제.행렬의 곱셈



# 입력
'''
1. 2차원 행렬 arr1과 arr2
- 2 <= 행렬 arr1, arr2의 행과 열의 길이 <= 100
- -10 <= 행렬 arr1, arr2의 원소 <= 20
'''



# 출력
'''
1.  arr1에 arr2를 곱한 결과를 반환
'''


# 코드 1

# 접근방법
'''
<행렬의 곱> 
- 필수조건: arrA의 열 개수 == arrB의 행 개수 일 때, 행렬의 곱 가능
arrA x arrB = arrC 라고 하면
arrC의 (r, c) = (0, 1) 값은 (arrA의 r=0번째 행) x (arrB의 c=1번째 열)이다.

        arrA   arrB   arrC
      c 0 1
    r   →
    0 ↓ 1 4    1 2    0 0
    1   3 2    3 4    0 0
    2   4 1           0 0
'''

import sys

sys.stdin = open('input_text/행렬의곱셈.txt')

def solution(arr1, arr2):
    # 두 배열의 곱을 반환하는 함수
    def mul_two_arr(A, B):
        mul = 0
        for i in range(0, len(A)):
            mul += A[i] * B[i]
        return mul

    # 행렬 answer의 프레임 만들기
    answer = []
    for _ in range(len(arr1)):
        answer.append([0] * len(arr1[0]))

    # arr1 x arr2 = answer
    for r in range(0, len(arr1)):
        for c in range(0, len(arr1[0])):
            answer[r][c] = mul_two_arr(arr1[r], [arr2[i][c] for i in range(len(arr2))])

    return answer


# 실행 결과: 실패(런타임 에러 ⇒ 이유: 2x4행렬과 4x2행렬의 곱일때 2x2행렬이 나와야 함)



# 코드 2

# 접근방법
'''
<행렬의 곱> 
- 필수조건: arrA의 열 개수 == arrB의 행 개수 일 때, 행렬의 곱 가능
arrA x arrB = arrC일때
arrC = (arrA의 행 개수 x arrB의 열 개수) 행렬
'''

import sys

sys.stdin = open('input_text/행렬의곱셈.txt')

def solution(arr1, arr2):
    # 두 배열의 곱을 반환하는 함수
    def mul_two_arr(A, B):
        mul = 0
        for i in range(0, len(A)):
            mul += A[i] * B[i]
        return mul

    # 행렬 answer의 프레임 만들기
    answer = []
    for _ in range(len(arr1)):
        answer.append([0] * len(arr2[0]))

    # arr1 x arr2 = answer
    for r in range(0, len(arr1)):
        for c in range(0, len(arr2[0])):
            answer[r][c] = mul_two_arr(arr1[r], [arr2[i][c] for i in range(len(arr2))])

    return answer


# 실행 결과: 성공



# 코드 3
import sys

sys.stdin = open('input_text/행렬의곱셈.txt')

def solution(arr1, arr2):
    answer = []
    for arr1_row in arr1:
        answer_row = []
        for arr2_col in zip(*arr2):
            answer_ele = 0
            for a, b in zip(arr1_row, arr2_col):
                answer_ele += a * b
            answer_row.append(answer_ele)
        answer.append(answer_row)
    return answer


# 실행 결과: 성공



# 코드 4
import sys

sys.stdin = open('input_text/행렬의곱셈.txt')

def solution(arr1, arr2):
    return [[sum(a * b for a, b in zip(arr1_row, arr2_col)) for arr2_col in zip(*arr2)] for arr1_row in arr1]


# 실행 결과: 성공