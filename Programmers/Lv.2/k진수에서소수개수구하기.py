# https://school.programmers.co.kr/learn/courses/30/lessons/92335?language=python3
# 코딩테스트연습 < 2022 KAKAO BLIND RECRUITMENT < 문제.k진수에서 소수 개수 구하기



# 입력
'''
1. 정수 n, k
- 1 ≤ n ≤ 1,000,000
- 3 ≤ k ≤ 10
'''



# 출력
'''
1. n을 k진수로 바꿨을 때, 변환된 수 안에서 찾을 수 있는 아래 조건에 맞는 소수의 개수를 return

<조건에 맞는 소수(Prime number)>
- 0P0: 소수 양쪽에 0이 있는 경우
- P0: 소수 오른쪽에만 0이 있는 경우
- 0P: 소수 왼쪽에만 0이 있는 경우
- P: 소수 양쪽에 아무것도 없는 경우

- 단, P는 각 자릿수에 0을 포함하지 않는 소수이어야함!
- 중복되는 소수를 발견하더라도 모두 따로 세어야함
'''


# 코드 

# 접근방법
'''
진수 변환 참고: https://security-nanglam.tistory.com/508
'''

import sys
import string

sys.stdin = open('input_text/k진수에서소수개수구하기.txt')

# 소수인지 판별하는 함수
def is_prime(num):
    if num == 1:
        return False

    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    
    return True


# n을 k진수로 변환하는 함수 
def convert(num, base):
    tmp = string.digits + string.ascii_lowercase   # 0부터 z까지 문자열
    q, r = divmod(num, base)

    if q == 0:
        return tmp[r] 
    else:
        return convert(q, base) + tmp[r]


def solution(n, k):
    # n을 k진수로 변환
    new_n = convert(n, k)

    # 0을 기준으로 쪼개기
    nums = str(new_n).split('0')

    # k진수에서 조건에 맞는 소수 찾기
    cnt = 0  
    for num in nums:
        if num and is_prime(int(num)):  
            cnt += 1

    return cnt


# 실행 결과: 성공