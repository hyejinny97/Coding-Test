# 문제2056.연월일 달력
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 테스트케이스 개수 T
2. 연월일 순으로 구성된 8자리 날짜
'''

# 출력
'''
각 줄은
1. #테스트케이스
2. 올바른 날짜인 경우, 'YYYY/MM/DD'형식으로 전환
- 올바르지 않은 날짜인 경우, -1을 출력
1 + 2 형식으로 출력 
'''

# 코드
import sys

sys.stdin = open('SWEA/input_text/2056.txt', 'r')

T = int(input())
date = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}   # {월: 마지막 일}
for test_case in range(1, T+1):
    nums = input()
    year = nums[0:4]
    month = nums[4:6]
    day = nums[6:8]
    if int(month) in date and int(day) <= date[int(month)]:
        print(f'#{test_case} {year}/{month}/{day}')
    else:
        print(f'#{test_case} -1')

# 실행 결과: 성공(메모리:56,940 kb, 시간:140 ms)