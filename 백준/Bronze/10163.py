# https://www.acmicpc.net/problem/10163
# 문제10163번.색종이
# 시간: 1초, 메모리: 64MB



# 입력
'''
1. 색종이 장 수 N
- 1 <= N <= 100
- 격자 가로, 세로 <= 1,001칸
2. 색종이의 왼쪽 아래 좌표(c, r), 너비, 높이

'''



# 출력
'''
1. 입력에서 주어진 순서대로 각 색종이가 보이는 부분의 면적
- 만약 색종이가 보이지 않는다면 0 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/10163.txt')

# 색종이가 놓이는 평면을 2차원 리스트로 표현
matrix = []
for _ in range(1001):
    matrix.append([0] * 1001)

# N장의 색종이를 올려놓음
N = int(input())
for n in range(1, N + 1):
    c_start, r_start, w, h = map(int, input().split())
    # 격자 위에 색종이가 올려진 위치 표시
    for r in range(r_start, r_start + h):
        for c in range(c_start, c_start + w):
            matrix[r][c] = n

# 각 색종이가 보이는 부분의 면적 출력
tot_cnt = [0] * (N + 1)   # 인덱스: 1~N번째 색종이, 값: n번째 색종이가 보이는 부분의 면적
for r in range(1001):
    for c in range(1001):
        tot_cnt[matrix[r][c]] += 1

for cnt in tot_cnt[1:]:
    print(cnt)



# 실행 결과: 부분성공 53점(메모리:37624kb, 시간:340ms)



# 코드 2
import sys

sys.stdin = open('input_text/10163.txt')

# 교집합 체크
def check_intersection(std, cpr):   # std: 기준 색종이, cpr: 비교 대상 색종이
    # 교집합의 행 범위
    r_start = max(papers[std][1], papers[cpr][1])
    r_end = min(papers[std][3], papers[cpr][3])
    # 겹치지 않는 경우
    if r_start > r_end:   
        return 
    
    # 교집합의 열 범위
    c_start = max(papers[std][0], papers[cpr][0])
    c_end = min(papers[std][2], papers[cpr][2])
    # 겹치지 않는 경우
    if c_start > c_end:   
        return 

    # n번째 색종이에 교집합 부분 체크
    for r in range(r_start - papers[std][1], r_end - papers[std][1] + 1):
        for c in range(c_start - papers[std][0], c_end - papers[std][0] + 1):
            paper_n[r][c] -= 1


# N장의 색종이 입력 받기
# 인덱스: 1~N번째 색종이, 값: [c_start, r_start, c_end, r_end, w, h]
papers = [[]]   
N = int(input())
for n in range(1, N + 1):
    c_start, r_start, w, h = map(int, input().split())
    c_end, r_end = c_start + w - 1, r_start + h - 1
    papers.append([c_start, r_start, c_end, r_end, w, h])
    
# 각 색종이가 보이는 부분의 면적 출력
# 인덱스: 1~N번째 색종이, 값: 색종이가 보이는 부분의 면적
rst = [0] * (N + 1)
for n in range(N, 1 - 1, -1):
    # n번째 색종이를 2차원 리스트로 표현
    paper_n = [[1] * papers[n][4] for _ in range(papers[n][5])]
    
    # n번째 색종이가 보이는 부분의 면적 = n번째 색종이와 n번째 이후의 종이의 차집합
    for next in range(n + 1, N + 1):
        check_intersection(n, next)

    # 색종이가 보이는 부분의 면적 계산
    area = 0
    for row in paper_n:
        area += row.count(1)
    rst[n] = area

for area in rst[1:]:
    print(area)



# 실행 결과: 부분성공 53점(메모리:37756kb, 시간:84ms)



# 코드 3 - 코드 1 리팩토링
import sys

sys.stdin = open('input_text/10163.txt')

# 색종이가 놓이는 평면을 2차원 리스트로 표현
matrix = []
for _ in range(1001):
    matrix.append([0] * 1001)

# N장의 색종이를 올려놓음
N = int(input())
minr, minc = 1001, 1001
maxr, maxc = 0, 0
for n in range(1, N + 1):
    c_start, r_start, w, h = map(int, input().split())
    # 격자 위에 색종이가 올려진 위치 표시
    for r in range(r_start, r_start + h):
        for c in range(c_start, c_start + w):
            matrix[r][c] = n

    # 행 최대/최소값, 열 최대/최소값 갱신
    minr, minc = min(minr, r_start), min(minc, c_start)
    maxr, maxc = max(maxr, r_start + h - 1), max(maxc, c_start + w - 1)

# 각 색종이가 보이는 부분의 면적 출력
tot_cnt = [0] * (N + 1)   # 인덱스: 1~N번째 색종이, 값: n번째 색종이가 보이는 부분의 면적
for r in range(minr, maxr + 1):
    for c in range(minc, maxc + 1):
        tot_cnt[matrix[r][c]] += 1

for cnt in tot_cnt[1:]:
    print(cnt)



# 실행 결과: 부분성공 53점(메모리:37624kb, 시간:336ms)