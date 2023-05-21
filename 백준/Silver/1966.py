# https://www.acmicpc.net/problem/1966
# 문제1966번.프린터 큐
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 테스트케이스의 수
2. 첫 번째 줄에는 문서의 개수 N, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M
- 1 ≤ N ≤ 100
- 0 ≤ M < N
- 맨 왼쪽은 0번째
3. 두 번째 줄에는 N개 문서의 중요도
- 1 <= 중요도 <= 9
- 중요도가 같은 문서가 여러 개 있을 수도 있음
'''



# 출력
'''
1. 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력

<인쇄 조건>
- 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인
- 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
'''



# 코드
import sys
from collections import deque

sys.stdin = open('input_text/1966.txt')

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    importance = deque(input().split())
    for i in range(N):
        importance[i] = (i, int(importance[i]))   # 원래 인덱스 위치, 중요도
    
    rst = 0   # 원하는 문서가 몇 번째로 출력되는지
    while True:
        if importance[0][1] == max(importance, key=lambda x: x[1])[1]:
            doc = importance.popleft()
            rst += 1
            if doc[0] == M:
                break
        else:
            importance.append(importance.popleft())

    print(rst)


# 실행 결과: 성공(메모리:34128kb, 시간:100ms)