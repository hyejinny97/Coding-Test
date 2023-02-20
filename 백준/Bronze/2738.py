# https://www.acmicpc.net/problem/2738
# 문제2738번.행렬 덧셈
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 행렬의 크기 N 과 M
- 0 < N, M <= 100
2. N개의 줄에 행렬 A의 원소 M개
3. N개의 줄에 행렬 B의 원소 M개
- -100 <= 원소 <= 100
'''



# 출력
'''
1. N개의 줄에 행렬 A와 B를 더한 행렬을 출력
- 행렬의 각 원소는 공백으로 구분
'''



# 코드
import sys

sys.stdin = open('input_text/2738.txt')

N, M = map(int, input().split())

# 행렬 A, B 입력값을 받음
array_A = []
for _ in range(N):
    array_A.append(list(map(int, input().split())))

array_B = []
for _ in range(N):
    array_B.append(list(map(int, input().split())))

# 행렬 A, B를 더함
for r in range(N):
    for c in range(M):
        print(array_A[r][c] + array_B[r][c], end=' ')
    print()


# 실행결과(메모리:31256KB, 시간:56ms)