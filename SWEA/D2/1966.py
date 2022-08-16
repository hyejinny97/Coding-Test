# 문제1966번.숫자를 정렬하자
# 시간: 30초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 개수 T
2. N개의 숫자
- 5 <= N <= 50
'''



# 출력
'''
1. #{테스트케이스} {N개의 숫자열을 오름차순으로 정렬해 출력}
'''



# 코드 
import sys

sys.stdin = open('../input_text/1966.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    print(f'#{test_case}', *nums)



# 실행 결과: 성공(메모리:56,672 kb, 시간:128 ms)