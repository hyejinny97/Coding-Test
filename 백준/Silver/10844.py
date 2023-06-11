# https://www.acmicpc.net/problem/10844
# 문제10844번.쉬운 계단 수
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 정수 N
- 1 <= N <= 10
'''



# 출력
'''
1. 길이가 N인 계단 수 총 갯수를 1,000,000,000으로 나눈 나머지를 출력
- 계단 수: 인접한 모든 자리의 차이가 1인 수
'''



# 코드 

# 접근방법
'''
<점화식>
dp[row][col] = dp[row - 1][col - 1] + dp[row - 1][col + 1]

(row: n번째 자리수)
(col: 0 ~ 9까지의 수)
'''
import sys

sys.stdin = open('input_text/10844.txt')

N = int(input())

dp = [[0] * 10 for _ in range(N)] 
dp[0] = [0,1,1,1,1,1,1,1,1,1]  # idx: 0 ~ 9까지 수, value: 이 자리까지의 계단 수 총 개수

for row in range(1, N):
    for col in range(10):
        if (col - 1) >= 0:
            dp[row][col] += dp[row - 1][col - 1]
        
        if (col + 1) <= 9:
            dp[row][col] += dp[row - 1][col + 1]

print(sum(dp[-1]) % 1000000000)


# 실행 결과: 성공(메모리:31256kb, 시간:44ms)