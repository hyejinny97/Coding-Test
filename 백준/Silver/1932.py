# https://www.acmicpc.net/problem/1932
# 문제1932번.정수 삼각형
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 삼각형의 크기 n
- 1 ≤ n ≤ 500
2. 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어짐
'''



# 출력
'''
1. 합이 최대가 되는 경로에 있는 수의 합을 출력
- 단, 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있음
'''



# 코드 

# 접근방법
'''
- 현재까지의 수의 합 최댓값 = 이전까지의 수의 합 최댓값 + 현재의 수
'''
import sys

sys.stdin = open('input_text/1932.txt')

N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):       # i층
    for j in range(i + 1):  # j번째
        # 각 층의 젤 왼쪽에 존재하는 수인 경우, 오른쪽 대각선만 존재
        if j == 0:  
            nums[i][j] += nums[i - 1][j]
        # 각 층의 젤 오른쪽에 존재하는 수인 경우, 왼쪽 대각선만 존재
        elif j == i:  
            nums[i][j] += nums[i - 1][j - 1]
        else:
            nums[i][j] += max(nums[i - 1][j - 1], nums[i - 1][j])

print(max(nums[-1]))


# 실행 결과: 성공(메모리:35616kb, 시간:148ms)