# https://www.acmicpc.net/problem/1436
# 문제1436번.영화감독 숌
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 자연수 N
- 0 < N <= 10,000
'''



# 출력
'''
1. N번째 영화의 제목에 들어간 수를 출력
'''



# 코드
import sys

sys.stdin = open('input_text/1436.txt')

N = int(input())

num = 666   # 현재 수
cnt = 0     # '666'이 나온 횟수
while True:
    if '666' in str(num):
        cnt += 1
    
    if cnt == N:
        break
    
    num += 1

print(num)


# 실행 결과: 성공(메모리:31388kb, 시간:620ms)