# 문제1933.간단한 N의 약수
# 시간: 4초, 메모리: 256MB

# 입력
'''
1. 정수 1개
- 1 <= N <= 1,000
'''

# 출력
'''
1. 정수 N의 모든 약수를 오름차순으로 출력
'''

# 코드 
import sys

sys.stdin = open('SWEA/input_text/1933.txt', 'r')

n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=' ')

# 실행 결과: 성공(메모리:56,712 kb, 시간:136 ms)
