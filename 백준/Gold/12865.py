# https://www.acmicpc.net/problem/12865
# 문제12865번.평범한 배낭
# 시간: 2초, 메모리: 512MB



# 입력
'''
1. 물품의 수 N, 준서가 버틸 수 있는 무게 K
- 1 ≤ N ≤ 100
- 1 ≤ K ≤ 100,000
2. N개의 줄에 거쳐 각 물건의 무게 W, 해당 물건의 가치 V
- 1 ≤ W ≤ 100,000
- 0 ≤ V ≤ 1,000
'''



# 출력
'''
1. 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력
'''



# 코드

# 접근방법
'''
참고) https://claude-u.tistory.com/208
dp[i] = max(현재 물건 가치 + dp[이전 물건][제한 무게 - 현재 물건 무게], dp[이전 물건][제한 무게])
'''
import sys

sys.stdin = open('input_text/12865.txt')

N, K = map(int, input().split())

W_V = []  # [[weight, value]]
for _ in range(N):
    W, V = map(int, input().split())
    W_V.append([W, V])

dp = [[0] * (K + 1)]   # 2차원 배열(row: 무게, col: 무게제한, value: 가치합 최댓값)
for weight, value in W_V:
    row = [0]
    for weight_limit in range(1, K + 1):
        if weight <= weight_limit:
            row.append(max(value + dp[-1][weight_limit - weight], dp[-1][weight_limit]))
        else:
            row.append(dp[-1][weight_limit])
    dp.append(row)

print(dp[-1][-1])


# 실행 결과: 성공 - 50점(메모리:282468kb, 시간:4504ms)