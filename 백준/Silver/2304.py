# https://www.acmicpc.net/problem/2304
# 문제2304번.창고 다각형
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 기둥의 갯수 N
- 1 <= N <= 1,000
2. N개의 줄에 각 기둥의 왼쪽 면의 위치를 나타내는 L, 높이를 나타내는 H
- 1 <= L, H <= 1,000
'''



# 출력
'''
1.가장 작은 창고 다각형의 면적
'''



# 코드
import sys

sys.stdin = open('input_text/2304.txt')

# 기둥들의 높이는 리스트로 표현
N = int(input())
heights = [0] * 1001   # 인덱스: 기둥 위치(L), 값: 기둥 높이(H)
max_height, max_i = 0, []    # 가장 높은 기둥의 H, L 찾기
min_L, max_L = 1000, 0   # 가장 왼쪽 기둥의 L, 가장 오른쪽 기둥의 L 
for _ in range(N):
    L, H = map(int, input().split())
    heights[L] = H
    if H > max_height:
        max_height = H
        max_i = [L]
    elif H == max_height:
        max_i.append(L)
    
    if L < min_L:
        min_L = L
    if L > max_L:
        max_L = L
max_i.sort()

# 가장 높은 기둥 왼쪽 부분의 다각형 면적 구하기
tot_area = 0
prev_max_height = heights[min_L]
prev_max_i = min_L
for i in range(min_L, max_i[0] + 1):
    if heights[i] > prev_max_height:
        tot_area += (i - prev_max_i) * prev_max_height   # 가로 길이 x 세로 길이
        prev_max_height = heights[i]
        prev_max_i = i

# 가장 높은 기둥 오른쪽 부분의 다각형 면적 구하기
prev_max_height = heights[max_L]
prev_max_i = max_L
for i in range(max_L, max_i[-1] - 1, -1):
    if heights[i] > prev_max_height:
        tot_area += (prev_max_i - i) * prev_max_height   # 가로 길이 x 세로 길이
        prev_max_height = heights[i]
        prev_max_i = i

# 가장 높은 기둥 간의 다각형 면적 구하기
tot_area += max_height * (max_i[-1] - max_i[0] + 1)

print(tot_area)



# 실행 결과: 성공(메모리:30840kb, 시간:108ms)