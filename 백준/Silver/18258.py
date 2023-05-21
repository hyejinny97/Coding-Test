# https://www.acmicpc.net/problem/18258
# 문제18258번.큐2
# 시간: 1초, 메모리: 512MB



# 입력
'''
1. 명령의 수 N
- 1 ≤ N ≤ 2,000,000
2. N개의 줄에 명령이 하나씩 주어짐
'''



# 출력
'''
1. 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력

<명령>
- push X: 정수 X를 큐에 넣는 연산
- pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력(없는 경우에는 -1을 출력)
- size: 큐에 들어있는 정수의 개수를 출력
- empty: 큐가 비어있으면 1, 아니면 0을 출력
- front: 큐의 가장 앞에 있는 정수를 출력(없는 경우에는 -1을 출력)
- back: 큐의 가장 뒤에 있는 정수를 출력(없는 경우에는 -1을 출력)
'''



# 코드
import sys
from collections import deque

sys.stdin = open('input_text/18258.txt')

class q:
    def __init__(self):
        self.queue = deque([])

    def push(self, x):
        self.queue.append(x)
    
    def pop(self):
        print(self.queue.popleft() if self.queue else -1)

    def size(self):
        print(len(self.queue))

    def empty(self):
        print(0 if self.queue else 1)

    def front(self):
        print(self.queue[0] if self.queue else -1)

    def back(self):
        print(self.queue[-1] if self.queue else -1)


N = int(input())
queue = q()
for _ in range(N):
    command = input().split()
    if len(command) == 2:
        queue.push(command[1])
    elif command[0] == 'pop':
        queue.pop()
    elif command[0] == 'size':
        queue.size()
    elif command[0] == 'empty':
        queue.empty()
    elif command[0] == 'front':
        queue.front()
    elif command[0] == 'back':
        queue.back()

     
# 실행 결과: 성공(메모리:37480kb, 시간:3704ms)