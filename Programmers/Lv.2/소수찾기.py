# https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 코딩테스트연습 < 완전탐색 < 문제.소수 찾기



# 입력
'''
1. 숫자가 적힌 문자열 numbers
- 1 <= numbers 길이 <= 7
- 0 <= numbers 숫자 <= 9
'''



# 출력
'''
1. 숫자로 만들 수 있는 소수가 몇 개인지 return
'''



# 코드 1

# 접근방법
'''
numbers = '17'이면,
두 자리에 각각 올 수 있는 숫자는 '.(아무것도 오지 않음)', '1' ,'7' 세가지임

첫번째자리   두번째자리
    .            .
    1            1   
    7            7

=> 경우의 수(순열): .1, .7, 1., 17, 7., 71
'''
import sys

sys.stdin = open('input_text/소수찾기.txt')

# 소수인지 확인
def isPrime(num):
    if num == 1 or num == 0:
        return False
    
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
        
    return True


def solution(numbers):
    def permutation(nums: list, long, result = []):  # 순열
        if len(result) == long:
            cases.add(int(''.join(result)))
            return
        
        for num in nums:
            new_nums = nums[:]
            new_nums.remove(num)
            permutation(new_nums, long, result + [num])
    
    # 만들 수 있는 모든 경우의 수 찾기 
    cases = set()  
    permutation(['', *numbers], len(numbers))
    
    # 소수인지 확인
    cnt_primes = 0  # 소수 개수
    for case in cases:
        if isPrime(case):
            cnt_primes += 1

    return cnt_primes


# 실행 결과: 실패



# 코드 2
import sys

sys.stdin = open('input_text/소수찾기.txt')

# 소수인지 확인
def isPrime(num):
    if num == 1 or num == 0:
        return False
    
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
        
    return True


def solution(numbers):
    def permutation(nums: list, long, result = []):  # 순열
        if len(result) == long:
            cases.add(int(''.join(result)))
            return
        
        for num in nums:
            new_nums = nums[:]
            new_nums.remove(num)
            permutation(new_nums, long, result + [num])
    
    # 만들 수 있는 모든 경우의 수 찾기 
    cases = set()  
    for long in range(1, len(numbers) + 1):
        permutation(list(numbers), long)  # mPn
    
    # 소수인지 확인
    cnt_primes = 0  # 소수 개수
    for case in cases:
        if isPrime(case):
            cnt_primes += 1

    return cnt_primes


# 실행 결과: 성공