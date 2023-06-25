# https://www.acmicpc.net/problem/11053
# 문제11053번.가장 긴 증가하는 부분 수열
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 수열 A의 크기 N
- 1 ≤ N ≤ 1,000
2. 수열 A를 이루고 있는 Ai
- 1 ≤ Ai ≤ 1,000
'''



# 출력
'''
1. 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/11053.txt')

N = int(input())
nums = list(map(int, input().split()))

dp = [1] * N   # value: 현재 위치까지 부분 수열 최대 길이

for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))
    

# 실행 결과: 성공(메모리:31256kb, 시간:104ms)