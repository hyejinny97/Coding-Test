# 문제14692번.통나무 자르기
# 시간: 3초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 통나무의 길이 N미터
- 2 <= N <= 1,000,000,000
'''



# 출력
'''
1. #{테스트케이스} {Alice가 이기면 “Alice”, 아니면 “Bob” 을 출력}
- 게임은 Alice가 먼저 시작하며 그 이후 둘이 번갈아가면서 턴을 가짐
- 잘린 통나무가 모두 자연수(1 이상의 정수) 미터 길이를 가지도록 잘라야함
'''



# 코드
import sys

sys.stdin = open('../input_text/14692.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # 통나무 길이가 짝수이면, Alice 승
    if N % 2 == 0:
        print(f'#{test_case} Alice')
    # 통나무 길이가 홀수이면, Bob 승
    else:
        print(f'#{test_case} Bob')



# 실행 결과: 성공(메모리:56,920 kb, 시간:147 ms)