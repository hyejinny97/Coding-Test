# https://www.acmicpc.net/problem/9610
# 문제9610번.사분면
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 점의 개수 n
- 1 <= n <= 1,000
2. n개의 줄에 점의 좌표(x, y)
- -10^6 <= x, y <= 10^6
'''



# 출력
'''
1. 각 사분면과 축에 점이 몇 개 있는지 출력
'''



# 코드
import sys

sys.stdin = open('input_text/9610.txt')

n = int(input())
axis, q1, q2, q3, q4 = 0, 0, 0, 0, 0
for _ in range(n):
    x, y = map(int, input().split())
    
    # 축에 있는 좌표
    if x == 0 or y == 0:
        axis += 1
    
    # 1사분면 좌표
    if x > 0 and y > 0:
        q1 += 1
    # 2사분면 좌표
    elif x < 0 and y > 0:
        q2 += 1
    # 3사분면 좌표
    if x < 0 and y < 0:
        q3 += 1
    # 4사분면 좌표
    if x > 0 and y < 0:
        q4 += 1

print(f'Q1: {q1}')
print(f'Q2: {q2}')
print(f'Q3: {q3}')
print(f'Q4: {q4}')
print(f'AXIS: {axis}')



# 실행 결과: 성공(메모리:30840kb, 시간:128ms)