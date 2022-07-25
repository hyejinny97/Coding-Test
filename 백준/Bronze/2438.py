# https://www.acmicpc.net/problem/2438
# 문제2438.별찍기-1
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 정수 N
- 1 <= N <= 100
'''



# 출력
'''
1. 별 1개 출력
2. 별 2개 출력
...
N. 별 N개 출력
'''



# 코드
N = int(input())
for n in range(1, N + 1):
    print('*' * n)



# 실행결과(메모리:30840KB, 시간:76ms)