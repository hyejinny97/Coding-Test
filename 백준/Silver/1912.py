# https://www.acmicpc.net/problem/1912
# 문제1912번.연속합
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 정수 n
- 1 ≤ n ≤ 100,000
2. n개의 정수로 이루어진 수열
- -1,000 <= 정수 <= 1,000
'''



# 출력
'''
1. 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 출력
- 단, 수는 한 개 이상 선택해야 한다.
'''



# 코드 

# 접근방법
'''
참고) 카데인 알고리즘: https://sustainable-dev.tistory.com/23
- 계속해서 부분 최댓값을 구해나가는 과정!
- 즉, '자신'과 '자신 앞까지의 부분 최댓값 + 자신'을 비교해 더 높은 수를 선택

nums   = 10 -4 3 1  5   6 -35 12 21 -1
submax = 10  6 9 10 15 21 -14|12 33 32  
'''
import sys

sys.stdin = open('input_text/1912.txt')

N = int(input())
nums = list(map(int, input().split()))

local_max = nums[0]       # 자신 앞까지의 부분 최댓값
global_max = nums[0]      # 최종 최댓값
for i in range(1, N):
    cur_num = nums[i]
    local_max = max(cur_num, local_max + cur_num)
    global_max = max(global_max, local_max)

print(global_max)


# 실행 결과: 성공(메모리:38964kb, 시간:112ms)