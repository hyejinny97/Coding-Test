# https://www.acmicpc.net/problem/2439
# 문제2439.별 찍기-2
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 정수 N
- 1 <= N <= 100
'''



# 출력
'''
1. N번째 줄까지 차례대로 N개의 별을 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2439.txt')

N = int(input())

for n in range(1, N + 1):
    print(" " * (N - n) + '*' * n)



# 실행 결과: 성공(메모리:30840kb, 시간:68ms)