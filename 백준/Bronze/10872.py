# https://www.acmicpc.net/problem/10872
# 문제10872번.팩토리얼
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 정수 N
- 0 <= N <= 12
'''



# 출력
'''
1. N!을 출력
'''



# 코드
import sys

sys.stdin = open('input_text/10872.txt')

def factorial(N):
    if N == 0 or N == 1:
        return 1

    return N * factorial(N - 1)


N = int(input())
print(factorial(N))



# 실행 결과: 성공(메모리:30840kb, 시간:80ms)