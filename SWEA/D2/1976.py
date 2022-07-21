# 문제1976.시각 덧셈
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 테스트 케이스 개수 T
2. 4개의 정수(시, 분, 시, 분)
- 1 <= 시 <= 12
- 0 <= 분 <= 59
'''

# 출력
'''
1. #테스트케이스
2. 두개의 시각을 더한 값을 시, 분으로 출력
'''

# 코드 
import sys

sys.stdin = open('SWEA/input_text/1976.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    # 13시에 도달하면 다시 1로 되돌려야 함
    hour = 12 if (h1 + h2 + (m1 + m2) // 60) % 12 == 0 else (h1 + h2 + (m1 + m2) // 60) % 12 
    # 60분에 도달하면 다시 0으로 되돌려야 함
    minute = (m1 + m2) % 60
    print(f'#{test_case} {hour} {minute}')

# 실행 결과: 성공(메모리:56,704 kb, 시간:129 ms)