# https://www.acmicpc.net/problem/2563
# 문제2563번.색종이
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 색종이의 수
- 0 < 색종이 수 <= 100
2. 한 줄에 하나씩 색종이를 붙인 위치 
- 위치 = (색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리, 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리)
- 색종이가 도화지 밖으로 나가는 경우는 없음
'''



# 출력
'''
1. 100 x 100 크기의 도화지에서 10 x 10 크기의 색종이가 붙은 검은 영역의 넓이를 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2563.txt')

# 100 x 100 크기의 도화지
matrix = [[0] * 100 for _ in range(100)]

# 도화지에 색종이 붙이기
paper = int(input())   # 색종이 수
for _ in range(paper):
    x, y = map(int, input().split())
    for r in range(y, y + 10):
        for c in range(x, x + 10):
            matrix[r][c] = 1

# 색종이가 붙은 검은 영역(1)의 넓이 구하기
print(sum(sum(row) for row in matrix))


# 실행결과(메모리:31256KB, 시간:44ms)