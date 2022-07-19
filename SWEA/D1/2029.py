# 문제2029.몫과 나머지 출력하기
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 테스트케이스 개수 T
2. 2개의 정수 a, b
- 1 <= 정수 <= 10000
'''

# 출력
'''
각 줄은
1. #테스트케이스
2. a를 b로 나눈 몫과 나머지
1 + 2 형식으로 출력 
'''

# 코드
import sys

sys.stdin = open('SWEA/input_text/2029.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    a, b = map(int, input().split())
    print(f'#{test_case} {a // b} {a % b}')

# 실행 결과: 성공(메모리:56,688 kb, 시간:127 ms)