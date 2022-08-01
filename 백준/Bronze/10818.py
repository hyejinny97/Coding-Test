# https://www.acmicpc.net/problem/10818
# 문제10818.최소, 최대
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 정수 N의 갯수
- 1 <= N의 갯수 <= 1,000,000
2. N개의 정수
- -1,000,000 <= 정수 <= 1,000,000
'''



# 출력
'''
1. 정수 N개의 최솟값과 최댓값을 출력
'''



# 코드
import sys

sys.stdin = open('input_text/10818.txt')

N = int(input())
nums = list(map(int, input().split()))

max_n = -1000000
min_n = 1000000
for n in nums:
    if max_n < n:
        max_n = n
    if min_n > n:
        min_n = n

print(min_n, max_n)



# 실행 결과: 성공(메모리:148408kb, 시간:476ms)