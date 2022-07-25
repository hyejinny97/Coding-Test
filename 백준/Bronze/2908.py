# https://www.acmicpc.net/problem/2908
# 문제2908번.상수
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 세자리수 A, B
- 0은 포함되어 있지 않음
'''



# 출력
'''
1. 수 A와 B를 각각 뒤집은 후, 크기 비교해 큰 수를 출력
'''



# 코드
import sys

sys.stdin = open("input_text/1_상수.txt")

# 세자리수 2개를 입력 받아 변수 A,B에 할당
A, B = input().split()

# A, B 값 뒤집은 후 크기 비교
print(B[::-1] if A[::-1] < B[::-1] else A[::-1])



# 실행결과(메모리:30840KB, 시간:68ms)