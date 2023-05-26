# https://www.acmicpc.net/problem/24416
# 문제24416번.알고리즘 수업 - 피보나치 수1
# 시간: 1초, 메모리: 512MB



# 입력
'''
1. n
- 5 ≤ n ≤ 40
'''



# 출력
'''
1. 코드1 코드2 실행 횟수를 한 줄에 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/24416.txt')

def fibo(n):
    global cnt1

    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    
    return fibo(n - 1) + fibo(n - 2)

def fibonacci(n):
    global cnt2

    a, b = 1, 1
    for _ in range(3, n + 1):
        cnt2 += 1
        a, b = b, a + b
    return b


N = int(input())

# 재귀 호출
cnt1 = 0
fibo(N)

# DP
cnt2 = 0
fibonacci(N)

print(cnt1, cnt2)


# 실행 결과: 시간 초과



# 코드 2
import sys

sys.stdin = open('input_text/24416.txt')

def fibo(n):
    global cnt1

    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    
    return fibo(n - 1) + fibo(n - 2)


N = int(input())

# 재귀 호출
cnt1 = 0
fibo(N)

# DP
cnt2 = N - 2

print(cnt1, cnt2)


# 실행 결과: pypy3로 성공(메모리:129876kb, 시간:2292ms)