# https://www.acmicpc.net/problem/2156
# 문제2156번.포도주 시식
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 포도주 잔의 개수 n
- 1 ≤ n ≤ 10,000
2. 각 줄에 포도주 잔에 들어있는 포도주의 양이 순서대로 주어짐
- 0 <= 포도주의 양 <= 1,000
'''



# 출력
'''
1. 최대로 마실 수 있는 포도주의 양을 출력

<포도주 시식 규칙>
- 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
- 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
'''



# 코드 

# 접근방법
'''
최대한 많은 포도주를 선택해야 많이 마실 수 있음
따라서, 연속해서 3잔은 마실 수 없으니까 최대 한 칸만 띄워서 선택해야 함
i번째 잔을 선택한 경우, (i-1)번째 잔, (i-2)번째 잔 중 하나를 선택한 것임

<점화식>
dp[i] = max(alcohol[i] + dp[i - 2], alcohol[i] + alcohol[i - 1] + dp[i - 3], dp[i - 1])
'''
import sys

sys.stdin = open('input_text/2156.txt')

N = int(input())
alcohol = [0] + [int(input()) for _ in range(N)]

dp = [0] + [0] * N   # idx: i번째 포도주 잔, value: 이 자리에 오기까지 마신 포도주 양 최댓값

if N <= 2:
    print(sum(alcohol[:N + 1]))
else:
    dp[1] = alcohol[1]
    dp[2] = sum(alcohol[:3])

    for i in range(3, N + 1):
        dp[i] = max(alcohol[i] + dp[i - 2], alcohol[i] + alcohol[i - 1] + dp[i - 3], dp[i - 1])

    print(dp[N])
    

# 실행 결과: 성공(메모리:31256kb, 시간:416ms)