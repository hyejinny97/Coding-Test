# https://www.acmicpc.net/problem/10430
# 문제10430번.나머지
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 세 수 A, B, C
- 2 <= A, B, C <= 10,000
'''



# 출력
'''
1. 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력
'''



# 코드
import sys

sys.stdin = open('input_text/10430.txt')

A, B, C = list(map(int, input().split()))
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B ) % C)
print(((A % C) * (B % C)) % C)


# 실행 결과: 성공(메모리:30840kb, 시간:76ms)