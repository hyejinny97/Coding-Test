# https://www.acmicpc.net/problem/2563
# 문제2563번.색종이
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 색종이의 수 N
- 도화지 크기: 가로세로 각각 100
- 색종이 크기: 가로세로 각각 10
- 0 < N <= 100
2. N개의 줄에 색종이를 붙인 위치 (x, y)
'''



# 출력
'''
1. 색종이가 붙은 검은 영역의 넓이 출력
'''



# 코드
import sys

sys.stdin = open("input_text/2563.txt")

# 도화지를 이차원리스트로 만들기
matrix = []
for _ in range(101):
    matrix.append([0] * 101)

# 도화지에 색종이 붙이기
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for r in range(y, y + 10):
        for c in range(x, x + 10):
            matrix[r][c] = 1

# 색종이가 붙은 영역의 넓이 출력
cnt = 0
for row in matrix:
    cnt += row.count(1)
print(cnt)



# 실행 결과: 성공(메모리:30840kb, 시간:72ms)