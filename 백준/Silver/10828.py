# https://www.acmicpc.net/problem/10828
# 문제10828번.스택
# 시간: 0.5초, 메모리: 256MB



# 입력
'''
1. 명령의 수 N
- 1 ≤ N ≤ 10,000
2. N개의 줄에 명령
- 명령 = push/pop/size/empty/top 중 하나 + [정수X]
- push X: 정수 X를 스택에 넣음
- pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력(정수가 없으면 -1 출력)
- size: 스택에 들어있는 정수의 개수를 출력
- empty: 스택이 비어있으면 1, 아니면 0을 출력
- top: 스택의 가장 위에 있는 정수를 출력(정수가 없으면 -1 출력)
'''



# 출력
'''
1. 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/10828.txt')

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        if self.stack:
            print(self.stack.pop())
            return
        print(-1)
    
    def size(self):
        print(len(self.stack))
    
    def empty(self):
        print(0 if self.stack else 1)
    
    def top(self):
        if self.stack:
            print(self.stack[-1])
            return
        print(-1)


N = int(sys.stdin.readline())
stack = Stack()
for _ in range(N):
    line = sys.stdin.readline().split()
    if line[0] == 'push':
        command, num = line
        stack.push(num)
    if line[0] == 'pop':
        stack.pop()
    if line[0] == 'size':
        stack.size()
    if line[0] == 'empty':
        stack.empty()
    if line[0] == 'top':
        stack.top()


# 실행 결과: 성공(메모리:31256kb, 시간:52ms)