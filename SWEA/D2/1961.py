# 문제1961번.숫자 배열 회전
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 테스트 케이스 개수 T
2. 행렬 크기 N
- 3 <= N <= 7
3. N x N 크기의 행렬
'''

# 출력
'''
1. #{테스트케이스} {시계방향으로 90도, 180도, 270도 회전한 모양}
- 회전한 모양 사이에만 공백 존재
'''

# 코드 
import sys
from pprint import pprint

sys.stdin = open('../input_text/1961.txt', 'r')

# 시계방향으로 90도 회전시키는 함수
def rotate_90(original, rotated):
    for c in range(N):
        for r in range(N):
            rotated[c][r] = original[N - r - 1][c]
    
    return rotated


T = int(input())
for test_case in range(1, T + 1):
    # N x N 크기의 행렬 입력 받기
    N = int(input())
    matrix = [input().split() for _ in range(N)]
    
    # 시계방향으로 90도, 180도(90도 x 2), 270도(90도 x 3) 회전한 행렬 출력
    rot_90 = [[0] * N for _ in range(N)]
    rot_180 = [[0] * N for _ in range(N)]
    rot_270 = [[0] * N for _ in range(N)]
    
    rot_90 = rotate_90(matrix, rot_90)
    rot_180 = rotate_90(rot_90, rot_180)
    rot_270 = rotate_90(rot_180, rot_270)

    # 3개의 회전 행렬 출력
    print(f'#{test_case}')
    for i in range(N):
        print(''.join(rot_90[i]), end = ' ')
        print(''.join(rot_180[i]), end=' ')
        print(''.join(rot_270[i]))



# 실행 결과: 성공(메모리:56,692 kb, 시간:133 ms)