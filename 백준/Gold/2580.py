# https://www.acmicpc.net/problem/2580
# 문제2580번.스도쿠
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 아홉 줄에 걸쳐 9x9 크기의 스도쿠 판 숫자들 정보가 주어짐
- 0: 빈 칸
- 
'''



# 출력
'''
1. 모든 빈 칸이 채워진 스도쿠 판의 최종 모습을 아홉 줄에 걸쳐 한 줄에 9개씩 한 칸씩 띄워서 출력

<스도쿠 빈 칸을 채우는 방식>
1. 각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
2. 굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
'''



# 코드 

# 접근방법
'''
행, 열, 3x3사각형 안에 모두 없는 숫자일 수록 빈 칸에 정답인 숫자일 가능성이 높음
'''
import sys

sys.stdin = open('input_text/2580.txt')

# 스도쿠 빈 칸 채우기
def sudoku(idx):
    # 모든 빈 칸을 다 채운 경우, 스도쿠를 출력하고 재귀 종료
    if idx == len(locs_zero):
        for row in plate:
            print(*row)
        exit(0)

    # 행, 열, 3x3사각형 안에 모두 없는 숫자 찾기
    r, c = locs_zero[idx]
    nums_row = set(plate[r])  # 행에 있는 모든 숫자
    nums_col = set(plate[row][c] for row in range(9))  # 열에 있는 모든 숫자
    nums_square = set()  # 3x3 사각형에 있는 모든 숫자
    for row in range(r // 3 * 3, r // 3 * 3 + 3):
        for col in range(c // 3 * 3, c // 3 * 3 + 3):
            nums_square.add(plate[row][col])
    possible_nums = set(range(1,9+1)) - (nums_row | nums_col | nums_square)
    
    # 가능성 있는 숫자로 빈 칸을 채우고 재귀 반복
    for num in possible_nums:
        plate[r][c] = num
        sudoku(idx + 1)
        plate[r][c] = 0
    

# 스도쿠 판 숫자 정보를 입력받고 0의 위치를 기록하기
plate = []  # 스도쿠 판
locs_zero = []  # 빈 칸의 위치 (r, c)
for r in range(9):
    row = list(map(int, input().split()))
    plate.append(row)
    for c in range(9):
        if row[c] == 0:
            locs_zero.append((r, c))

sudoku(0)  # 첫번 째 빈칸 (idx)


# 실행 결과: python3 시간 초과/pypy3로 성공(메모리:162912kb, 시간:3424ms)