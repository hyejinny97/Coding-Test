# https://www.acmicpc.net/problem/10815
# 문제10815번.숫자 카드
# 시간: 2초, 메모리: 256MB



# 입력
'''
1. 상근이가 가지고 있는 숫자 카드의 개수 N
- 1 ≤ N ≤ 500,000
2. 숫자 카드에 적혀있는 N개의 정수
- -10,000,000 <= 정수 <= 10,000,000
- 같은 수가 적혀있는 경우는 없음
3. M
- 1 ≤ M ≤ 500,000
4. M개의 정수
- -10,000,000 <= 정수 <= 10,000,000
'''



# 출력
'''
1. M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력
'''



# 코드
import sys

sys.stdin = open('input_text/10815.txt')

N = int(input())
cards_N = set(map(int, input().split()))
M = int(input())
cards_M = map(int, input().split())

for card in cards_M:
    if card in cards_N:
        print(1, end=' ')
        continue
    print(0, end=' ') 


# 실행 결과: 성공(메모리:107848kb, 시간:656ms)