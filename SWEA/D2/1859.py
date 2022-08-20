# 문제1859번.백만장자 프로젝트
# 시간: 30초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 연속된 N일
- 2 <= N <= 1,000,000
3. 각 날의 매매가 N개
- 0 < 매매가 <= 10,000
'''



# 출력
'''
1. #{테스트케이스} {차익으로 벌수있는 최대 이익}
- 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있음
- 하루에 최대 1만큼 구입 가능
- 판매는 얼마든지 할 수 있음
'''



# 접근 방법
'''
- 매매가가 가장 높은 날에 팔아야 수익이 최대
- 당연히 팔기 전에 사야 함
- 즉, 매매가가 가장 높은 날 이전 모든 날의 물건을 사야함

<접근 방법 1>
- 부분 집합으로 접근 => 시간 복잡도: 2^n
- N = 3이면, 경우의 수는 2 x 2 x 2 = 8가지
- 1일: 사거나/팔거나, 2일: 사거나/팔거나, 3일: 사거나/팔거나

<접근 방법2>
- max()값을 구해 그 날 이전에 물건 모두 사고 차익 보기를 반복 => 시간 복잡도: (최악의 경우) n^2

<접근 방법3>
- 모든날의 매매가를 내림차순으로 정렬한 후, 큐를 이용해 pop()해가면서 매매가가 최고인 날보다 작은 날의 물건만 사 차익 보기를 반복 => 시간 복잡도: 정렬의 경우만 NlogN + 순회 n^2
'''



# 코드 1
import sys
from collections import deque

sys.stdin = open('../input_text/1859.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    
    # 매매가를 기준으로 내림차순 정렬된 덱 자료형 만들기
    prices = []   # (매매가, 날짜)
    day = 1 
    for price in input().split():
        prices.append((int(price), day))
        day += 1
    prices.sort(reverse=True)
    prices = deque(prices)   

    # 매매가가 최고인 날을 기준으로 순회하면서 차익 계산
    tot_profit = 0
    while prices:
        high = prices.popleft()   # 현재 매매가가 최고인 날 => (매매가, 날짜)
        # 아직 매매하지 않은 날들을 순회하면서, 자신보다 앞선 날인 경우 사서 차익보기
        for _ in range(len(prices)):   
            low = prices.popleft()  
            if high[1] > low[1]:
                tot_profit += high[0] - low[0]
            else:
                prices.append(low)
    
    print(f'#{test_case} {tot_profit}')



# 실행 결과: 실패(10개 중 9개만 통과, 런타임 에러)



# 코드 2
import sys

sys.stdin = open('../input_text/1859.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))

    # 매매가가 최고인 날을 찾아 이전의 모든날 구매해 차익 계산
    tot_profit = 0
    while prices:
        # 매매가가 최고인 날 찾기
        high_price, high_idx = 0, None
        for i in range(len(prices)):
            if high_price < prices[i]:
                high_price = prices[i]
                high_idx = i
        
        # 이전의 모든날 구매해 차익 계산
        tot_profit += high_price * high_idx - sum(prices[:high_idx])
        
        # 매매한 날들은 제외한 후 재할당
        prices = prices[high_idx + 1:]
    
    print(f'#{test_case} {tot_profit}')



# 실행결과(메모리:259,704 kb, 시간:1,789 ms)



# 코드 3
import sys

sys.stdin = open('../input_text/1859.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    prices = input().split()

    # 매매가가 높은 날을 기준으로 이전의 모든날 구매해 차익 계산
    tot_profit = 0
    high = 0   # 매매가가 높은 날
    while prices:
        pop_val = int(prices.pop())
        if pop_val > high:    # 매매가가 높은 날 갱신
            high = pop_val
        else:   # 차익 계산
            tot_profit += high - pop_val
    
    print(f'#{test_case} {tot_profit}')



# 실행결과(메모리:217,740 kb, 시간:986 ms)