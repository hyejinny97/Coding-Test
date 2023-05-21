# https://www.acmicpc.net/problem/11866
# 문제11866번.요세푸스 문제 O
# 시간: 2초, 메모리: 512MB



# 입력
'''
1. N명의 사람, K번째 사람을 제거
- 1 ≤ K ≤ N ≤ 1,000
'''



# 출력
'''
1. 요세푸스 순열을 출력
- 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있음
- 순서대로 K번째 사람을 제거
- 이 과정은 N명의 사람이 모두 제거될 때까지 계속됨
'''



# 코드
import sys
from collections import deque

sys.stdin = open('input_text/11866.txt')

N, K = map(int, input().split())

seq = deque(range(1, N + 1))   # 원을 이루면서 앉은 N명
rst = []   # 요세푸스 순열
while seq:
    cnt = 1
    while cnt < K:
        seq.append(seq.popleft())
        cnt += 1
    rst.append(str(seq.popleft()))

print(f"<{', '.join(rst)}>")


# 실행 결과: 성공(메모리:34104kb, 시간:128ms)