# 문제2001번.파리 퇴치
# 시간: 30초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. N x N 크기의 행렬 길이 N, M x M 크기의 파리채 길이 M
- 5 <= N <= 15
- 2 <= M <= N
- 각 영역의 파리 갯수는 30 이하
3. N줄에 N x N 크기 행렬
- 배열 안에 숫자는 해당 영역에 존재하는 파리의 갯수를 의미
'''



# 출력
'''
1. #{테스트케이스} {파리채를 한 번 내리쳐 죽일 수 있는 파리 최댓값}
'''



# 코드 
import sys

sys.stdin = open('../input_text/2001.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    # N x N 크기의 행렬
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 행렬을 차례로 돌면서 파리 죽이기
    max_fly = 0
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            # M x M 크기 내에 파리 갯수 카운트
            fly = 0
            for x in range(M):
                for y in range(M):
                    fly += matrix[r + x][c + y]   

            # 죽일 수 있는 파리 최댓값 갱신
            max_fly = max(max_fly, fly)
    
    print(f'#{test_case} {max_fly}')



# 실행 결과: 성공(메모리:60,100 kb, 시간:145 ms)