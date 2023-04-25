# https://www.acmicpc.net/problem/1010
# 문제1010번.다리 놓기
# 시간: 0.5초, 메모리: 128MB



# 입력
'''
1. 테스트 케이스의 개수 T
2. T줄마다 강의 서쪽과 동쪽에 있는 사이트의 개수 정수 N, M
- 0 < N ≤ M < 30
'''



# 출력
'''
1. 각 테스트 케이스에 대해 주어진 조건하에 다리를 지을 수 있는 경우의 수를 출력

<다리 조건>
- 한 사이트에는 최대 한 개의 다리만 연결될 수 있다
- 다리끼리는 서로 겹쳐질 수 없다
'''



# 코드 

# 접근방법
'''
N과 M 중 큰 수 = M, 작은 수 = N이라면 
M개의 사이트 중 N개를 선택해 각각을 반대편 사이트 N개와 순서대로 연결시키기만 하면 됨
- 즉, 다리를 지을 수 있는 경우의 수 == M개의 사이트 중 N개를 선택하는 경우의 수
'''
import sys

sys.stdin = open('input_text/1010.txt')

def combination(N, K):   # nCk
    K = min(K, N - K)
    if K == 0:
        return 1
    
    rst = 1
    for n in range(N, N - K, -1):  # 분자
        rst *= n
    for k in range(K, 0, -1):   # 분모
        rst //= k

    return rst


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(combination(max(N,M), min(N,M)))


# 실행 결과: 성공(메모리:31256kb, 시간:80ms)

