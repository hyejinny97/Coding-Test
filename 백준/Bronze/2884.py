# https://www.acmicpc.net/problem/2884
# 문제2884번.알람 시계
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 현재 상근이가 설정한 놓은 알람 시간 H시 M분
- 0 ≤ H ≤ 23
- 0 ≤ M ≤ 59
'''



# 출력
'''
1. 설정해야 하는 알람 시간을 출력
- 알람을 45분 앞서는 시간으로 바꾸어 출력
- 시간을 나타낼 때, 불필요한 0은 사용하지 않는다
'''



# 코드
import sys

sys.stdin = open('input_text/2884.txt')

h, m = map(int, input().split())

if m < 45:
    m = 60 + (m - 45)
    if h == 0:
        h = 23
    else:
        h -= 1
else:
    m -= 45

print(h, m)


# 실행 결과: 성공(메모리:30616kb, 시간:36ms)