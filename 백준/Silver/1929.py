# https://www.acmicpc.net/problem/1929
# 문제1929번.소수 구하기
# 시간: 2초, 메모리: 256MB



# 입력
'''
1. 자연수 M, N
- 1 ≤ M ≤ N ≤ 1,000,000
'''



# 출력
'''
1. M이상 N이하의 소수를 한 줄에 하나씩, 증가하는 순서대로 출력
'''



# 코드
import sys

sys.stdin = open('input_text/1929.txt')

def is_prime(num):
    if num == 1:
        return False
    
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


M, N = map(int, input().split())

primes = []  
for num in range(M, N + 1):
    if is_prime(num):
        primes.append(str(num))

print('\n'.join(primes))


# 실행 결과: 성공(메모리:36828kb, 시간:3108ms)