# https://www.acmicpc.net/problem/10951
# 문제10951번.A + B - 4
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 여러 줄에 걸쳐 정수 A, B가 주어짐
- 1 < A, B < 10
'''



# 출력
'''
1. 각 줄마다 A + B 결과 출력
'''



# 코드
import sys

sys.stdin = open('input_text/10951.txt')

lines = sys.stdin.readlines()
for line in lines:
    print(sum(map(int, line.split())))


# 실행 결과: 성공(메모리:31256kb, 시간:40ms)