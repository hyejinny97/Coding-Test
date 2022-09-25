# 문제2805번.농작물 수확하기
# 시간: 4초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 수 T
2. 농장의 크기 N
- 1 <= N <= 49
- 농장은 크기는 항상 홀수
- N x N 크기의 농장
3. 농장 내 농장물의 가치
- 0 <= 가치 <= 5
- 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능
'''



# 출력
'''
1. #{테스트케이스} {농장의 규칙에 따라 얻을 수 있는 수익}
'''



# 코드
import sys

sys.stdin = open('../input_text/2805.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    
    # N x N 크기의 농장을 2차원배열 형태로 구현
    farm = [list(map(int, input())) for _ in range(N)]

    # 농장을 순회하면서 마름모 형태로 농작물 수확하기
    tot_value = 0
    for r in range(N):
        # 중간 행까지는 홀수 증가
        if 2 * r + 1 <= N:
            width = 2 * r + 1   # 현재 행 수확 너비
        # 중간 행 이후엔 홀수 감소
        else:
            width = 2 * (N - r - 1) + 1
        start = (N - width) // 2   # 시작 열
        for c in range(start, start + width):
            tot_value += farm[r][c]
    
    print(f'#{test_case} {tot_value}')

    

# 실행 결과: 성공(메모리:62,740 kb, 시간:205 ms)