# https://www.acmicpc.net/problem/10250
# 문제10250번.ACM 호텔
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. T줄마다 호텔의 층 수 H, 각 층의 방 수 W, 몇 번째 손님 N
- 1 ≤ H, W ≤ 99
- 1 ≤ N ≤ H x W
'''



# 출력
'''
1. T줄마다 N 번째 손님에게 배정되어야 하는 방 번호를 출력

<방 배정 규칙>
- 호텔 정문으로부터 걷는 거리가 가장 짧도록 방을 배정
- 다만, 걷는 거리가 같을 때에는 아래층의 방으로 배정
'''



# 코드

# 접근 방법
'''
아래에서부터 위로 방을 차례대로 배정하면 됨
W = 12, H = 6일때

방번호  손님번호  
601     ↑ 6        602     ↑ 12
501     ↑ 5        502     ↑ 11
401     ↑ 4        402     ↑ 10
301     ↑ 3        302     ↑ 9
201     ↑ 2        202     ↑ 8
101     ↑ 1        102     ↑ 7

방 번호를 YXX 또는 YYXX라고 할 때,
Y(YY) = 층 수
XX = 엘리베이터에서부터 세었을 때의 번호

손님이 배정받을 XX = (손님번호 - 1) // H + 1
손님이 배정받을 YY = (손님번호 - 1) % H + 1

- f-string 참고: https://axis.tistory.com/entry/Python-f-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%8F%AC%EB%A7%A4%ED%8C%85-f-string-formatting
'''

import sys

sys.stdin = open('input_text/10250.txt')

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    X = (N - 1) // H + 1
    Y = (N - 1) % H + 1
    print(f'{Y}{X:0>2}')


# 실행 결과: 성공(메모리:31256kb, 시간:52ms)