# https://www.acmicpc.net/problem/11659
# 문제11659번.구간 합 구하기4
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 수의 개수 N, 합을 구해야 하는 횟수 M
- 1 ≤ N ≤ 100,000
- 1 ≤ M ≤ 100,000
2. N개의 수
- 0 < N <= 1,000
3. M개의 줄에 합을 구해야 하는 구간 i와 j
- 1 ≤ i ≤ j ≤ N
'''



# 출력
'''
1. M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/11659.txt')

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

# 누적합
accumulated_nums = [0]
for i in range(N):
    accumulated_nums.append(accumulated_nums[-1] + nums[i])

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(accumulated_nums[end] - accumulated_nums[start - 1])


# 실행 결과: 성공(메모리:31256kb, 시간:80ms)

