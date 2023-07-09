# https://www.acmicpc.net/problem/13305
# 문제13305번.주유소
# 시간: 2초, 메모리: 512MB



# 입력
'''
1. 도시의 개수 N
- 2 ≤ N ≤ 100,000
2. 인접한 두 도시를 연결하는 도로의 길이 N-1개
- 1 <= N-1개 총 길이 <= 1,000,000,000
3. 주유소의 리터당 가격 N개
- 1 <= 가격 <= 1,000,000,000
'''



# 출력
'''
1. 제일 왼쪽 도시에서 제일 오른쪽 도시로 가는 최소 비용을 출력
'''



# 코드

# 접근방법
'''
기름 가격이 낮을 때 많이 사야 함
'''
import sys

sys.stdin = open('input_text/13305.txt')

N = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

ordered_prices = []
for i in range(N):
    ordered_prices.append([prices[i], i])
ordered_prices.sort(key=lambda x: (x[0], x[1]))

start, end = 0, N
tot_price = 0
for i in range(N):
    price, idx = ordered_prices[i]
    if not (start <= idx <= end):
        continue

    tot_price += price * sum(roads[idx:end])
    end = idx

print(tot_price)


# 실행 결과: 성공(메모리:58964kb, 시간:260ms)