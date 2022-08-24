# https://www.acmicpc.net/problem/2628
# 문제2628번.종이자르기
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 종이의 가로길이, 세로길이
- 0 < 길이 <= 100
2. 칼로 잘라야하는 점선의 개수
3. 잘라야하는 점선 정보 => 잘라야하는 방향(가로 또는 세로), 점선 번호
- 0: 가로로 자르는 점선
- 1: 세로로 자르는 점선
- 끝까지 한번에 다 잘라야 함
'''



# 출력
'''
1. 가장 큰 종이 조각의 넓이를 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2628.txt')

# 가로 절단 위치, 세로 절단 위치 기록
hor, ver = map(int, input().split())
N = int(input())
row_cut = [0, ver]
col_cut = [0, hor]
for _ in range(N):
    dir, num = map(int, input().split())
    if dir == 0:
        row_cut.append(num)
    elif dir == 1:
        col_cut.append(num)
row_cut.sort()
col_cut.sort()

# 가장 큰 종이 조각의 넓이 찾기
max_square = 0
for ri in range(1, len(row_cut)):
    for ci in range(1, len(col_cut)):
        rlen = row_cut[ri] - row_cut[ri - 1]   # 사각형 가로길이
        clen = col_cut[ci] - col_cut[ci - 1]   # 사각형 세로길이
        sqaure = rlen * clen   # 사각형 넓이
        max_square = max(max_square, sqaure)   # 사각형 넓이 최댓값 갱신

print(max_square)



# 실행 결과: 성공(메모리:30840kb, 시간:84ms)