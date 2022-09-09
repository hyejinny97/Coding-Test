# https://www.acmicpc.net/problem/2564
# 문제2564번.경비원
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 블록의 가로길이, 세로길이
- 0 < 길이 <= 100
2. 상점의 갯수 N
- 0 < 개수 <= 100
3. N개의 줄에 상점이 위치한 방향, 블록의 왼쪽/위쪽 경계로부터의 거리
방향: 1(북), 2(남), 3(서), 4(동)
4. 마지막 줄에 동근이의 위치한 방향, 블록의 왼쪽/위쪽 경계로부터의 거리
- 동근이의 위치는 블록의 꼭짓점이 될 수 없음
'''



# 출력
'''
1. 동근이의 위치와 각 상점 사이의 최단 거리의 합
'''


# 코드 1
import sys

sys.stdin = open('input_text/2564.txt')

w, h = map(int, input().split())
N = int(input())

# 세 가게의 위치와 동근이의 위치 받기
stores = []   # 값: 세 가게의 위치(r, c)
for n in range(N + 1):
    dir, dis = map(int, input().split())

    if dir == 1:      # 북쪽
        loc = (h, dis)   # (r, c)
    elif  dir == 2:   # 남쪽
        loc = (0, dis)
    elif dir == 3:    # 서쪽
        loc = (h - dis, 0)
    elif dir == 4:    # 동쪽
        loc = (h - dis, w)

    # 동근이의 위치
    if n == N:   
        dong_r, dong_c = loc
    # 세 상점의 위치
    else:
        stores.append(loc)

# 동근이가 세 상점에 도착하기 위해 이동해야하는 총 거리 출력
tot_dis = 0  
for store_r, store_c in stores:
    arrival = False   # 동근이가 상점에 도착 여부
    r, c = dong_r, dong_c   # 동근이 위치 초기화
    clockwise = 0   # 시계방향으로 이동했을때 거리 초기화

    dr = [1, 0, -1, 0]    # 시계방향(북동남서)
    dc = [0, 1, 0, -1]
    # 동근이의 처음 시작 방향 정하기
    if dir == 1:
        i = 1
    elif dir == 2:
        i = 3
    elif dir == 3:
        i = 0
    elif dir == 4:
        i = 2
        
    while True:
        while True:
            nr = r + dr[i]
            nc = c + dc[i]

            # 다음 위치가 상점의 위치인 경우
            if nr == store_r and nc == store_c:
                clockwise += 1
                arrival = True
                break
            # 다음 위치가 이동불가한 경로인 경우
            if nr < 0 or nr > h or nc < 0 or nc > w or (0 < nr < h and 0 < nc < w):
                i = (i + 1) % 4
                break
            r, c = nr, nc
            clockwise += 1
        
        # 시계방향으로 이동해 상점에 도착한 경우, 
        # 시계방향/반시계방향 중 거리가 더 짧은 것을 선택
        if arrival:
            tot_dis += min(clockwise, 2 * w + 2 * h - clockwise)
            break

print(tot_dis)



# 실행 결과: 성공(메모리:30840kb, 시간:80ms)



# 코드 2
import sys

sys.stdin = open('input_text/2564.txt')

# 사각형의 왼쪽 위 부분(0, h)을 잘라 일자로 펼쳤다고 생각
def distance(dir, dis):
    if dir == 1:   # 북
        return dis
    elif dir == 2:   # 남
        return w + h + w - dis
    elif dir == 3:   # 서
        return w + h + w + h - dis
    elif dir == 4:   # 동
        return w + dis


w, h = map(int, input().split())
N = int(input())

# 세 가게의 위치와 동근이의 위치 받기
locations = []   # 값: 세 가게의 위치와 동근이의 위치(r, c)
for _ in range(N + 1):
    dir, dis = map(int, input().split())
    locations.append(distance(dir, dis))

# 동근이가 세 상점에 도착하기 위해 이동해야하는 총 거리 출력
dong = locations.pop()   # 동근이의 위치
l = 2 * w + 2 * h
tot_dis = 0
for dis in locations:
    tot_dis += min(abs(dis - dong), l - abs(dis - dong))
print(tot_dis)



# 실행 결과: 성공(메모리:30840kb, 시간:68ms)