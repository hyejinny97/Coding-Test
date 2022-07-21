# 문제1945.간단한 소인수분해
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 테스트케이스 갯수 T
2. 정수 N
- 2 <= N <= 10,000,000 
'''

# 출력
'''
1. #테스트케이스
2. N = 2^a x 3^b x 5^c x 7^d x 11^e일때 a, b, c, d, e를 출력
'''

# 코드 
import sys

sys.stdin = open('SWEA/input_text/1945.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    primes = [2, 3, 5, 7, 11]
    rst = [0] * len(primes)
    # 2~11까지의 소수를 돌면서 각 소수로 N이 더이상 나누어 떨어지지 않을때까지 나누고 카운트 세기
    for i in range(len(primes)):
        while N % primes[i] == 0:
            N //= primes[i]
            rst[i] += 1
    
    print(f'#{test_case}', *rst, sep=' ')

# 실행 결과: 성공(메모리:56,924 kb, 시간:132 ms)