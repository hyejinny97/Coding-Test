# https://www.acmicpc.net/problem/2581
# 문제2581번.소수
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 자연수 M
2. 자연수 N
- 0 < M <= N <= 10,000
'''



# 출력
'''
1. M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력
- 단, 소수가 없을 경우는 첫째 줄에 -1을 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2581.txt')

def is_prime(num):
    if num == 1:
        return False
    
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


M = int(input())
N = int(input())

primes = []
for num in range(M, N + 1):
    if is_prime(num):
        primes.append(num)

if primes:
    print(sum(primes), min(primes), sep='\n')
else:
    print(-1)


# 실행 결과: 성공(메모리:31256kb, 시간:52ms)