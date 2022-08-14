# https://www.acmicpc.net/problem/1526
# 문제1526번.가장 큰 금민수
# 시간: 2초, 메모리: 256MB



# 입력
'''
1. N
- 4 <= N <= 1,000,000
'''



# 출력
'''
1. N보다 작거나 같은 금민수 중 가장 큰 것을 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/1526.txt')

N = int(input())

for n in range(N, 4 - 1, -1):
    for num in str(n):
        if num not in '47':
            break
    else:
        print(n)
        break



# 실행 결과: 성공(메모리:30840kb, 시간:176ms)