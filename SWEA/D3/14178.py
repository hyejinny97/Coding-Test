# 문제14178번.1차원 정원
# 시간: 3초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 꽃 갯수 N, 분무 길이 D
- 좌표 x에 분무기를 놓았을 경우 닫힌 구간 [x - D, x + D]에 심긴 모든 꽃들에 물을 줄 수 있음
- 1 ≤ N, D ≤ 100
'''



# 출력
'''
1. #{테스트케이스} {필요한 최소한의 분무기 수}
- 모든 꽃이 한 개 이상의 분무기에서 물을 받을 수 있도록 하기 위해 필요한 최소한의 분무기 수
'''



# 코드
import sys

sys.stdin = open('../input_text/14178.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, D = map(int, input().split())
    watering = 1 + D * 2
    
    rst = 0
    if N % watering != 0:
        rst += 1
    rst += N // watering

    print(f'#{test_case} {rst}')
    


# 실행 결과: 성공(메모리:64,888 kb, 시간:1,248 ms)