# 문제10570번.제곱 팰린드롬 수
# 시간: 100개의 테스트케이스 다 합해서 2초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 자연수 A, B
- 1 ≤ A ≤ B ≤ 1000
'''



# 출력
'''
1. #{테스트케이스} {A 이상 B 이하 제곱 팰린드롬 수}
- 제곱 팰린드롬: N과 √N이 모두 팰린드롬
'''



# 코드 1
import sys
from math import sqrt

sys.stdin = open('../input_text/10570.txt')

def isPalindrome(n):
    num = str(n)
    left = 0   # 좌측 인덱스
    right = len(num) - 1   # 우측 인덱스
    while left < right:
        if num[left] != num[right]:
            return False
        left += 1
        right -= 1
    return True


T = int(input())
for test_case in range(1, T + 1):
    A, B = map(int, input().split())

    cnt = 0
    for num in range(A, B + 1):
        # 일단 제곱근값이 정수여야 함
        if sqrt(num) == int(sqrt(num)):
            # 제곱 팰린드롬 수의 조건
            if isPalindrome(num) and isPalindrome(int(sqrt(num))):
                cnt += 1
    
    print(f'#{test_case} {cnt}')



# 실행 결과: 성공(메모리:60,132 kb, 시간:174 ms)



# 코드 2
import sys
from math import sqrt

sys.stdin = open('../input_text/10570.txt')

def isPalindrome(n):
    num = str(n)
    left = 0   # 좌측 인덱스
    right = len(num) - 1   # 우측 인덱스
    while left < right:
        if num[left] != num[right]:
            return False
        left += 1
        right -= 1
    return True


# 1부터 1000까지 제곱 팔린드롬 수인지 확인
nums = [0]   # 인덱스: 숫자, 값: 제곱 팰린드롬 맞으면 1, 아니면 0
for num in range(1, 1000 + 1):
    palindrome = False
    # 일단 제곱근값이 정수여야 함
    if sqrt(num) == int(sqrt(num)):
        # 제곱 팰린드롬 수의 조건
        if isPalindrome(num) and isPalindrome(int(sqrt(num))):
            palindrome = True
    
    if palindrome:
        nums.append(1)
    else:
        nums.append(0)


T = int(input())
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    
    print(f'#{test_case} {sum(nums[A : B + 1])}')



# 실행 결과: 성공(메모리:59,340 kb, 시간:146 ms)



# 코드 3
import sys
from math import sqrt

sys.stdin = open('../input_text/10570.txt')

def isPalindrome(n):
    num = str(n)
    left = 0   # 좌측 인덱스
    right = len(num) - 1   # 우측 인덱스
    while left < right:
        if num[left] != num[right]:
            return False
        left += 1
        right -= 1
    return True


# 1부터 1000까지 수 중에서 제곱 팔린드롬 수 찾기
nums = set() 
# 일단 제곱값이 1000 이하인 것만 선별
for num in range(1, int(sqrt(1000)) + 1):
    # 제곱 팰린드롬 수의 조건
    if isPalindrome(num) and isPalindrome(num ** 2):
        nums.add(num ** 2)
    

T = int(input())
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    
    cnt = 0
    for num in nums:
        if A <= num <= B:
            cnt += 1

    print(f'#{test_case} {cnt}')



# 실행 결과: 성공(메모리:56,924 kb, 시간:153 ms)