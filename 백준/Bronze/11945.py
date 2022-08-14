# https://www.acmicpc.net/problem/11945
# 문제11945번.뜨거운 붕어빵
# 시간: 1초, 메모리: 32MB



# 입력
'''
1. 두 개의 정수 N, M
- 0 <= N, M <= 10
2. N개의 줄에 붕어빵의 모양
- 0: 공백
- 1: 붕어빵, 총 M개
'''



# 출력
'''
1. 주어진 붕어빵이 좌우로 뒤집힌 모양 출력
'''



# 코드
import sys

sys.stdin = open('input_text/11945.txt')

N, M = map(int, input().split())
for _ in range(N):
    row = input()
    print(row[::-1])



# 실행 결과: 성공(메모리:30840kb, 시간:72ms)