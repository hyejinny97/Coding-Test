# https://www.acmicpc.net/problem/2693
# 문제2693번.N번째 큰 수
# 시간: 1초, 메모리: 32MB



# 입력
'''
1. 테스트 케이스 수 T
- 1 <= T <= 1,000
2. 배열 A의 원소 10개
- 1 <= 원소 <= 1,000
'''



# 출력
'''
1. 한 줄에 하나씩 배열 A에서 3번째 큰 값을 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2693.txt')

T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[-3])



# 실행 결과: 성공(메모리:30840kb, 시간:164ms)