# https://www.acmicpc.net/problem/2565
# 문제2565번.전깃줄
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 두 전봇대 사이의 전깃줄의 개수
- 1 ≤ N ≤ 100
2. 전깃줄이 A전봇대와 연결되는 위치의 번호와 B전봇대와 연결되는 위치의 번호
- 1 ≤ 위치 번호 ≤ 500
- 같은 위치에 두 개 이상의 전깃줄이 연결될 수 없음
'''



# 출력
'''
1. 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 출력
'''



# 코드 

# 접근방법
'''
전기줄이 겹치지 않게 전기줄 제거 개수 최솟값
= 전체 전기줄 개수 - 전기줄이 겹치지 않게 전기줄 선택 개수 최댓값 
'''
import sys

sys.stdin = open('input_text/2565.txt')

N = int(input())
lines = {}   # {start: end}
max_num = 0  # 전기줄 위치 번호 최댓값
for _ in range(N):
    start, end = map(int, input().split())
    lines[start] = end
    max_num = max(max_num, start, end)

dp = [1] * (max_num + 1)   # value: 현재 위치까지 겹치지 않게 선택한 전깃줄 최댓값

for i in range(2, max_num + 1):
    if not lines.get(i):
        continue

    for j in range(i):
        if not lines.get(j):
            continue

        # 자신의 앞 전기줄과 교차되는 경우
        if (j < i < lines[j]) and (i - lines[i]) * (j - lines[j]) < 0:
            continue
        if (i < j) and (lines[i] > lines[j]):
            continue
        if (i > j) and (lines[j] > lines[i]):
            continue

        # 자신의 앞 전기줄과 교차되지 않는 경우
        dp[i] = max(dp[j] + 1, dp[i])

print(N - max(dp))


# 실행 결과: 성공(메모리:31256kb, 시간:72ms)