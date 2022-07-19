# 문제2070.큰 놈, 작은 놈, 같은 놈
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 테스트케이스 개수 T
2. 2개의 수
- 0 <= 정수 <= 10000
'''

# 출력
'''
각 줄은 
1. #테스트케이스 
2. 2개의 정수의 크기를 비교하여 등호 또는 부등호
1 + 2 형식으로 출력
'''

# 코드
import sys

sys.stdin = open('SWEA/input_text/2070.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    if a == b:
        result = '='
    elif a > b:
        result = '>'
    else:
        result = '<' 
    print(f'#{test_case} {result}')

# 실행 결과: 성공(메모리:56,940 kb , 시간:135 ms)