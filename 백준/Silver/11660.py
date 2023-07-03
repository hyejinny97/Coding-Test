# https://www.acmicpc.net/problem/11660
# 문제11660번.구간 합 구하기5
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 표의 크기 N, 합을 구해야 하는 횟수 M
- 1 ≤ N ≤ 1024
- 1 ≤ M ≤ 100,000
- NxN 크기의 표
2. N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어짐
- 0 < 수 <= 1,000
3. M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어짐
- x1 ≤ x2, y1 ≤ y2
- x: 행, y: 열
'''



# 출력
'''
1. 총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력
'''



# 코드
import sys

sys.stdin = open('input_text/11660.txt')

N, M = map(int, input().split())
matrix = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

acc_matrix = [[0] * (N + 1) for _ in range(N + 1)]   # 누적 표
for row in range(1, N + 1):
    for col in range(1, N + 1):
        acc_matrix[row][col] = acc_matrix[row - 1][col] + acc_matrix[row][col - 1] - acc_matrix[row - 1][col - 1] + matrix[row][col] 

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(acc_matrix[x2][y2] - acc_matrix[x1 - 1][y2] - acc_matrix[x2][y1 - 1] + acc_matrix[x1 - 1][y1 - 1])


# 실행 결과: 성공 - 50점(메모리:105392kb, 시간:992ms)