# 문제1948.날짜 계산기
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 테스트케이스 갯수 T
2. 날짜 2개 (월, 일, 월, 일)
- 1 <= 월 <= 12
- 두번째 날짜는 항상 첫번째 날짜보다 크게 주어짐
'''

# 출력
'''
1. #테스트케이스
2. 두번째 날짜가 첫번째 날짜의 몇일째인지 출력
'''

# 코드 1 - 각 달의 날짜를 일일이 더해줌
import sys

sys.stdin = open('SWEA/input_text/1948.txt', 'r')

days = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)   # 각 달의 일수

T = int(input())
for test_case in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    rst = 0
    # 일단 m1부터 m2까지 일수를 모두 더해줌
    for m in range(m1, m2 + 1):
        rst += days[m]
    
    # d1, d2만큼 빼주기
    rst -= d1 + (days[m2] - d2)
 
    print(f'#{test_case} {rst + 1}')

# 실행 결과: 성공(메모리:56,924 kb, 시간:134 ms)



# 코드 2 - accumulate()를 이용해 각 달의 날짜를 더한 후 계산
from itertools import accumulate

sys.stdin = open('SWEA/input_text/1948.txt', 'r')

days = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
acc_days = tuple(accumulate(days))

T = int(input())
for test_case in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    # m1부터 m2까지 일수를 더한 값
    rst = acc_days[m2] - acc_days[m1 - 1]

    # d1, d2만큼 빼주기
    rst -= d1 + (days[m2] - d2)
 
    print(f'#{test_case} {rst + 1}')

# 실행 결과: 성공(메모리:56,944 kb, 시간:163 ms)