# 문제1986.지그재그 숫자
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 테스트 케이스 개수 T
2. 정수 N
- 1 <= N <= 10
'''

# 출력
'''
1. #테스트케이스
2. 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺀 후 최종 누적된 값
'''

# 코드
import sys

sys.stdin = open('SWEA/input_text/1986.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    rst = 0
    for n in range(1, N + 1):
        # 홀수인 경우 더함
        if n % 2 == 1:
            rst += n
        # 짝수인 경우 뺌
        else:
            rst -= n
    print(f'#{test_case} {rst}')

# 실행 결과: 성공(메모리:56,944 kb, 시간:128 ms)