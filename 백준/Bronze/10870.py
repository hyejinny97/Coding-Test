# https://www.acmicpc.net/problem/10870
# 문제10870번.피보나치 수5
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 수 N
- 0 <= N <= 20
'''



# 출력
'''
1. N번째 피보나치 수를 출력

<피보나치 수>
- 0번째 피보나치 수 = 0
- 1번째 피보나치 수 = 1
- n >= 2일 땐, Fn = Fn-1 + Fn-2 
'''



# 코드
import sys

sys.stdin = open('input_text/10870.txt')

def F(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return F(n - 1) + F(n - 2)

N = int(input())
print(F(N))


# 실행 결과: 성공(메모리:31256kb, 시간:40ms)