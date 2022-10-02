# 문제10580번.전봇대
# 시간: 2초, 메모리: 256MB


# 입력
"""
1. 테스트 케이스 T
2. 전선의 개수 N
- 1 <= N <= 1,000
3. 첫번째 전봇대가 걸려있는 고도 Ai (cm), 두번째 전봇대가 걸려있는 고도 Bi (cm)
- 1 ≤ Ai, Bi ≤ 10,000
- 세 전선이 한 점에서 만나지 않게 입력이 주어짐
"""


# 출력
"""
1. #{테스트케이스} {교차점의 개수}
"""


# 접근방법
"""
다른 전선이 전선 자신의 A 전봇대 고도보다는 높고 B 전봇대 고도보다는 낮으면 교차함
"""


# 코드
import sys

sys.stdin = open("../input_text/10580.txt")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # 전봇대 정보 입력 받기
    As = []
    Bs = []
    for _ in range(N):
        A, B = map(int, input().split())
        As.append(A)
        Bs.append(B)

    # A와 B 전봇대를 순회하면서 카운트
    cnt = 0
    for i in range(N):  # 기준 전선
        for j in range(N):  # 비교할 전선들
            if As[i] < As[j] and Bs[i] > Bs[j]:
                cnt += 1

    print(f"#{test_case} {cnt}")


# 실행 결과: 성공(메모리:63,708 kb, 시간:358 ms)
