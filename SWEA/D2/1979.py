# 문제1979번.어디에 단어가 들어갈 수 있을까
# 시간: 30초, 메모리: 256MB



# 입력
'''
1. 테스트케이스 갯수 T
2. N x N 크기 단어 퍼즐의 가로, 세로 길이 N, 단어의 길이 K
- 5 <= N <= 15
- 2 <= K <= N
3. N개 줄에 퍼즐 모양의 정보
- 1: 흰색
- 0: 검은색
'''



# 출력
'''
1. #{테스트케이스} {주어진 퍼즐 모양에서 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수}
'''



# 코드 
import sys

sys.stdin = open('../input_text/1979.txt', 'r')

# 행렬의 가로줄에서 길이 K의 단어가 들어갈 수 있는 자리의 수 세기
def cnt_K(matrix, K):
    cnt = 0
    for row in matrix:
        for s in ''.join(row).split('0'):
            if len(s) == K:
                cnt += 1
    
    return cnt


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    
    # 퍼즐 모양
    puzzle = [input().split() for _ in range(N)]

    # 2차원 퍼즐의 가로줄에서 길이 K의 단어가 들어갈 수 있는 자리의 수 세기
    cnt_row = cnt_K(puzzle, K)

    # 2차원 퍼즐 행렬 반전
    new_puzzle = [[0] * N for _ in range(N)]
    for c in range(N):
        for r in range(N):
            new_puzzle[c][r] = puzzle[r][c]
    
    # 2차원 퍼즐의 세로줄에서 길이 K의 단어가 들어갈 수 있는 자리의 수 세기
    cnt_col = cnt_K(new_puzzle, K)

    print(f'#{test_case} {cnt_row + cnt_col}')



# 실행 결과: 성공(메모리:59,612 kb, 시간:140 ms)