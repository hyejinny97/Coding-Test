# https://www.acmicpc.net/problem/11054
# 문제11054번.가장 긴 바이토닉 부분 수열
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
1. 수열 A의 가장 긴 바이토닉 부분 수열의 길이를 출력

<바이토닉 수열>
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족
'''



# 코드 

# 접근방법
'''
1. idx = 0 ~ N 순서대로 가장 긴 증가하는 부분 수열 최대 길이 구하기
2. idx = N ~ 0 순서대로 가장 긴 증가하는 부분 수열 최대 길이 구하기
3. 위 각 dp 값을 더한 최댓값 = 가장 긴 바이토닉 부분 수열
'''
import sys

sys.stdin = open('input_text/11054.txt')

def lis(nums):  # 가장 긴 증가하는 부분 수열을 구해주는 함수
    dp = [1] * N   # value: 현재 위치까지 가장 긴 증가하는 부분 수열 최대 길이
    for i in range(1, N):
        for j in range(i):
            if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1

    return dp


N = int(input())
nums = list(map(int, input().split()))

dp = lis(nums)
reverse_dp = lis(nums[::-1])[::-1]

print(max((dp[i] + reverse_dp[i]) for i in range(N)) - 1)
    

# 실행 결과: 성공(메모리:31256kb, 시간:100ms)