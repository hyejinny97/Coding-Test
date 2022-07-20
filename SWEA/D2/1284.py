# 문제1284.수도 요금 경쟁
# 시간: 4초, 메모리: 256MB

# 입력
'''
1. 테스트 케이스 개수 T
2. 자연수 P, Q, R, S, W
- 1 <= P,Q,R,S,W <= 10000
- A회사: 1리터당 P원의 돈을 냄
- B회사: 기본요금 Q원 + 월간사용량이 R리터 이상인 경우, 1리터당 S원의 돈을 냄
- W리터: 한 달간 사용하는 수도의 양
'''

# 출력
'''
1. #테스트케이스
2. A사와 B사 각각 종민이가 내야하는 수도 요금 중 더 저렴한 요금을 골라 출력
'''

# 코드
import sys

sys.stdin = open('SWEA/input_text/1284.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    company_A = W * P
    company_B = Q if W < R else Q + (W - R) * S
    print(f'#{test_case} {company_B if company_A > company_B else company_A}')

# 실행 결과: 성공(메모리:56,944 kb, 시간:135 ms)