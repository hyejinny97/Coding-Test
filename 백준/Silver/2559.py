# https://www.acmicpc.net/problem/2559
# 문제2559번.수열
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 온도를 측정한 전체 날짜의 수 N, 합을 구하기 위한 연속적인 날짜의 수 K
- 2 <= K <= N <= 100,000
2. 매일 측정한 N개의 온도
- -100 <= 온도 <= 100 
'''



# 출력
'''
1. 온도의 수열에서 연속적인 K일의 온도의 합이 최대가 되는 값 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/2559.txt')

# 온도의 수열 누적합
N, K = map(int, input().split())
temp = [0] + list(map(int, input().split()))
for i in range(1, N + 1):
    temp[i] += temp[i - 1]

# 투포인터를 이용해 K일의 온도의 합이 최대가 되는 값 출력
max_sum = -100 * 100000
left = 0
right = left + K
while right <= N:
    max_sum = max(max_sum, temp[right] - temp[left])
    left += 1
    right += 1

print(max_sum)



# 실행 결과: 성공(메모리:39572kb, 시간:144ms)



# 코드 2
import sys

sys.stdin = open('input_text/2559.txt')

# 온도의 수열 입력 받기
N, K = map(int, input().split())
temp = list(map(int, input().split()))

# K일의 온도의 합이 최대가 되는 값 출력
max_sum = now = sum(temp[:K])
for i in range(K, N):
    now += temp[i] - temp[i - K]
    max_sum = max(max_sum, now)

print(max_sum)



# 실행 결과: 성공(메모리:39572kb, 시간:116ms)