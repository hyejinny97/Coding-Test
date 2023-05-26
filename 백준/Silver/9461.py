# https://www.acmicpc.net/problem/9461
# 문제9461번.파도반 수열
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 테스트 케이스의 개수 T
2. N
- 1 ≤ N ≤ 100
'''



# 출력
'''
1. 각 테스트 케이스마다 P(N)을 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/9461.txt')

T = int(input())
for _ in range(T):
    N = int(input())

    if N == 1 or N == 2 or N == 3:
        print(1)
    else:
        a, b, c = 1, 1, 1
        for _ in range(4, N + 1):
            a, b, c = b, c, a + b
        print(c)
    

# 실행 결과: 성공(메모리:31256kb, 시간:52ms)