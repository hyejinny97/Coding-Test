# https://www.acmicpc.net/problem/2527
# 문제2527번.직사각형
# 시간: 1초, 메모리: 128MB



# 입력
'''
<총 4개의 줄>
1. 각 줄에는 8개의 정수 좌하측 꼭지점 (x, y), 우상측 꼭지점 (p, q)
- x < p, y < q
- 첫 4개의 정수는 첫 번째 직사각형
- 나머지 4개의 정수는 두 번째 직사각형
- 1 <= 좌표 값 <= 50,000
'''



# 출력
'''
1. 4개의 각 줄에 주어진 두 직사각형의 공통부분을 조사해서 해당하는 코드 문자를 출력
<공통부분의 특성에 따른 코드 문자>
1) 직사각형 -> a
2) 선분 -> b
3) 점 -> c
4) 공통부분 없음 -> d
'''



# 코드
import sys

sys.stdin = open('input_text/2527.txt')

for _ in range(4):
    # 두 직사각형 중 x좌표가 더 좌측에 있는 직사각형을 앞 좌표에 넣기
    nums = list(map(int, input().split()))
    if nums[0] <= nums[4]:
        x1, y1, p1, q1 = nums[0:4]
        x2, y2, p2, q2 = nums[4:]
    else:
        x1, y1, p1, q1 = nums[4:]
        x2, y2, p2, q2 = nums[0:4]

    # 공통부분의 특성에 따른 코드 문자 출력
    if (x2 == p1 and y2 == q1) or (p1 == x2 and y1 == q2):   # 점
        print('c')
    elif p1 < x2 or q1 < y2 or q2 < y1:   # 공통부분이 없음
        print('d')
    elif x2 == p1 or q1 == y2 or y1 == q2:   # 선분
        print('b')
    else:   # 직사각형
        print('a')



# 실행 결과: 성공(메모리:30840kb, 시간:68ms)