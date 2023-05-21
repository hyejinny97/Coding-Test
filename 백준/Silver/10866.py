# https://www.acmicpc.net/problem/10866
# 문제10866번.덱
# 시간: 0.5초, 메모리: 256MB



# 입력
'''
1. 명령의 수 N
- 1 ≤ N ≤ 10,000
2. N개의 줄에 명령
'''



# 출력
'''
1. 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력
'''



# 코드
import sys
from collections import deque

sys.stdin = open('input_text/10866.txt')

class deq:
    def __init__(self):
        self.deque = deque([])

    def push_front(self, x):
        self.deque.appendleft(x)

    def push_back(self, x):
        self.deque.append(x)

    def pop_front(self):
        print(self.deque.popleft() if self.deque else -1) 

    def pop_back(self):
        print(self.deque.pop() if self.deque else -1) 

    def size(self):
        print(len(self.deque))
    
    def empty(self):
        print(0 if self.deque else 1) 

    def front(self):
        print(self.deque[0] if self.deque else -1)

    def back(self):
        print(self.deque[-1] if self.deque else -1)


N = int(input())
deque1 = deq() 
for _ in range(N):
    command = input().split()
    if command[0] == 'push_front':
        deque1.push_front(command[1])
    if command[0] == 'push_back':
        deque1.push_back(command[1])
    if command[0] == 'pop_front':
        deque1.pop_front()
    if command[0] == 'pop_back':
        deque1.pop_back()
    if command[0] == 'size':
        deque1.size()
    if command[0] == 'empty':
        deque1.empty()
    if command[0] == 'front':
        deque1.front()
    if command[0] == 'back':
        deque1.back()

        
# 실행 결과: 성공(메모리:34128kb, 시간:100ms)