# https://www.acmicpc.net/step/10
# 문제1978번.소수 찾기
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 수의 개수 N
- 0 < N <= 100
2. N개의 자연수
- 0 < 자연수 <= 1,000
'''



# 출력
'''
1. 주어진 N개의 수들 중 소수의 개수를 출력
'''



# 코드
import sys

sys.stdin = open('input_text/1978.txt')

def is_prime(num):
    if num == 1:
        return False

    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False

    return True


N = int(input())
nums = list(map(int, input().split()))

cnt = 0   # 소수 개수
for n in nums:
    if is_prime(n):
        cnt += 1
print(cnt)


# 실행 결과: 성공(메모리:31256kb, 시간:40ms)