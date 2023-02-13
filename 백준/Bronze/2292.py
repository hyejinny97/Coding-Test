# https://www.acmicpc.net/problem/2292
# 문제2292번.벌집
# 시간제한:2초, 메모리제한:128MB



# 입력
'''
1. 숫자 N
- 1 ≤ N ≤ 1,000,000,000
'''



# 출력
'''
1. 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력
'''



# 코드 

# 접근방법
'''
벌집 중앙에서부터 바깥쪽으로 1, (1x6) 6, (2x6) 12, (3x6) 18 ...개의 방 수만큼 한 층씩 쌓여나간다.

1  2  3   4   5   6   (층)
1  6  12  18  24  30  (층당 방 수)
1  7  19  37  61  91  (누적 방 수)

따라서, 58번 방은 37과 61 사이의 숫자이므로 5층에 위치하게 되고 최소 5개의 방을 지나면 도달할 수 있다.
'''

import sys

sys.stdin = open('input_text/2292.txt')

N = int(input())

floor = 0       # 현재 층
acc_rooms = 0   # 누적 방 수
while acc_rooms < N:
    floor += 1
    if floor == 1:   
        acc_rooms += 1
        continue
    acc_rooms += (floor - 1) * 6

print(floor)


# 실행결과(메모리:31256KB, 시간:44ms)