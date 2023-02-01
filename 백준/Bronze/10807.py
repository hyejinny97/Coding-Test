# https://www.acmicpc.net/problem/10807
# 문제10807번.개수 세기
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 정수의 개수 N
- 1 ≤ N ≤ 100
2. N개의 정수가 공백으로 구분되어져 있음
3. 찾으려고 하는 정수 v
- -100 <= v <= 100
'''



# 출력
'''
1. N개의 정수 중에 v가 몇 개인지 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/10807.txt')

N = int(input())
nums = list(map(int, input().split()))
v = int(input())

cnt = 0
for num in nums:
    if num == v:
        cnt += 1
print(cnt)


# 실행 결과: 성공(메모리:31256kb, 시간:40ms)