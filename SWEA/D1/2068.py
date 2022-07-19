# 문제2068.최대수 구하기
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 테스트케이스 개수 T
2. 10개의 수
- 0 <= 정수 <= 10000
'''

# 출력
'''
각 줄은 
1. #테스트케이스 
2. 10개의 수 중 가장 큰 수
1 + 2 형식으로 출력
'''

# 코드
import sys

sys.stdin = open('SWEA/input_text/2068.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case} {max(map(int, input().split()))}')

# 실행 결과: 성공(메모리:56,672 kb, 시간:136 ms)