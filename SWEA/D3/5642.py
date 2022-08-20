# 문제5642번.합
# 시간: 4초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
- 1 <= T <= 20
2. 숫자 N
- 3 <= N <= 100,000
3. N개의 정수 
- -1,000 <= N <= 1,000
'''



# 출력
'''
1. #{테스트케이스} {연속된 정수의 합의 최댓값}
'''



# 코드 1
import sys

sys.stdin = open('../input_text/5642.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    max_subsum = 0   # 구간합 최댓값
    size = 1   # 슬라이싱 사이즈
    while size < N:
        # 슬라이딩 윈도우로 탐색하면서 값 합하기
        for i in range(N - size):
            subsum = sum(nums[i:i + size])
            max_subsum = max(max_subsum, subsum)   # 최대 구간합 갱신
        
        size += 1
    
    print(f'#{test_case} {max_subsum}')



# 실행 결과: 실패(21개 중 2개만 통과, 시간초과)



# 코드 2
import sys
from itertools import accumulate

sys.stdin = open('../input_text/5642.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(accumulate(map(int, [0] + input().split())))   # 누적합

    # 순회하면서 투 포인터 내 구간합 구하기
    max_subsum = 0   # 구간합 최댓값
    for left in range(1, N):
        for right in range(left, N + 1):
            max_subsum = max(max_subsum, nums[right] - nums[left - 1])
    
    print(f'#{test_case} {max_subsum}')



# 실행 결과: 실패(21개 중 4개만 통과, 시간초과)



# 코드 3
import sys

sys.stdin = open('../input_text/5642.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # 숫자 누적합
    nums = [0]
    sum_nums = 0
    for num in input().split():
        sum_nums += int(num)
        nums.append(sum_nums)

    # 순회하면서 투 포인터 내 구간합 구하기
    max_subsum = 0   # 구간합 최댓값
    for left in range(1, N):
        for right in range(left, N + 1):
            max_subsum = max(max_subsum, nums[right] - nums[left - 1])
    
    print(f'#{test_case} {max_subsum}')



# 실행 결과: 실패(21개 중 4개만 통과, 시간초과)



# 코드 4
import sys

sys.stdin = open('../input_text/5642.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    max_val = nums[0]

    for i in range(N - 1):
        # 다음 값이랑 합쳤을 때 음수가 된다면, 더해줄 필요 없음
        if nums[i] >= 0 and (nums[i] + nums[i+1]) >= 0:
            nums[i+1] += nums[i]
        max_val = max(max_val, nums[i+1])   # 누적된 다음 값과 비교해 갱신
    
    print(f'#{test_case} {max_val}')



# 실행결과(메모리:121,104 kb, 시간:534 ms)