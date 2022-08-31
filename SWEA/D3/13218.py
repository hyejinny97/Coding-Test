# 문제13218번.조별과제
# 시간: 3초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 학생의 수
- 1 <= N <= 1,000
'''



# 출력
'''
1. #{테스트케이스} {3명 이상의 학생으로 구성된 조의 수의 최댓값}
'''



# 코드
import sys

sys.stdin = open('../input_text/13218.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    print(f'#{test_case} {N // 3}')



# 실행 결과: 성공(메모리:62,496 kb, 시간:310 ms)