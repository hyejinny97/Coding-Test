# https://www.acmicpc.net/problem/10816
# 문제10816번.숫자카드2
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 상근이가 가지고 있는 숫자 카드의 갯수 N
- 1 <= N <= 500,000
2. 숫자 카드에 적혀있는 정수
- -10,000,000 <= 정수 <= 10,000,000
3. 상근이 카드와 비교할 숫자 카드의 갯수 M개
- 1 <= M <= 500,000
4. 숫자 카드에 적혀있는 정수
- -10,000,000 <= 정수 <= 10,000,000
'''



# 출력
'''
1. M개의 숫자 카드에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지 공백으로 구분해 출력
'''



# 코드
import sys
from collections import Counter

sys.stdin = open('input_text/10816.txt')

N = int(input())
have = Counter(input().split())

M = int(input())
compare = input().split()
for n in compare:
    print(have[n], end=' ')



# 실행 결과: 성공(메모리:125188kb, 시간:748ms)