# https://www.acmicpc.net/problem/1021
# 문제1021번.회전하는 큐
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 양방향 순환 큐의 크기 N, 뽑아내려고 하는 수의 개수 M
- 0 < M <= N <= 50
- 큐는 1부터 N까지의 원소를 포함하고 있음
2. 지민이가 뽑아내려고 하는 M개의 수의 위치
'''



# 출력
'''
1. 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력

<3가지 연산>
1. 첫 번째 원소를 뽑아낸다
2. 왼쪽으로 한 칸 이동시킨다. 
3. 오른쪽으로 한 칸 이동시킨다. 
'''



# 코드
import sys
from collections import deque

sys.stdin = open('input_text/1021.txt')

N, M = map(int, input().split())
locations = list(map(int, input().split()))  # 뽑아내려고 하는 수의 위치
q = deque(range(1, N + 1))

cnt = 0   # 2,3번 연산 횟수
for loc in locations:
    front = q.index(loc)             # 원하는 수 앞의 원소 개수
    back = (len(q) - 1) - front      # 원하는 수 뒤의 원소 개수
    if front <= back + 1:  
        q.rotate(-front)   # 오른쪽으로 이동
        cnt += front
    else:
        q.rotate(back + 1)   # 왼쪽으로 이동
        cnt += back + 1
    q.popleft()   # 첫번째 원소를 뽑아냄

print(cnt)


# 실행 결과: 성공(메모리:34272kb, 시간:104ms)