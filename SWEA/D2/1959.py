# 문제1959번.두 개의 숫자열
# 시간: 30초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 개수 T
2. 배열 A의 크기 N, 배열 B의 크기 M
- 3 <= N, M <= 20
3. 배열 A
4. 배열 B
'''



# 출력
'''
1. #{테스트케이스} {서로 마주보는 숫자의 곱하고 합한 최댓값}
'''



# 코드 
import sys
from unittest import TestResult

sys.stdin = open('../input_text/1959.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))

    # 길이가 더 긴 배열을 기준으로 짧은 배열과 마주보게 하기
    long = arrA if N > M else arrB   # 긴 배열
    short = arrA if N < M else arrB   # 짧은 배열
    max_val = 0
    for i in range(0, len(long) - len(short) + 1):
        # 두 배열의 각 요소를 곱한 후 더하기
        sum_arr = 0
        for j in range(0, len(short)):
            sum_arr += long[i + j] * short[j]
        
        # 최댓값 갱신
        max_val = max(max_val, sum_arr)   
        
    print(f'#{test_case} {max_val}')



# 실행 결과: 성공(메모리:56,672 kb, 시간:128 ms)