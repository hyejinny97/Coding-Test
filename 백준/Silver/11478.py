# https://www.acmicpc.net/problem/11478
# 문제11478번.서로 다른 부분 문자열의 개수
# 시간: 1초, 메모리: 512MB



# 입력
'''
1. 문자열 S
- 알파벳 소문자로만 이루어짐
- 0 < S 길이 <= 1,000
'''



# 출력
'''
1. S의 서로 다른 부분 문자열의 개수를 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/11478.txt')

S = input()

sub_S = set()   # 서로 다른 부분 문자열
for long in range(1, len(S) + 1):
    for start in range(0, len(S) - long + 1):
        sub_S.add(S[start : start + long])

print(len(sub_S))


# 실행 결과: 성공(메모리:240716kb, 시간:520ms)