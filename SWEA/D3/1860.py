# 문제1860번.진기의 최고급 붕어빵
# 시간: 4초, 메모리: 256MB


# 입력
"""
1. 테스트 케이스 수 T
2. 예약 받은 사람의 수 N명, M초, M초당 만들 수 있는 붕어빵 개수 K개
- 1 ≤ N, M, K ≤ 100
- 진기는 0초부터 붕어빵을 만들기 시작
- M초당 K개의 붕어빵을 만들 수 있음
3. N명의 각 사람이 언제 도착하는지를 초 단위로 정보가 주어짐
- 0 <= 초 <= 11,111
"""


# 출력
"""
1. #{테스트케이스} {모든 손님에 대해 기다리는 시간이 없이 붕어빵을 제공할 수 있으면 “Possible”을, 아니라면 “Impossible”}
- '0초 이후'에 손님들이 언제 도착하는지 주어지면, 모든 손님들에게 기다리는 시간없이 붕어빵을 제공할 수 있는지 판별
"""


# 코드
import sys

sys.stdin = open("../input_text/1860.txt")

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())

    # 각 시간대마다 손님이 오는 수 기록
    people = [0] * 11112  # 인덱스: 초, 값: 오는 사람 수
    for sec in map(int, input().split()):
        people[sec] += 1

    # 맨 마지막 손님이 오는 시간까지 반복
    bread = 0  # 여분의 붕어빵 수
    rst = "Possible"
    for sec in range(0, 11111 + 1):
        # 빵 만들기
        if sec and sec % M == 0:
            bread += K

        # 손님에게 빵 나눠주기
        if people[sec]:
            if bread >= people[sec]:
                bread -= people[sec]
            else:
                rst = "Impossible"
                break

    # 모든 손님에 대해 기다리는 시간이 없이 붕어빵을 제공할 수 있는지
    print(f"#{test_case} {rst}")


# 실행 결과: 성공(메모리:65,904 kb, 시간:485 ms)
