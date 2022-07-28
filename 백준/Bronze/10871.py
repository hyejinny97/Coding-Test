# https://www.acmicpc.net/problem/10871
# 문제10871번.X보다 작은 수
# 시간제한:1초, 메모리제한:256MB



# 입력
'''
1. 정수 N, X
- 1 <= N, X <= 10,000
2. N개의 수열 A
- 1 <= 수열 내 정수 <= 10,000
'''



# 출력
'''
1. 수열 A에서 X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력
'''



# 코드
import sys

sys.stdin = open('input_text/10871.txt')

N, X = map(int, input().split())
A = map(int, input().split())

for a in A:
    if X > a:
        print(a, end=' ')



# 실행 결과: 성공(메모리:30840kb, 시간:72ms)