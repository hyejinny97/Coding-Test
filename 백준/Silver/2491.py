# https://www.acmicpc.net/problem/2491
# 문제2491번.수열
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 수열의 길이 N
- 1 <= N <= 100,000
2. N개의 숫자
'''



# 출력
'''
1. 가장 긴 길이 출력
- 수열 안에서 연속해서 커지거나(같은 것 포함), 혹은 연속해서 작아지는(같은 것 포함) 수열 중 가장 길이가 긴 것을 찾아 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2491.txt')

N = int(input())
nums = list(map(int, input().split()))

max_increase = 1   # 상승 최댓값
max_decrease = 1    # 하강 최댓값
increase = 1
decrease = 1
for i in range(1, N):
    # 이전 수와 같은 경우
    if nums[i] == nums[i - 1]:
        increase += 1
        decrease += 1
        max_increase = max(max_increase, increase)
        max_decrease = max(max_decrease, decrease)
    # 이전 수보다 커진 경우 
    elif nums[i] > nums[i - 1]:
        increase += 1
        max_increase = max(max_increase, increase)
        decrease = 1   # 하강 초기화
    # 이전 수보다 작아진 경우
    elif nums[i] < nums[i - 1]:
        decrease += 1
        max_decrease = max(max_decrease, decrease)
        increase = 1   # 상승 초기화

print(max(max_increase, max_decrease))
        


# 실행 결과: 성공(메모리:32404kb, 시간:152ms)