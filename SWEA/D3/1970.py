# 문제1970번.쉬운 거스름돈
# 시간: 30초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 손님에게 거슬러 주어야 할 금액 N
- 10 <= N <= 1,000,000
- N의 마지막 자릿수는 항상 0
'''



# 출력
'''
1. #{테스트케이스} {각 돈의 종류마다 필요한 개수}
'''



# 코드 1
import sys

sys.stdin = open('../input_text/1970.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = [0] * 8   # 인덱스: 순서대로 50,000원~10원, 값: 거슬러줘야하는 갯수

    # 각 돈의 종류마다 필요한 개수 세기
    for i in range(8):
        while True:
            if N - money[i] < 0:
                break
            N -= money[i]
            change[i] += 1
    
    print(f'#{test_case}')
    print(*change)



# 실행 결과: 성공(메모리:56,940 kb, 시간:133 ms)



# 코드 2
import sys

sys.stdin = open('../input_text/1970.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = [0] * 8   # 인덱스: 순서대로 50,000원~10원, 값: 거슬러줘야하는 갯수

    # 각 돈의 종류마다 필요한 개수 세기
    for i in range(8):
        cnt = N // money[i]
        if cnt == 0:
            continue
        N %= money[i]
        change[i] += cnt
    
    print(f'#{test_case}')
    print(*change)



# 실행 결과: 성공(메모리:56,708 kb, 시간:133 ms)