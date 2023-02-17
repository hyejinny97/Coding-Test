# https://www.acmicpc.net/problem/11653
# 문제11653번.소인수분해
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 정수 N 
- 1 ≤ N ≤ 10,000,000
'''



# 출력
'''
1. N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력
- N이 1인 경우 아무것도 출력하지 않음
'''



# 코드
import sys

sys.stdin = open('input_text/11653.txt')

def is_prime(num):
    if num == 1:
        return False
    
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


N = int(input())

primes = []   # 소인수분해 결과
while N != 1:
    for num in range(2, N + 1):
        if N % num == 0 and is_prime(num):
            primes.append(str(num))
            N //= num
            break

print('\n'.join(primes))


# 실행 결과: 성공(메모리:31388kb, 시간:908ms)