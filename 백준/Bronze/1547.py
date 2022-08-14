# https://www.acmicpc.net/problem/1547
# 문제1547번.공
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 컵의 위치를 바꾼 횟수 M
- 0 < M <= 50
2. M개의 줄에 컵의 위치를 바꾼 방법X와 Y
- X번 컵과 Y번 컵의 위치를 서로 바꾸는 것을 의미
- 0 < X, Y <= 3
'''



# 출력
'''
1. 공이 들어있는 컵의 번호 출력, 공이 사라져서 컵 밑에 없는 경우엔 -1 출력
- 컵의 번호는 맨 왼쪽 컵부터 순서대로 1, 2, 3번
- 가장 첨에 1번 컵 아래에 공을 넣음
'''



# 코드
import sys

sys.stdin = open('input_text/1547.txt')

M = int(input())
cups = {1:1, 2:2, 3:3}   # 키: 컵 번호, 값: 각 컵이 위치한 자리
for _ in range(M):  
    swap1, swap2 = map(int, input().split())
    cups[swap1], cups[swap2] = cups[swap2], cups[swap1]
    
for num, loc in cups.items():
    if loc == 1:
        print(num)



# 실행 결과: 성공(메모리:30840kb, 시간:76ms)