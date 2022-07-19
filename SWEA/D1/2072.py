# 문제2072.홀수만 더하기
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 테스트케이스 개수 T
2. 10개의 수
- 0 <= 정수 <= 1000
'''

# 출력
'''
각 줄은 
1. #테스트케이스 
2. 10개의 수 중 홀수만 더한값
1 + 2 형식으로 출력
'''

# 코드
import sys

sys.stdin = open('SWEA/input_text/2072.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    print(f'#{test_case} {sum(filter(lambda x: x % 2 == 1, nums))}')

# 실행 결과: 성공(메모리:56,672 kb , 시간:127 ms)