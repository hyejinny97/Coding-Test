# https://school.programmers.co.kr/learn/courses/30/lessons/131701?language=python3
# 코딩테스트연습 < 연습문제 < 문제.연속 부분 수열 합의 개수



# 입력
'''
1. 원형 수열의 모든 원소 elements
- 3 <= elements 길이 <= 1,000
- 1 <= elements 원소 <= 1,000
'''



# 출력
'''
1. 원형 수열의 연속 부분 수열 합으로 만들 수 있는 수의 개수를 return
'''



# 코드 1

# 접근방법
'''
elements 길이만큼 반복해야 빠짐없이 경우의 수를 채울 수 있음
'''

import sys

sys.stdin = open('input_text/연속부분수열합의개수.txt')

# def solution(elements):
#     sum_nums = set()
#     for cnt in range(1, len(elements) + 1):  # 연속 부분 수열 개수
#         for start in range(len(elements)):
#             sum_num = 0
#             if len(elements) - start < cnt:
#                 sum_num = sum(elements[start:] + elements[:cnt - (len(elements) - start)])
#                 continue
#             sum_num = sum(elements[start:start + cnt])
#             print(f'cnt:{cnt}, start:{start}, sum_num:{sum_num}')
#             sum_nums.add(sum_num)

#     return len(sum_nums)
# print(solution([7,9,1,1,4]))


from collections import deque

def solution(elements):
    q = deque(elements)
    sum_nums = set()   # 길이만큼 연속 부분 수열의 합 모음
    for long in range(1, len(elements) + 1):  # 연속 부분 수열 길이
        for _ in range(len(elements)):  # elements 길이만큼 반복해야함
            sum_num = 0
            for _ in range(long):
                next = q.popleft()
                sum_num += next
                print(next)
                q.append(next)
            sum_nums.add(sum_num)

    return len(sum_nums)


# 실행 결과: 실패(1번 제외한 모든 테스트 실패)



# 코드 2

# 접근방법
'''
elements 길이만큼 반복해야 빠짐없이 경우의 수를 채울 수 있음
즉, elements 길이가 5이고 길이 3씩 수열을 합한다면, 
총 5 * 3 = 15개 만큼 원소를 지나야 함

지나온 원소가 5개라면, 
다음 원소의 인덱스는 (지나온 원소 개수 % elements 길이) = 5 % 5 = 0 이다
'''

import sys

sys.stdin = open('input_text/연속부분수열합의개수.txt')

def solution(elements):
    sum_nums = set()   # 길이만큼 연속 부분 수열의 합 모음
    for long in range(1, len(elements) + 1):  # 연속 부분 수열 길이
        cnt = 0   # 지나온 총 요소 개수
        while cnt != long * len(elements):
            sum_num = 0
            for _ in range(long):
                sum_num += elements[cnt % len(elements)]
                cnt += 1
            sum_nums.add(sum_num)

    return len(sum_nums)


# 실행 결과: 실패(1번 제외한 모든 테스트 실패)



# 코드 3

# 접근방법
'''
1. 젤 앞에 [0]을 더한 후, elements 길이만큼 요소를 반복해서 적기
2. 요소를 누적해서 합하기
3. 연속 부분 수열 개수 길이만큼 합한 값은 누적 배열의 인덱스 차가 됨

ex) elements = [7,9,1]이면, 총 3번 반복해서 적기
[0,7,9,1,7,9,1,7,9,1]
⇒ 누적합 = [0,7,16,17,24,33,34,41,50,51]
⇒ 길이 2씩 합한다고 하면, 아래와 같이 구할 수 있음
(idx = 2)의 값 - (idx = 0)의 값
(idx = 4)의 값 - (idx = 2)의 값
(idx = 6)의 값 - (idx = 4)의 값
'''

import sys
from itertools import accumulate

sys.stdin = open('input_text/연속부분수열합의개수.txt')

def solution(elements):
    # 누적합 배열
    acc_elements = list(accumulate([0] + elements * len(elements)))  

    sum_nums = set()   # 길이만큼 연속 부분 수열의 합 모음
    for long in range(1, len(elements) + 1):  # 연속 부분 수열 길이
        for i in range(0, len(elements) * long, long):
            sum_nums.add(acc_elements[i + long] - acc_elements[i])

    return len(sum_nums)


# 실행 결과: 실패(1번 제외한 모든 테스트 실패)



# 코드 4

# 접근방법
'''
https://magentino.tistory.com/47
앞의 부분 수열 다음에 위치하는 수부터 부분 수열을 만드는 것이 아님
elements를 첫 요소부터 끝까지 반복해서 돌면서 시작점을 잡아야 함
'''

import sys

sys.stdin = open('input_text/연속부분수열합의개수.txt')

def solution(elements):
    sum_nums = set()   # 길이만큼 연속 부분 수열의 합 모음
    for long in range(1, len(elements) + 1):  # 연속 부분 수열 길이
        for i in range(len(elements)):
            if long + i >= len(elements):
                sum_nums.add(sum(elements[i:] + elements[:long - (len(elements) - i)]))
            else:
                sum_nums.add(sum(elements[i: i + long]))

    return len(sum_nums)


# 실행 결과: 성공
