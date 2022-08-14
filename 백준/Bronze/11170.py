# https://www.acmicpc.net/problem/11170
# 문제11170번.0의 갯수
# 시간: 3초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 수 T
- 1 <= T <= 20
2. N, M
- 0 <= N <= M <= 1,000,000
'''



# 출력
'''
1. 각 테스트 케이스마다 N부터 M까지의 0의 갯수를 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/11170.txt')

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    cnt = 0   # 0의 갯수
    for num in range(N, M + 1):
        for n in str(num):
            if n == '0':
                cnt += 1

    print(cnt)



# 실행 결과: 성공(메모리:30840kb, 시간:4992ms)