# 문제1926.간단한 369게임
# 시간: 4초, 메모리: 256MB

# 입력
'''
1. 정수 N
- 10 <= N <= 1,000
'''

# 출력
'''
1. 1부터 N까지의 숫자를 출력하는데, 숫자 중 3/6/9가 들어가면 해당 숫자가 들어가는 개수만큼 하이픈(-)을 출력한다
'''

# 코드 1
import sys

sys.stdin = open('SWEA/input_text/1926.txt', 'r')

N = int(input())
for num in range(1, N + 1):
    # 정수 내 3/6/9 존재 여부 및 갯수 파악
    clap = 0   # 정수 내 3/6/9 갯수
    for char in str(num):
        if char in '369':
            clap += 1
    
    print('-' * clap if clap else num, end=' ')

# 실행 결과: 성공(메모리:56,936 kb, 시간:132 ms)


# 코드 2
sys.stdin = open('SWEA/input_text/1926.txt', 'r')

N = int(input())
for num in range(1, N + 1):
    # 정수 내 3/6/9 존재 여부 및 갯수 파악
    clap = 0   # 정수 내 3/6/9 갯수
    rst = num
    while num:
        n = num % 10
        if n == 3 or n == 6 or n == 9:
            clap += 1
        num //= 10
    
    print('-' * clap if clap else rst, end=' ')

# 실행 결과: 성공(메모리:56,920 kb, 시간:131 ms)