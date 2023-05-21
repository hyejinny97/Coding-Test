# https://www.acmicpc.net/problem/2164
# 문제2164번.카드2
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 카드 N장
- 1 ≤ N ≤ 500,000
'''



# 출력
'''
1. 남게 되는 카드의 번호를 출력
- 카드는 차례로 1부터 N까지의 번호가 붙어 있음
- 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
'''



# 코드
import sys
from collections import deque

sys.stdin = open('input_text/2164.txt')

N = int(input())

cards = deque(range(1, N + 1))
while len(cards) > 1:
    cards.popleft()
    if len(cards) > 1:
        cards.append(cards.popleft())

print(cards[0])


# 실행 결과: 성공(메모리:37480kb, 시간:3704ms)