# https://www.acmicpc.net/problem/2776
# 문제2776번.암기왕
# 시간: 2초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 수첩 1에 적은 정수 갯수 N
- 1 <= N <= 1,000,000
3. 수첩 2에 적은 정수 갯수 M
- 1 <= M <= 1,000,000
'''



# 출력
'''
1. 수첩 2에 적힌 M개의 숫자 순서대로, 수첩 1에 있으면 1을 출력, 없으면 0을 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/2776.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    nums_N = set(map(int, input().split()))   # set은 탐색의 시간복잡도 = O(1)
    M = int(input())
    nums_M = list(map(int, input().split()))

    for m in nums_M:
        if m in nums_N:
            print(1)
        else:
            print(0)



# 실행 결과: 성공(메모리:220876kb, 시간:1504ms)