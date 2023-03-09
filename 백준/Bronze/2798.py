# https://www.acmicpc.net/problem/2798
# 문제2798번.블랙잭
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 카드의 개수 N, 양의 정수 M
- 3 ≤ N ≤ 100
- 10 ≤ M ≤ 300,000
2. M개의 카드
- 0 < 카드 <= 100,000
'''



# 출력
'''
1. M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2798.txt')

N, M = map(int, input().split())
cards = list(map(int, input().split()))

min_diff = 300000   # 근사값
for i in range(len(cards)):
    for j in range(i + 1, len(cards)):
        for k in range(j + 1, len(cards)):
            sum_3 = cards[i] + cards[j] + cards[k]
            diff = abs(M - sum_3)
            if sum_3 <= M and diff < min_diff:
                min_diff = diff

print(M - min_diff)


# 실행 결과: 성공(메모리:31256kb, 시간:96ms)