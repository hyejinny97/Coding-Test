# https://www.acmicpc.net/problem/1110
# 문제1110.더하기 사이클
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 정수 N
- 0 <= N <= 99
'''



# 출력
'''
1. N의 사이클 길이를 출력

<한 사이클>
1) 정수의 각 자리수 더함
- 주어진 정수가 10보다 작다면, 앞에 0을 붙여 두자리수로 만듦
2) 정수의 오른쪽 자리수 + 더한 값의 오른쪽 자리수 = 다음 사이클의 정수
'''



# 코드
import sys

sys.stdin = open('input_text/1110.txt')

N = int(input())

now = N   # 현재 정수
cnt = 0   # 사이클 수
while True:
    cnt += 1

    # 각 자리수를 더함
    sum_n = 0
    for n in str(now):
        sum_n += int(n)
    
    # 다음 사이클의 정수 = 정수의 오른쪽 자리수 + 더한 값의 오른쪽 자리수
    next = (now % 10) * 10 + sum_n % 10
    
    # 다음 사이클의 정수가 시작 정수와 동일하면 반복 중단
    if next == N:
        print(cnt)
        break
    else:
        now = next



# 실행 결과: 성공(메모리:30840kb, 시간:76ms)