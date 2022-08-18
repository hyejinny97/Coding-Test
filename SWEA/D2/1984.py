# 문제1984번.중간 평균값 구하기
# 시간: 30초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 10개의 수
- 0 <= 정수 <= 10,000
'''



# 출력
'''
1. #{테스트케이스} {최대 수와 최소 수를 제외한 나머지의 평균값}
- 평균값은 소수점 첫째 자리에서 반올림
'''



# 코드 1
import sys

sys.stdin = open('../input_text/1984.txt')

T = int(input())
for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))

    # 최대 수와 최소 수 찾기, 전체 수를 합하기
    max_num, max_idx = 0, None
    min_num, min_idx = 10000, None
    sum_nums = 0
    for i in range(len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
            max_idx = i
        elif nums[i] < min_num:
            min_num = nums[i]
            min_idx = i
        sum_nums += nums[i]
    
    # 최대 수와 최소 수를 제외한 평균값 구하기
    print(f'#{test_case} {int(round((sum_nums - nums[max_idx] - nums[min_idx]) / 8, 0))}')
   


# 실행 결과: 성공(메모리:56,928 kb, 시간:144 ms)



# 코드 2
import sys

sys.stdin = open('../input_text/1984.txt')

T = int(input())
for test_case in range(1, T + 1):
    # 최대 수와 최소 수를 제외한 수
    nums = sorted(map(int, input().split()))[1:-1]

    # 최대 수와 최소 수를 제외한 평균값 구하기
    print(f'#{test_case} {round(sum(nums) / 8)}')
   


# 실행 결과: 성공(메모리:56,672 kb, 시간:133 ms)