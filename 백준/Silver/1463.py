# https://www.acmicpc.net/problem/1463
# 문제1463번.1로 만들기
# 시간: 0.15초, 메모리: 128MB



# 입력
'''
1. 정수 N
- 1 <= N <= 1,000,000
'''



# 출력
'''
1. 연산 횟수 최솟값 출력

<정수 X에 사용할 수 있는 연산>
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2으로 나누어 떨어지면, 2으로 나눈다.
3. 1을 뺀다.
'''



# 코드 

# 접근방법
'''
정수 N에서 3을 나누거나 2를 나누거나 1을 빼가며 1을 구함
= 1에서 3을 곱하거나 2를 곱하거나 1을 더해가며 정수 N을 구함
'''
import sys

sys.stdin = open('input_text/1463.txt')

N = int(input())

MAX = 1000000   # 연산 횟수 최댓값
dp = [MAX] * (N + 1)   # idx: 1~N 숫자, value: 연산 횟수 최솟값
dp[1] = 0

for i in range(1, N):
    if dp[i] == MAX:
        continue
    
    if (i * 3) <= N:
        dp[i * 3] = min(dp[i] + 1, dp[i * 3])
    
    if (i * 2) <= N:
        dp[i * 2] = min(dp[i] + 1, dp[i * 2])
    
    if (i + 1) <= N:
        dp[i + 1] = min(dp[i] + 1, dp[i + 1])

print(dp[N])


# 실행 결과: 성공(메모리:39068kb, 시간:892ms)