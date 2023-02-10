# https://www.acmicpc.net/problem/2675
# 문제2675번.문자열 반복
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 테스트 케이스의 개수 T
- 1 ≤ T ≤ 1,000
2. T개 줄에 반복 횟수 R, 문자열 S
- 1 ≤ R ≤ 8
- 1 <= S <= 20
- S에는 QR Code "alphanumeric" 문자만 들어있음
- "alphanumeric" 문자 = 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:
'''



# 출력
'''
1. S의 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2675.txt')

T = int(input())

for _ in range(T):
    R, S = input().split()
    P = ''
    for char in S:
        P += char * int(R)
    print(P)



# 실행결과(메모리:31256KB, 시간:44ms)