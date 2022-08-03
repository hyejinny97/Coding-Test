# https://www.acmicpc.net/problem/14720
# 문제14720번.우유 축제
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 우유 가게의 수 N
- 1 <= N <= 1,000
2. N개의 우유가게의 정보
- 0: 딸기우유만 파는 가게
- 1: 초코우유만 파는 가게
- 2: 바나나우유만 파는 가게
'''



# 출력
'''
1. 마실 수 있는 우유의 최대 갯수
<우유 마시는 규칙>
1. 딸기(0)
2. 딸기(0) -> 초코(1)
3. 초코(1) -> 바나나(2)
4. 바나나(2) -> 딸기(0)
- 즉, 0 -> 1 -> 2 -> 0순으로 우유를 마셔야 함
'''



# 코드
import sys

sys.stdin = open('input_text/14720.txt')

N = int(input())
stores = map(int, input().split())

milk = 0   # 맨 처음엔 딸기우유를 마심
for store in stores:
    if store == milk % 3:
        milk += 1

print(milk)



# 실행 결과: 성공(메모리:30840kb, 시간:68ms)