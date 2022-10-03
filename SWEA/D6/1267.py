# 문제1267번.작업순서
# 시간: 30초, 메모리: 256MB


# 입력
"""
<총 10개의 테스트 케이스>
1. 정점의 개수 V, 간선의 개수 E
- 3 <= V <= 1,000
- 2 <= E <= 3,000
- 정점의 번호는 1부터 V까지의 정수값
- 간선은 간선을 이루는 두 정점으로 표기
- 예) 정점 5에서 28로 연결되는 간선은 “5 28”로 표기
"""


# 출력
"""
1. #{테스트케이스} {올바른 작업 순서}
- 그래프에서 각 작업은 하나씩의 정점으로 표시되고 선행 관계는 방향성을 가진 간선으로 표현
- 선행 관계: 어떤 작업은 특정 작업이 끝나야 시작할 수 있음
"""


# 코드
import sys
from collections import defaultdict

sys.stdin = open("../input_text/1267.txt")


def work_seq(depart):
    stack = [] + list(depart)  # 지금 당장 수행 가능한 작업들
    work = []  # 수행 완료한 작업 순서
    while stack:
        node = stack.pop()  # 현재 수행하려는 작업

        # 수행 중인 작업 기록
        work.append(node)

        # 다음으로 수행 가능한 작업 탐색
        if node in forward:
            for next in forward.get(node):
                # 수행 가능하려면 이전 작업을 모두 수행한 노드여야 함
                for prev in reverse.get(next):
                    if prev not in work:
                        break
                else:
                    stack.append(next)

    return work


T = 10
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    info = list(map(int, input().split()))

    # E개의 간선 정보를 읽으면서, 순방향/역방향 기록
    forward = defaultdict(list)  # start: [end]
    reverse = defaultdict(list)  # end: [start]
    for i in range(0, 2 * E, 2):
        start, end = info[i], info[i + 1]

        # 순방향 기록
        forward[start].append(end)

        # 역방향 기록
        reverse[end].append(start)

    # 시발점 찾기 (시발점은 end가 될 수 없음)
    depart = set(range(1, V + 1)) - set(reverse.keys())

    # 작업 순서 출력
    print(f"#{test_case}", *work_seq(depart))


# 실행 결과: 성공(메모리:65,872 kb, 시간:227 ms)
