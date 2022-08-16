# 문제1974번.스도쿠 검증
# 시간: 30초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 개수 T
2. 9 x 9 크기의 스도쿠 데이터
'''



# 출력
'''
1. #{테스트케이스} {겹치는 숫자가 없는 경우 1출력, 아니면 0 출력}
- 가로, 세로, 3 x 3 크기 모두 겹치는 숫자가 없어야 함
'''



# 코드 
import sys

sys.stdin = open('../input_text/1974.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    answer = 1   # 초기화: 겹치는 숫자가 없는 완벽한 스도쿠
    
    # 가로 검증
    for row in sudoku:
        if len(set(row)) != 9:
            answer = 0
            break
    
    # 세로 검증
    for c in range(9):
        column = set()
        for r in range(9):
            column.add(sudoku[r][c])
        if len(column) != 9:
            answer = 0
            break

    # 3 x 3 크기 표 검증
    for r in range(0, 6 + 1, 3):
        for c in range(0, 6 + 1, 3):
            table = set()
            # 3 x 3 크기 표
            for x in range(3):
                for y in range(3):
                    table.add(sudoku[r + x][c + y])
            if len(table) != 9:
                answer = 0
                break
        if not answer:
            break

    print(f'#{test_case} {answer}')



# 실행 결과: 성공(메모리:56,664 kb, 시간:139 ms)