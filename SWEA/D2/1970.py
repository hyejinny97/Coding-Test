# 문제1970번.쉬운 거스름돈
# 시간: 30초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 개수 T
2. 거슬러주어야할 금액 N원
- 10 <= N <= 1,000,000
- N의 마지막 자릿수는 항상 0
'''



# 출력
'''
1. #{테스트케이스} {각 돈의 종류마다 필요한 갯수 출력}
- 금액이 높은 돈을 우선적으로 계산해 거스름돈의 갯수가 최소가 되게 함
'''



# 코드 1
import sys

sys.stdin = open('../input_text/1970.txt', 'r')

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]   # 돈 8종류

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())   # 거슬러줘야하는 돈
    change = [0] * 8   # 거스름돈의 갯수

    for i in range(len(money)):
        while N - money[i] >= 0:
            change[i] += 1
            N -= money[i]
           
    print(f'#{test_case}')
    print(*change)



# 실행 결과: 성공(메모리:56,704 kb, 시간:133 ms)



# 코드 2
import sys

sys.stdin = open('../input_text/1970.txt', 'r')

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]   # 돈 8종류

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())   # 거슬러줘야하는 돈
    change = [0] * 8   # 거스름돈의 갯수

    for i in range(len(money)):
        n = N // money[i]
        if n > 0:
            N -= money[i] * n
        change[i] += n

    print(f'#{test_case}')
    print(*change)



# 실행 결과: 성공(메모리:56,672 kb, 시간:133 ms)