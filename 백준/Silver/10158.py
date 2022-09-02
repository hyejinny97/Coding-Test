# https://www.acmicpc.net/problem/10158
# 문제10158번.개미
# 시간: 0.15초, 메모리: 256MB



# 입력
'''
1. 격자의 너비 w, 높이 h
- 2 <= w, h <= 40,000
2. 개미의 초기 위치 가로 p, 세로 q
- 0 < p < w
- 0 < q < h
3. 개미가 움직일 시간 t
- 1 <= t <= 200,000,000
- (p,q)에서 출발한 개미는 1시간 후에는 (p+1,q+1)로 옮겨감
'''



# 출력
'''
1. t시간 후에 개미의 위치 좌표(x,y) 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/10158.txt')

w, h = map(int, input().split())
c, r = map(int, input().split())
t = int(input())

dr, dc = 1, 1   # 시작: 오른쪽 45도 방향
for _ in range(t):
    # (r, c)가 격자의 모서리에 있는 경우
    if (c, r) in {(w, h), (w, 0), (0, h), (0, 0)}:   
        dr *= -1
        dc *= -1
    elif c == w:
        dc *= -1
    elif r == h:
        dr *= -1 
    elif r <= 0:
        dr *= -1 
    elif c <= 0: 
        dc *= -1
    
    r += dr
    c += dc

print(c, r)



# 실행 결과: 실패(시간초과)



# 코드 2
import sys

sys.stdin = open('input_text/10158.txt')

w, h = map(int, input().split())
c, r = map(int, input().split())
t = int(input())

# r, c 방향에 각각 그림자를 비춘다고 생각하면 격자 내에서 진동하는 것처럼 보임
if ((c + t) // w) % 2 == 1:
    c = w - (c + t) % w
else:
    c = (c + t) % w

if ((r + t) // h) % 2 == 1:
    r = h - (r + t) % h
else:
    r = (r + t) % h

print(c, r)



# 실행 결과: 성공(메모리:30840KB, 시간:68ms)