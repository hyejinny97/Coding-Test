# https://www.acmicpc.net/problem/11047
# 문제11047번.동전 0
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 동전은 총 N종류, 가치의 합을 K
- 1 ≤ N ≤ 10
- 1 ≤ K ≤ 100,000,000
2. N개의 줄에 동전의 가치 Ai가 오름차순으로 주어짐
- 1 ≤ Ai ≤ 1,000,000
'''



# 출력
'''
1. K원을 만드는데 필요한 동전 개수의 최솟값을 출력
'''



# 코드
import sys

sys.stdin = open('input_text/11047.txt')

N, K = map(int, input().split())
moneys = [int(input()) for _ in range(N)]

cnt = 0  # 동전 개수
for money in moneys[::-1]:
    cnt += K // money
    K %= money

print(cnt)


# 실행 결과: 성공 - 50점(메모리:31256kb, 시간:40ms)