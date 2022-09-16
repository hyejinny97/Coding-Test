# 문제1209번.Sum
# 시간: 30초, 메모리: 256MB



# 입력
'''
<총 10개의 테스트 케이스 T>
1. 테스트 케이스 번호
2. 2차원 배열의 각 행 값
- 배열 크기: 100 x 100
'''



# 출력
'''
1. #{테스트케이스} {각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값}
'''



# 코드 1 - 실제 100 x 100 크기의 2차원 배열을 만듦
import sys

sys.stdin = open('../input_text/1209.txt')

for _ in range(10):
    test_case = int(input())

    # 100개의 행 입력 받기
    matrix = [list(map(int, input().split())) for _ in range(100)]

    # 각 행의 합 중 최댓값 구하기
    max_sum = 0
    for row in matrix:
        max_sum = max(max_sum, sum(row))
    
    # 각 열의 합 중 최댓값 구하기
    for c in range(0, 99 + 1):
        col_sum = 0
        for r in range(0, 99 + 1):
            col_sum += matrix[r][c]
        max_sum = max(max_sum, col_sum)
    
    # 각 대각선의 합 중 최댓값 구하기
    right_up = 0   # 우상향 대각선
    right_down = 0   # 우하향 대각선
    for i in range(0, 99 + 1):
        right_down += matrix[i][i]
        right_up += matrix[i][99 - i]
    max_sum = max(max_sum, right_up, right_down)

    print(f'#{test_case} {max_sum}')



# 실행 결과: 성공(메모리:62,204 kb, 시간:231 ms)



# 코드 2 - 100 x 100 길이의 1차원 배열을 만듦
import sys

sys.stdin = open('../input_text/1209.txt')

for _ in range(10):
    test_case = int(input())

    # 100개의 행 입력 받기
    array = []
    for _ in range(100):
        array += list(map(int, input().split()))
        
    # 각 행의 합 중 최댓값 구하기
    max_sum = 0
    for mul in range(0, 99 + 1):
        row_sum = sum(array[100 * mul:100 * mul + 100])
        max_sum = max(max_sum, row_sum)

    # 각 열의 합 중 최댓값 구하기
    for c in range(0, 99 + 1):
        col_sum = 0
        for r in range(0, 10000, 100):
            col_sum += array[r + c]
        max_sum = max(max_sum, col_sum)

    # 각 대각선의 합 중 최댓값 구하기
    right_up = 0   # 우상향 대각선
    right_down = 0   # 우하향 대각선
    for mul in range(0, 100):
        right_up += array[100 * mul + mul]
        right_down += array[9900 - 100 * mul + mul]
    max_sum = max(max_sum, right_up, right_down)

    print(f'#{test_case} {max_sum}')



# 실행 결과: 성공(메모리:61,948 kb, 시간:203 ms)