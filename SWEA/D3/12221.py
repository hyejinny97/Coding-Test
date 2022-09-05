# 문제12221번.구구단2
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 두 정수 A, B
- 1 <= A, B <= 20
'''



# 출력
'''
1. #{테스트케이스} {결과}
- A, B가 1 이상 9 이하이면 곱을 출력
- A, B가 10 이상이면 -1을 출력
'''



# 코드
import sys

sys.stdin = open('../input_text/12221.txt')

T = int(input())
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    
    # A, B 둘 중 하나라도 10 이상인 경우
    if A >= 10 or B >= 10:
        print(f'#{test_case} -1')
    else: 
        print(f'#{test_case} {A * B}')



# 실행 결과: 성공(메모리:58,764 kb, 시간:153 ms)